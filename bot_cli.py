import sys
import argparse
import getpass
import bot


if sys.platform == "linux":
    from pyvirtualdisplay import Display
    # seamless executable on Ubuntu
    display = Display(visible=0, size=(800, 600))
    display.start()
elif sys.platform == "darwin":
    pass
elif sys.platform == "win32":
    raise "I don't give a shit to Windows system."

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--available", dest="available",
                    action='store_true',
                    help="show available class")
parser.add_argument("-r", "--reserve", dest="classname",
                    help="enter name of desired class")
options = parser.parse_args()

PEbot = bot.Bot()
if options.classname:
    username = input("CNS ID: ")
    password = getpass.getpass("CNS Password: ")
    print(PEbot.login(username, password))
    print(PEbot.reserve_class(options.classname))

if options.available:
    username = input("CNS ID: ")
    password = getpass.getpass("CNS Password: ")
    print(PEbot.login(username, password))
    print(PEbot.show_available_class())

