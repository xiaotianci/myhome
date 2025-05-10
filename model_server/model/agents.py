from abc import ABC, abstractmethod
from global_config import *
import torch
from fastapi import APIRouter,FastAPI,Request

class Infer_agent(ABC):

    @abstractmethod
    def __init__(self):
        """
        子类必须实现，且只能设置 self.a 和 self.b
        """
        self.device = "cuda" if torch.cuda.is_available() else 'cpu'

    @abstractmethod
    def start(self):
        "初始化模型"
        pass

    @abstractmethod
    def infer(self):
        "推理函数"
    
    # def __setattr__(self, key, value):
    #     # 限制只能设置 a 和 b
    #     if not hasattr(self, '_initialized'):
    #         # 初始化阶段允许设置
    #         super().__setattr__(key, value)
    #     elif key not in ('a', 'b'):
    #         raise AttributeError(f"不允许设置其他属性: {key}")
    #     else:
    #         super().__setattr__(key, value)


class QWEN3_0D6B_float16_agent(Infer_agent):
    def __init__(self):
        super().__init__()
        self.model_path = QWEN3_0D6B_float16

    def start(self):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_path,
            torch_dtype="auto",
            device_map="auto"
        )
        self.model.to(self.device)

    def infer(self,prompt = "Give me a short introduction to large language model."):
        messages = [
            {"role": "user", "content": prompt}
        ]
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        # conduct text completion
        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=32768
        )
        output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

        # parsing thinking content
        try:
            # rindex finding 151668 (</think>)
            index = len(output_ids) - output_ids[::-1].index(151668)
        except ValueError:
            index = 0

        thinking_content = self.tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
        content = self.tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

        print("thinking content:", thinking_content)
        print("content:", content)
        ans = f"<think>:{thinking_content}\n<content>:{content}"
        return ans



class Register:
    def __init__(self,infet_agent_names :str = default_model):
        self.router = APIRouter()
        self.router.add_api_route("/infer/",self.infer,methods=["POST"])
        
        if infet_agent_names.split('_agent')[0] not in support_model:
            raise "暂不支持该模型"
        agent_name = f'{infet_agent_names}_agent'
        self.model = globals()[agent_name]()
        self.model.start()

    async def infer(self,data : Request):
        data = await data.json()
        prompt = data['prompt']
        answer = self.model.infer(prompt)
        return answer

app = FastAPI()
controller = Register()
app.include_router(controller.router)