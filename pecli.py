"""PEbot command line interface"""

import sys
# import datetime
from getpass import getpass
from tabulate import tabulate
import click
import inquirer
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
# @click.option('--date', '-d', required=True,
#               help="the date of the class")
# @click.option('--period', '-p', required=True,
#               help="the period of the class")
# @click.option('--classname', '-n', required=True,
#               help="the name of the class")
def register():
    # date, period, classname
    """Register class"""
    bot = botcore.Bot()
    available_class = bot.show_available_class()
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    day = inquirer.prompt([inquirer.List('day',
        message='Please choose the day of the week',
        choices=days)])
    courses = [course for course in available_class if day["day"] in course[0]]
    courses_name = [(course[0][:5] + "\tPeriod " + course[1] + "\t" + course[2]) for course in courses]
    course = inquirer.prompt([inquirer.List('course',
        message='Please choose the class you want to register',
        choices=courses_name)])
    selected = course["course"].split("\t")
    comfirm = inquirer.prompt([inquirer.Confirm('continue', message=("You selected " + selected[2] + " at " + selected[1] + " on " + selected[0] + " " + day["day"] + ". Register it?"))])
    if comfirm:
        username = input("CNS ID: ")
        password = getpass("CNS Password: ")
        bot.login(username, password)
        bot.register_class((selected[0] + " (" + day["day"] + ")"), selected[1][-1], selected[2])
    bot.tear_down()

@cli.command()
@click.option('--date', '-d', required=True,
              help="the date of the class")
@click.option('--period', '-p', required=True,
              help="the period of the class")
@click.option('--classname', '-n', required=True,
              help="the name of the class")
def cancel(date, period, classname):
    """Cancel class"""
    username = input("CNS ID:")
    password = getpass("CNS Password: ")
    bot = botcore.Bot()
    bot.login(username, password)
    bot.cancel_class(date, period, classname)
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
        print(tabulate(bot.show_available_class(), headers=[
            'Date', 'Period', 'Class Name', 'Teacher', 'Available']))
    else:
        username = input("CNS ID:")
        password = getpass("CNS Password: ")
        bot.login(username, password)
        print(tabulate(bot.show_registered_class(), headers=[
            'Date', 'Period', 'Class Name', 'Teacher']))
    bot.tear_down()
