# -*- coding: utf-8 -*-
from transformers import BertTokenizer, GPT2LMHeadModel
import torch
from fastapi import FastAPI,Request
app = FastAPI()

def generate_answer(input_text,model,max_len = 50):
    model.eval()
    model.to(device)
    input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)
    # input_ids = tokenizer.encode(f"{question}[UNK]", return_tensors="pt").to(device)

    # 生成文本
    with torch.no_grad():
        for _ in range(max_len):
            outputs = model(input_ids=input_ids)
            predicted_token_ids = torch.argmax(outputs.logits, dim=-1)

            input_ids = torch.cat((input_ids, torch.tensor([[predicted_token_ids[0,-1]]]).to(device)), dim=1)

            # 解码生成的文本
            generated_text = tokenizer.decode(input_ids[0], skip_special_tokens=True)
            # print(predicted_token_ids[:,-1])
            if predicted_token_ids[:,-1] == 102:
                break
        # print(generated_text)
    return generated_text

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = BertTokenizer.from_pretrained(r"F:\project\model_params\gpt2\gpt2-chinese-cluecorpussmall-tokenizer")
model = GPT2LMHeadModel.from_pretrained(r'F:\project\model_params\gpt2\gpt2-chinese-cluecorpussmall')
model.to(device)


@app.post("/infer/")
async def get_ans_from_question(data : Request):
    data = await data.json()
    question = data['question']
    ans = generate_answer(question, model)
    res = {'result':ans}
    return res


