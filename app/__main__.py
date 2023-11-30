import time


from entity import Person,Robot


text = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""
me = Person()
robot = Robot()

def cli():
    while True:
        question = me.ask()

        if question == "quit":
            robot.print("bye ~")
            break
        
        robot.print(end="")
        
        for i in range(len(text)):
            time.sleep(0.1)
            robot.answer(text[i])
        print("")


def main():
    cli()


if __name__ == "__main__":
    main()
