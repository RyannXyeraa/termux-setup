#!/usr/bin/env python3

import time

from constants import *
from ui import banner
from system import clear, run



def zsh_menu():
    while True:
        clear()

        banner("ZSH CONFIGURATION")

        print("1. Set ZSH as Default Shell")
        print("2. Install Oh-My-Zsh")

        print(f"\n{RED}0. Back{RESET}")

        choice = input("\nZSH >> ").strip()

        if choice == "0":
            break

        elif choice == "1":
            result = run("chsh -s zsh", silent=True)

            if result.returncode == 0:
                print(f"{GREEN}[SUCCESS] Default shell changed to ZSH!{RESET}")
            else:
                print(f"{RED}[ERROR] Failed to change shell!{RESET}")

            input("\nPress Enter to continue...")

        elif choice == "2":
            run(
                'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
            )

            input("\nPress Enter to continue...")

        else:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)
