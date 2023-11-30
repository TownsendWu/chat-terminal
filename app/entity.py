from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.live import Live

import sys

import time


console = Console()


class Common:
    def __init__(self) -> None:
        pass

    def welcome(self):
        welcome = """
# Chat Terminal

> ***Chat Terminal*** **是一个在 terminal 中使用的 chatgpt 支持 markdown 显示 和上下文记录**

可选，启动时加上额外参数可显示emoji：
```shell
chat-terminal emoji
🧛 : 你是谁
🤖 : 我是一个在terminal中的对话机器人。
```
- 输入 **quit** 退出
- 输入 **clear** 清屏
- 输入 **context** 查看上下文
- 输入 **reset** 重置api key
"""
        markdown = Markdown(welcome)
        console.print(markdown)
        console.rule("[bold red]")

    def context(self, messages):
        table = Table()
        table.add_column("Role")
        table.add_column("content")
        with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
            for row in messages:
                time.sleep(0.2)
                table.add_row(f"[red]{row['role']}", f"{row['content']}")

    def clear(self):
        console.clear()

    def console(self):
        return console
        

class Person:
    def __init__(self):
        self.icon = "[bold magenta]Me[/bold magenta]: "
        if len(sys.argv) >=2:
            param = sys.argv[1]
            if param == "emoji":
                self.icon = ":vampire: : "

    def input(self, text=""):
        tip = self.icon
        if len(text) > 0:
            tip = f"{self.icon}{text}"

        question = console.input(tip)
        return question

    def print(self, text=""):
        console.print(self.icon + text)


class Robot:
    def __init__(self):
        self.icon = "[bold yellow]Robot[/bold yellow]: "
        if len(sys.argv) >=2:
            param = sys.argv[1]
            if param == "emoji":
                self.icon = ":robot: : "

    def answer(self, text):
        content = text
        console.print(content, end="")

    def print(self, text="", end="\n"):
        console.print(self.icon + text, end=end)
