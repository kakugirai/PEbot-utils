import sys
import argparse
import bot

if sys.platform == "linux" or sys.platform == "linux2":
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(800, 600))
    display.start()
elif sys.platform == "darwin":
    pass
elif sys.platform == "win32":
    raise "I don't give a shit to Windows system."

##
# TODO: add multi-users support
##

#  class UserAction(argparse.Action):
#      def __call__(self, parser, namespace, values, option_string=None):
#          if len(namespace.password) < len(namespace.username):
#              parser.error('Missing password')
#          else:
#              namespace.username.append(values)
#
#
#  class PasswordAction(argparse.Action):
#      def __call__(self, parser, namespace, values, option_string=None):
#          if len(namespace.username) <= len(namespace.password):
#              parser.error('Missing user')
#          else:
#              namespace.password.append(values)

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', dest='username', required=True,
                    help="CNS username")
parser.add_argument('-p', '--password', dest='password', required=True,
                    help="CNS password")
parser.add_argument("-a", "--available",
                    help="show available class")
parser.add_argument("-r", "--reserve", dest="classname",
                    help="enter name of desired class")
options = parser.parse_args()

PEbot = bot.Bot()
if options.classname:
    print(PEbot.login(options.username, options.password))
    print(PEbot.reserve_class(options.classname))
