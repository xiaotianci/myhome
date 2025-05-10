import requests

# 发送数据到 FastAPI 服务器
def send_inference_request(input_data: str):
    url = "http://127.0.0.1:9363/infer/"
    data = {"prompt": input_data}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        result = response.json()
        print(result["result"])
    else:
        print("Error:", response.status_code)

# 示例请求
if __name__ == "__main__":
    send_inference_request("你觉得特朗普牛逼吗？")




