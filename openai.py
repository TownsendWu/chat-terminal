import requests
import json
API_KEY = "sk-HNEndMOWrHGpnrYS405093141b294b5aB3Ea646dC992C4D6"

text = """我将给你一片长文章，我需要你帮我做一下几件事：
1. 提取文章中的关键字
2. 将文章进行分类
3. 根据实际情况做一个 200~800字的概括性总结
4. 按以上要求格式化输出
"""

def chat():
    # url = "https://api.openai.com/v1/chat/completions"
    url = "https://openkey.cloud/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        # 填写OpenKEY生成的令牌/KEY，注意前面的 Bearer 要保留，并且和 KEY 中间有一个空格。
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "调用openai时如何保持上下文的对话"},
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    print("Status Code", response.status_code)
    print(response.text)
    res = response.json()
    choices = res["choices"]
    for choice in choices:
        print(choice["message"]["content"])


def read_txt():
    text = ""
    with open("./data/test_data.txt","r",encoding="utf8") as f:
        line = f.readline()
        while line:
            text = text + line
            line = f.readline()
    
    return text


def streamingChat():
    url = "https://openkey.cloud/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        # 填写OpenKEY生成的令牌/KEY，注意前面的 Bearer 要保留，并且和 KEY 中间有一个空格。
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "你是一个强大的编程助手"},
            {"role": "user", "content": "请问vue是什么"},
        ],
        "stream": True
    }

    response = requests.post(url, headers=headers, json=data,stream=True)

    for chunk in response.iter_lines():
        if not chunk:
            continue
        # message = json.loads(chunk)
        message = str(chunk.decode())
        flag_str = "data: "
        index = message.find(flag_str)
        if index == -1 or message.find("[DONE]") != -1:
            continue
        json_content = message[(index + len(flag_str)):]
        res = json.loads(json_content)
        print(res.get("choices"))


def img():
    url = "https://openkey.cloud/v1/images/generations"

    # 创建一个生成图像的请求的数据
    payload = {
        "model": "dall-e-3",
        "prompt": "generate a logo using the notion and bookmarks keywords", # 描述你想生成的图像
        "n": 1,  # 生成图像的数量
        "size": "128x128"  # 生成图像的尺寸
    }

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    # 检查响应状态
    if response.status_code == 200:
        # 解析响应数据
        data = response.json()
        print(data)
    else:
        print("Failed to generate image:", response.status_code, response.text)

    # 如果需要将图像保存到文件
    # 假设API返回的数据中包含了图像的URL
    image_url = data['data'][0]['urls'][-1]  # 获取图像的URL

    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        with open('./data/generated_image.png', 'wb') as f:
            f.write(image_response.content)
        print("Image saved as 'generated_image.png'.")
    else:
        print("Failed to download image:", image_response.status_code, image_response.text)


chat()