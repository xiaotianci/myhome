# from langchain.llms import HuggingFaceLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 创建一个简单的Prompt模板
prompt_template = """
你是一个非常聪明的助手，你会根据用户的需求执行不同的任务。
用户请求: {user_input}
"""

# 加载本地模型（使用 HuggingFace 的 GPT-Neo 模型）
# local_llm = HuggingFaceLLM(model_name="EleutherAI/gpt-neo-2.7B", device="cpu")  # 这里选择CPU或GPU
class gpt:
    def __init__(self):
        self.name = 123

    def test(self):
        return 123
    
    def __call__(self, *args, **kwds):
        return self.test()

local_llm = gpt()
# 创建一个处理输入的Prompt链
prompt = PromptTemplate(input_variables=["user_input"], template=prompt_template)
llm_chain = LLMChain(prompt=prompt, llm=local_llm)

# 定义一个任务：根据输入的文本做简单的文本处理
def process_input(user_input: str) -> str:
    response = llm_chain.run(user_input)
    return response

# 创建一个Agent类，负责处理不同的任务
class SimpleAgent:
    def __init__(self):
        self.chain = llm_chain

    def run(self, user_input: str) -> str:
        # 在这里可以添加更多的任务逻辑
        print("执行任务：", user_input)
        result = process_input(user_input)
        return result

# 创建一个Agent实例并执行任务
agent = SimpleAgent()
user_input = "帮我分析一下这个文本的情感"
result = agent.run(user_input)
print("Agent的响应:", result)
