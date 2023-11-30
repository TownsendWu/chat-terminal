from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.live import Live

import time


console = Console()

class Common:
    def __init__(self) -> None:
        pass
    
    def welcome(self):
        with open("./README.md","r",encoding="utf8") as f:
            txt = f.read()
            markdown = Markdown(txt)
            console.print(markdown)
            console.rule("[bold red]开始使用吧")


    def context(self,messages):
        table = Table()
        table.add_column("Role")
        table.add_column("content")
        with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
            for row in messages:
                time.sleep(0.1)
                table.add_row(f"[red]{row['role']}", f"{row['content']}")

    def clear(self):
        console.clear()

        

class Person:
    def __init__(self):
        self.icon = ":vampire: : "
        self.questions = []

    def ask(self):
        question = console.input(self.icon)
        self.questions.append(question)
        return question

    def print(self, text=""):
        console.print(self.icon + text)


class Robot:
    def __init__(self):
        self.icon = ":robot: : "

    def answer(self, text):
        content = text
        console.print(content, end="")



    def print(self, text="", end="\n"):
        console.print(self.icon + text, end=end)
