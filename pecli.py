"""pecli command line interface"""

import sys
# import datetime
from getpass import getpass
from tabulate import tabulate
import click
import inquirer

import botcore


if sys.platform == "linux" or sys.platform == "linux2":
    # headless executable on Ubuntu
    from pyvirtualdisplay import Display
    DISPLAY = Display(visible=0, size=(800, 600))
    DISPLAY.start()
elif sys.platform == "darwin":
    pass
elif sys.platform == "win32":
    raise "I don't give a shit to Windows system."


@click.group()
def cli():
    """pecli command line interface"""
    pass

@cli.command()
def register():
    """Register class"""
    bot = botcore.Bot()
    # Get all available classes
    available_class = bot.show_available_class()
    # Ask user the day they want to register PE class
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day = inquirer.prompt([inquirer.List('day',
        message='Please choose the day of the week',
        choices=days)])
    # Get all available classes on that day
    courses = [course for course in available_class if day["day"] in course[0]]
    if courses == []:
        bot.tear_down()
        print("Oops. It seems there's no PE class on that day.")
        sys.exit()
    # Format classes info
    courses_name = [(course[0][:5] + "\tperiod "
        + course[1] + "\t" + course[2]) for course in courses]
    class_to_select = inquirer.prompt([inquirer.List('class',
        message='Please choose the class you want to register',
        choices=courses_name)])
    # Format the selected class
    selected = class_to_select["class"].split("\t")
    confirm = inquirer.prompt([inquirer.Confirm('continue',
        message=("You selected " + selected[2] + " on " + selected[0]
                 + " " + day["day"] + " " + selected[1] + ". Register it?"))])
    if confirm["continue"]:
        username = input("CNS ID: ")
        password = getpass("CNS Password: ")
        bot.login(username, password)
        bot.register_class((selected[0] + " (" + day["day"] + ")"),
            selected[1][-1], selected[2])
        bot.tear_down()
    elif not confirm["continue"]:
        bot.tear_down()
        sys.exit()

@cli.command()
def cancel():
    """Cancel class"""
    username = input("CNS ID: ")
    password = getpass("CNS Password: ")
    bot = botcore.Bot()
    bot.login(username, password)
    registered_class = bot.show_registered_class()
    courses_name = [(course[0] + "\tperiod " + course[1] 
        + "\t" + course[2]) for course in registered_class]
    course_to_cancel = inquirer.prompt([inquirer.List('course',
        message='Please choose the class you want to cancel',
        choices=courses_name)])
    selected = course_to_cancel["course"].split("\t")
    comfirm = inquirer.prompt([inquirer.Confirm('continue',
        message=("You selected " + selected[2] 
            + " on " + selected[0] + " " + selected[1] + ". Cancel it?"))])
    if comfirm["continue"]:
        bot.cancel_class(selected[0], selected[1][-1], selected[2])
        bot.tear_down()
    elif not comfirm["continue"]:
        bot.tear_down()
        sys.exit()

@cli.command()
@click.option('--available', '-a', is_flag=True,
              help="show all available classes")
@click.option('--registered', '-r', is_flag=True,
              help="show registered classes(login required)")
def show(available, registered):
    """Show available classes"""
    bot = botcore.Bot()
    if available:
        print(tabulate(bot.show_available_class(),
            headers=['Date', 'Period', 'Class Name', 'Teacher', 'Available']))
    else:
        username = input("CNS ID: ")
        password = getpass("CNS Password: ")
        bot.login(username, password)
        print(tabulate(bot.show_registered_class(),
            headers=['Date', 'Period', 'Class Name', 'Teacher']))
    bot.tear_down()
