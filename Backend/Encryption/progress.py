import math
import colorama,sys
from matplotlib.colorbar import Colorbar

def progress_bar(progress, color = colorama.Fore.YELLOW):
    percent = 100*(progress/float(100))
    if progress == 0:
        color = colorama.Fore.RED
    bar = '▌' * int(percent) + '-' * (100 - int(percent))
    print(color + f"\r |{bar}| {percent:.2f}%",end = "")
  
    if progress == 100:
        print(colorama.Fore.GREEN + f"\r |{bar}| {percent:.2f}%",end = "")
        print(colorama.Fore.RESET)
def remove_progress_bar():
    print("")
    print(colorama.Fore.RESET)
    return
