import sys
import time

from rich.live import Live
from rich.markdown import Markdown



text = "There is a screencast available which shows the basic API of Click and how to build simple applications with it. It also explores how to build commands with subcommands."

def cli():
    markdown = Markdown("# test")
    with Live(refresh_per_second=4) as live:  # update 4 times a second to feel fluid
        for i in  range(len(text)):
            time.sleep(0.1)
            live.console.out(text[i])
            live.console.clear(home=False)


def main():
    cli()


if __name__ == "__main__":
    main()