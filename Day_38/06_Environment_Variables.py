# work of [(os.environ.get("USERNAME")) - {gives username of windows environment path},
# (os.environ.get("OS")) - {gives operating system name},
# (os.environ.get("PATH")) - {gives windows envir. whole path},
# (os.environ.get("USERPROFILE")) - {gives home/(windows envir.) directory name only}] function in os module.

#  Rem! = the thing inside these function brackets shoukd in capital letters.
# its useful to get details and more of windows envir. directory in REAL Projects

import os

print("Username:", os.environ.get(""))
print("Operating System:", os.environ.get("OS"))
print("Path:", os.environ.get("PATH"))

home = os.environ.get("USERNAME")

print("Home Directory:", home)