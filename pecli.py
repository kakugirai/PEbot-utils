import sys
import datetime
import click
from getpass import getpass
import botcore


if sys.platform == "linux":
    from pyvirtualdisplay import Display
    # seamless executable on Ubuntu
    display = Display(visible=0, size=(800, 600))
    display.start()
elif sys.platform == "darwin":
    pass
elif sys.platform == "win32":
    raise "I don't give a shit to Windows system."


@click.group()
def cli():
    """Register PE class, in God mode."""
    pass

@cli.command()
@click.option('--classname', required=True,
              help="enter the name of the class")
def reserve(classname):
    """Reserve class"""
    PEbot = botcore.Bot()
    PEbot.set_up()
    username = input("CNS ID:")
    password = getpass("CNS Password: ")
    PEbot.login(username, password)
    PEbot.reserve_class(classname)
    PEbot.tear_down()

@cli.command()
def show():
    """Show available class"""
    PEbot = botcore.Bot()
    PEbot.set_up()
    PEbot.show_available_class()
    PEbot.tear_down()

