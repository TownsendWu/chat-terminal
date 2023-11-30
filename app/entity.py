from rich.console import Console
from rich.markdown import Markdown

console = Console()


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
        content = Markdown(text)
        console.print("",content, end="")

    def print(self, text="", end="\n"):
        console.print(self.icon + text, end=end)
