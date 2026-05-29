#!/usr/bin/env python3

import time

from constants import *
from ui import banner
from system import clear

from configs.starship_config import starship_menu
from configs.zsh_config import zsh_menu
from configs.fastfetch_config import fastfetch_menu


PACKAGE_CONFIGS = {
    "1": ("Starship", starship_menu),
    "2": ("ZSH", zsh_menu),
    "3": ("Fastfetch", fastfetch_menu),
}


def pconfig_menu():
    while True:
        clear()

        banner("PACKAGE CONFIGURATION")

        for key, (label, _) in PACKAGE_CONFIGS.items():
            print(f"{key}. Configure {label}")

        print(f"\n{RED}0. Back{RESET}")

        choice = input("\nConfig >> ").strip()

        if choice == "0":
            break

        if choice not in PACKAGE_CONFIGS:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)
            continue

        _, action = PACKAGE_CONFIGS[choice]

        action()
