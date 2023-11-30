import requests
import time
import json


class ChaGPT:
    def __init__(self, api_key, model="gpt-3.5-turbo") -> None:
        self.api_key = api_key
        self.model = model
        self.temperature = 0.75
        self.url = "https://openkey.cloud/v1/chat/completions"
        self.stream = True

    def chat(self, messages):
        try:
            response = requests.post(
                self.url,
                headers=self.__header(),
                json=self.__body(messages),
                stream=True,
            )

            if response.status_code != 200:
                errorResponse = Error(response.json(), response.status_code)
                return errorResponse.error_message()

            return response.iter_lines()

        except Exception as e:
            print("openai调用异常：", e)

    def __header(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

    def __body(self, message):
        return {
            "model": self.model,
            "messages": message,
            "temperature": self.temperature,
            "stream": True,
        }


class Error:
    def __init__(self, response, code=400) -> None:
        self.message = "异常错误"
        self.code = code
        self.type = ""

        if "error" in response:
            error = response["error"]
            self.message = error.get("message", "异常错误")
            self.type = error.get("type")

    def error_message(self):
        yield {
            "id": "-1",
            "created": int(time.time()),
            "model": "gpt-3.5-turbo",
            "choices": [{"delta": self.message, "finish_reason": "stop"}],
        }


class Response:
    def __init__(self, response) -> None:
        self.id = "-1"
        self.created = -1
        self.model = ""
        self.choices = []
        self.role = "assistant"

        if response is None:
            return

        if isinstance(response, bytes):
            response = self.__convert_bytes(response)

        if len(response) == 0:
            return

        self.id = response.get("id", "-1")
        self.created = response.get("created", -1)
        self.model = response.get("model", "gpt-3.5-turbo")
        self.choices = response.get("choices", [])
        self.role = (
            "assistant"
            if len(self.choices) == 0
            else self.choices[0].get("delta", {}).get("role", "assistant")
        )

    def getContent(self):
        content = ""
        for choice in self.choices:
            if "delta" in choice:
                delta = choice["delta"]
                content += delta.get("content", "")
        return content

    def isStop(self):
        flag = False

        for choice in self.choices:
            if "delta" in choice:
                delta = choice["delta"]
                finish_reason = delta.get("finish_reason")
                flag = finish_reason == "stop"

        return flag

    def __convert_bytes(self, response):
        message = str(response.decode())
        flag_str = "data: "
        index = message.find(flag_str)
        if index == -1 or message.find("[DONE]") != -1:
            return {}

        json_content = message[(index + len(flag_str)) :]
        res = json.loads(json_content)
        return res


if __name__ == "__main__":
    gpt = ChaGPT("sk-HNEndMOWrHGpnrYS405093141b294b5aB3Ea646dC992C4D6", "")
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ]

    chunks = gpt.chat(messages)
    content = ""
    for chunk in chunks:
        if not chunk:
            continue
        res = Response(chunk)
        content += res.getContent()

    print(content)
