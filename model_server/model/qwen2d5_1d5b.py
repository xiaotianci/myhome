# -*- coding: utf-8 -*-
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from fastapi import FastAPI,Request
app = FastAPI()


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_path = 'F:\project\model_params\Qwen2.5-1.5B-Instruct'
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_path)


def generate_answer_qwen(question,model,tokenizer,max_len = 64):
    model.eval()
    model.to(device)
    question = [
            {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    question = tokenizer.apply_chat_template(
        question,
        tokenize=False,
        add_generation_prompt=True
        )
    model_inputs = tokenizer([question], return_tensors="pt").to(model.device)
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=max_len
        )
    generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return {'result':response}

@app.post("/infer/")
async def get_ans_from_question(data : Request):
    data = await data.json()
    question = data['question']

    ans = generate_answer_qwen(question, model, tokenizer)
    res = {'result':ans}
    return res


