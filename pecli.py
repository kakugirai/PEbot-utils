"""PEbot command line interface"""

import sys
# import datetime
from getpass import getpass
import click
import botcore


if sys.platform == "linux" or sys.platform == "linux2":
    from pyvirtualdisplay import Display
    # seamless executable on Ubuntu
    DISPLAY = Display(visible=0, size=(800, 600))
    DISPLAY.start()
elif sys.platform == "darwin":
    pass
elif sys.platform == "win32":
    raise "I don't give a shit to Windows system."


@click.group()
def cli():
    """Register PE class, in God mode."""
    pass

@cli.command()
@click.option('--date', required=True,
              help="enter the date of the class")
@click.option('--period', required=True,
              help="enter the period of the class")
@click.option('--classname', required=True,
              help="enter the name of the class")
def reserve(date, period, classname):
    """Reserve class"""
    username = input("CNS ID:")
    password = getpass("CNS Password: ")
    bot = botcore.Bot()
    bot.login(username, password)
    bot.reserve_class(date, period, classname)
    bot.tear_down()

@cli.command()
def show():
    """Show available class"""
    bot = botcore.Bot()
    bot.show_available_class()
    bot.tear_down()
