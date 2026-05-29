#!/usr/bin/env python3

import os
import time

from constants import *
from ui import banner
from system import clear, run


def generate_fastfetch_config(force=False):
    if force:
        command = [
            "fastfetch",
            "--gen-config-force"
        ]

    else:
        command = [
            "fastfetch",
            "--gen-config"
        ]

    result = run(
        command,
        silent=True
    )

    if result.returncode == 0:
        print(
            f"{GREEN}[SUCCESS] "
            f"Fastfetch config generated!{RESET}"
        )

    else:
        print(
            f"{RED}[ERROR] "
            f"Failed to generate config!{RESET}"
        )

        if result.stderr:
            print(result.stderr)

    input("\nPress Enter to continue...")


def overwrite_prompt():
    while True:
        clear()

        banner("FASTFETCH CONFIGURATION")

        print(
            f"{YELLOW}[INFO] "
            f"Config file already exists!{RESET}"
        )

        print("\n1. Overwrite Config")
        print("2. Cancel")

        choice = input("\n>> ").strip()

        if choice == "1":
            generate_fastfetch_config(force=True)
            break

        elif choice == "2":
            break

        else:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)


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
            config_dir = os.path.expanduser(
                "~/.config/fastfetch"
            )

            os.makedirs(
                config_dir,
                exist_ok=True
            )

            config_file = os.path.join(
                config_dir,
                "config.jsonc"
            )

            if os.path.exists(config_file):
                overwrite_prompt()

            else:
                generate_fastfetch_config()

        else:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)
