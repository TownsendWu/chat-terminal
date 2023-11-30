from .entity import Person, Robot, Common
from .openai import ChaGPT, Response
from .context import ContextManager
import os
from pathlib import Path
import sys


common = Common()
me = Person()
robot = Robot()


def cli():
    contextManager = ContextManager()

    api_key = initApiKey()

    chatGpt = ChaGPT(api_key)

    common.welcome()
    while True:
        input = me.input()

        if input == "quit":
            robot.print("bye ~")
            break

        if input == "clear":
            common.clear()
            continue

        if input == "context":
            common.context(contextManager.get())
            continue

        if input == "reset":
            api_key = initApiKey(True)
            chatGpt = ChaGPT(api_key)
            robot.print("apikey已重置，可以开始问答了~")
            continue

        cnt = 1
        contextManager.add("user", input)

        try:
            recordText = ""
            messages = contextManager.get()
            chunks = chatGpt.chat(messages)
            robot.print(end="")
            for chunk in chunks:
                res = Response(chunk)
                content = res.getContent()
                robot.answer(content)

                recordText += content

            if len(recordText) == 0:
                robot("[bold red]出现错误了[/]")
                print("")
                continue

            cnt += 1
            contextManager.add(res.role, recordText)
            print("")
        except Exception as e:
            robot.print("出现了异常: " + str(e))
            # 清理出现异常的上下文
            contextManager.remove(cnt)

        cnt = 0


def initApiKey(overwrite=False):
    key = ""
    user_path = os.path.expanduser("~")
    config_path = Path(user_path).joinpath("api_key.ini")
    if not config_path.exists():
        with open(config_path, "w", encoding="utf8") as f:
            key = me.input("请输入open ai apikey: ")
            key = key.replace(" ", "")
            f.write(key)
            return key

    with open(config_path, "r", encoding="utf8") as f:
        key = f.readline()
        if overwrite or key is None or len(key) == 0:
            key = me.input("请输入open ai apikey: ")
            key = key.replace(" ", "")
            overwrite = True

    if overwrite and len(key) > 0:
        with open(config_path, "w+", encoding="utf8") as f:
            f.write(key)

    return key


def main():
    cli()


if __name__ == "__main__":
    main()
