from datetime import datetime
import time
import colorama
from colorama import Fore,Style


def print_error_message(msg,msg_type,delay):
    colorama.init(autoreset = True)
    current_datetime = str(datetime.now())
    print(f'[{Fore.RED}{msg_type}{Fore.RESET}] {Fore.RED}{current_datetime} {Fore.RED}{Style.BRIGHT}{msg}')
    time.sleep(delay)
    return

