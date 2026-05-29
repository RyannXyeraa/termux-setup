#!/usr/bin/env python3

import time, subprocess

from constants import *
from ui import banner
from system import (
    clear,
    run,
    check_package
)


def set_zsh_default():
    if not check_package("zsh"):
        print(f"{RED}[ERROR] ZSH is not installed!{RESET}")

        print(
            f"{CYAN}[INFO] "
            f"Install it from:{RESET}"
        )

        print(
            f"{GREEN}Main Menu -> Install Packages{RESET}"
        )

        input("\nPress Enter to continue...")
        return

    result = run(
        [
            "chsh",
            "-s",
            "zsh"
        ],
        silent=True
    )


def install_ohmyzsh():
    if not check_package("zsh"):
        print(f"{RED}[ERROR] ZSH is not installed!{RESET}")

    result = subprocess.run(
        "curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | sh",
        shell=True,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(
            f"{GREEN}[SUCCESS] "
            f"Oh-My-Zsh installed successfully!{RESET}"
        )

    else:
        print(
            f"{RED}[ERROR] "
            f"Failed to install Oh-My-Zsh!{RESET}"
        )

    input("\nPress Enter to continue...")


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
            set_zsh_default()

        elif choice == "2":
            install_ohmyzsh()

        else:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)
