#!/usr/bin/env python3

import os
import time

from constants import *
from ui import banner
from system import clear, run



def generate_fastfetch_config():
    config_dir = os.path.expanduser("~/.config/fastfetch")

    os.makedirs(config_dir, exist_ok=True)

    result = run("fastfetch --gen-config", silent=True)

    if result.returncode == 0:
        print(f"{GREEN}[SUCCESS] Fastfetch config generated!{RESET}")
    else:
        print(f"{RED}[ERROR] Failed to generate config!{RESET}")

    input("\nPress Enter to continue...")



def fastfetch_menu():
    while True:
        clear()

        banner("FASTFETCH CONFIGURATION")

        print("1. Generate Config")

        print(f"\n{RED}0. Back{RESET}")

        choice = input("\nFastfetch >> ").strip()

        if choice == "0":
            break

        elif choice == "1":
            generate_fastfetch_config()

        else:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)
