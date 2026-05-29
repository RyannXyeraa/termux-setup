#!/usr/bin/env python3

import time

from constants import *
from ui import banner
from system import (
    clear,
    check_package
)

from configs.starship_config import starship_menu
from configs.zsh_config import zsh_menu
from configs.fastfetch_config import fastfetch_menu


PACKAGE_CONFIGS = {
    "1": ("Starship", "starship", starship_menu),
    "2": ("ZSH", "zsh", zsh_menu),
    "3": ("Fastfetch", "fastfetch", fastfetch_menu),
}


def get_status(package):
    if check_package(package):
        return f"{GREEN}[INSTALLED]{RESET}"

    return f"{RED}[NOT INSTALLED]{RESET}"


def pconfig_menu():
    while True:
        clear()

        banner("PACKAGE CONFIGURATION")

        for key, (
            label,
            package_name,
            _
        ) in PACKAGE_CONFIGS.items():

            status = get_status(package_name)

            print(
                f"{key}. "
                f"{label} "
                f"{status}"
            )

        print(f"\n{RED}0. Back{RESET}")

        choice = input("\nConfig >> ").strip()

        if choice == "0":
            break

        if choice not in PACKAGE_CONFIGS:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)
            continue

        label, package_name, action = (
            PACKAGE_CONFIGS[choice]
        )

        if not check_package(package_name):
            print(
                f"{RED}[ERROR] "
                f"{label} is not installed!{RESET}"
            )

            print(
                f"{CYAN}[INFO] "
                f"Install it from:{RESET}"
            )

            print(
                f"{GREEN}Main Menu -> Install Packages{RESET}"
            )

            input("\nPress Enter to continue...")
            continue

        action()
