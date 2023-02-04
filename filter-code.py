from colorama import Fore, Back
import os
from time import sleep

os.system("pip install colorama")
os.system("clear")
sleep(1.5)
print(Fore.RED, "welcome!")
sleep(2.0)

cb= (Fore.CYAN,""
"            _                 _                 ",
"  ___ _   _| |__   ___ _ __  | |__   ___  _   _ ",
" / __| | | | '_ \ / _ \ '__| | '_ \ / _ \| | | |",
"| (__| |_| | |_) |  __/ |    | |_) | (_) | |_| |",
" \___|\__, |_.__/ \___|_|    |_.__/ \___/ \__, |",
"      |___/                               |___/")
for cb in cb:
 print (cb)
 sleep(0.1)
print ()
print (Fore.RED, Back.BLACK, "")
print ("install tor...")
sleep(1)
os.system("pkg install tor")
sleep(1)
print (Fore.RED, Back.BLACK, "")
print (Fore.RED, Back.BLACK, "filtering code...")
print (Fore.RED, Back.BLACK, "")
sleep(1)
os.system("python filtering.py")
sleep(1)
print (Fore.RED, Back.BLACK, "")
print (Fore.RED, Back.BLACK, "filtering2 code...")
print (Fore.RED, Back.BLACK, "")
sleep(1)
os.system("python filtering2.py")
sleep(1)
print (Fore.RED, Back.BLACK, "")
print ("report code...")
print (Fore.RED, Back.BLACK, "")
sleep(1)
os.system(" python report.py")
sleep(1)
print (Fore.RED, Back.BLACK, "")
print ("tor...")
print (Fore.RED, Back.BLACK, "")
os.system("tor")

