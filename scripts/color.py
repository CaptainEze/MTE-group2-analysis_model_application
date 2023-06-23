import os
import time
import scripts.cprint as cp
try:
    from colorama import Style,Fore
except ModuleNotFoundError:
    cp.cprint("Unfortunately you need colorama...")
    time.sleep(1)
    cp.cprint("Dont worry I got it sorted out")
    time.sleep(.3)
    cp.cprint("Attempting to install colorama...")
    time.sleep(.5)
    cp.cprint("Please connect to the internet")
    os.system("pip install colorama")


c_r = Style.BRIGHT+Fore.RED
c_g = Style.BRIGHT+Fore.GREEN
c_b = Style.BRIGHT+Fore.BLUE
c_y = Style.BRIGHT+Fore.YELLOW
c_w = Style.RESET_ALL+Fore.RESET