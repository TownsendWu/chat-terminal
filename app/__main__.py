import time
from entity import Person, Robot, Common
from openai import ChaGPT, Response
from context import ContextManager

common = Common()
me = Person()
robot = Robot()
contextManager = ContextManager()
chatGpt = ChaGPT("sk-HNEndMOWrHGpnrYS405093141b294b5aB3Ea646dC992C4D6")


def cli():
    common.welcome()
    while True:
        input = me.ask()

        if input == "quit":
            robot.print("bye ~")
            break

        if input == "clear":
            common.clear()
            continue
        
        if input == "context":
            common.context(contextManager.get())
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


def main():
    cli()


if __name__ == "__main__":
    main()
