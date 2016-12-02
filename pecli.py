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
    pass

@cli.command()
@click.option('--classname', required=True)
def reserve(classname):
    PEbot = botcore.Bot()
    PEbot.set_up()
    username = input("CNS ID:")
    password = getpass("CNS Password: ")
    print(PEbot.login(username, password))
    print(PEbot.reserve_class(classname))
    PEbot.tear_down()

@cli.command()
def show():
    PEbot = botcore.Bot()
    PEbot.set_up()
    print(PEbot.show_available_class())
    PEbot.tear_down()
