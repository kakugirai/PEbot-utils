"""PEbot command line interface"""

import sys
# import datetime
from getpass import getpass
from tabulate import tabulate
import click
import botcore


if sys.platform == "linux" or sys.platform == "linux2":
    from pyvirtualdisplay import Display
    # headless executable on Ubuntu
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
@click.option('--date', '-d', required=True,
              help="the date of the class")
@click.option('--period', '-p', required=True,
              help="the period of the class")
@click.option('--classname', '-c', required=True,
              help="the name of the class")
def register(date, period, classname):
    """Register class"""
    username = input("CNS ID:")
    password = getpass("CNS Password: ")
    bot = botcore.Bot()
    bot.login(username, password)
    bot.register_class(date, period, classname)
    bot.tear_down()

@cli.command()
@click.option('--all', '-a', is_flag=True,
              help="show all available classes")
@click.option('--registered', '-r', is_flag=True,
              help="show registered classes(login required)")
def show(all, registered):
    """Show available classes"""
    bot = botcore.Bot()
    if all:
        print(tabulate(bot.show_available_class(), headers=['Date', 'Period', 'Class Name', 'Teacher', 'Available']))
    if registered:
        username = input("CNS ID:")
        password = getpass("CNS Password: ")
        bot.login(username, password)
        print(tabulate(bot.show_registered_class(), headers=['Date', 'Period', 'Class Name', 'Teacher']))
    bot.tear_down()
