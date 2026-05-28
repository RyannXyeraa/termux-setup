#!/usr/bin/env python3

import os
import shutil
import time

from constants import *
from ui import banner
from system import clear, run
from shell import enable_starship


STARSHIP_THEMES = {
    "1": (
        "Catppuccin Mocha",
        "assets/starship/catppuccin-mocha.toml"
    ),

    "2": (
        "Dracula",
        "assets/starship/dracula.toml"
    ),

    "3": (
        "Nord",
        "assets/starship/nord.toml"
    )
}


STARSHIP_ACTIONS = {
    "1": "Apply Theme",
    "2": "Enable Starship",
    "3": "Preview Prompt",
}


def get_starship_config_path():
    config_dir = os.path.expanduser("~/.config")

    os.makedirs(config_dir, exist_ok=True)

    return os.path.join(config_dir, "starship.toml")



def apply_starship_theme(theme_name, theme_file):
    config_path = get_starship_config_path()

    if not os.path.exists(theme_file):
        print(f"{RED}[ERROR] Theme file not found!{RESET}")
        input("\nPress Enter to continue...")
        return

    shutil.copy(theme_file, config_path)

    print(f"{GREEN}[SUCCESS] Applied {theme_name} theme!{RESET}")

    enable_starship()

    input("\nPress Enter to continue...")



def theme_menu():
    while True:
        clear()

        banner("STARSHIP THEMES")

        for key, (name, _) in STARSHIP_THEMES.items():
            print(f"{key}. {name}")

        print(f"\n{RED}0. Back{RESET}")

        choice = input("\nTheme >> ").strip()

        if choice == "0":
            break

        if choice not in STARSHIP_THEMES:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)
            continue

        theme_name, theme_path = STARSHIP_THEMES[choice]

        apply_starship_theme(theme_name, theme_path)



def preview_starship():
    clear()

    banner("STARSHIP PREVIEW")

    print(f"{CYAN}[INFO] Launching temporary shell preview...{RESET}\n")

    run("starship print-config")

    input("\nPress Enter to continue...")



def starship_menu():
    while True:
        clear()

        banner("STARSHIP CONFIGURATION")

        for key, label in STARSHIP_ACTIONS.items():
            print(f"{key}. {label}")

        print(f"\n{RED}0. Back{RESET}")

        choice = input("\nStarship >> ").strip()

        if choice == "0":
            break

        if choice == "1":
            theme_menu()

        elif choice == "2":
            enable_starship()
            input("\nPress Enter to continue...")

        elif choice == "3":
            preview_starship()

        else:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)
