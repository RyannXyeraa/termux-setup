#!/usr/bin/env python3

import os
import subprocess
import time

from constants import *
from ui import banner
from system import clear


TERMUX_DIR = os.path.expanduser("~/.termux")


FONTS = {
    "1": (
        "JetBrains Mono Nerd Font",
        "assets/fonts/jetbrains-mono.ttf"
    ),

    "2": (
        "Fira Code Nerd Font",
        "assets/fonts/fira-code.ttf"
    ),

    "3": (
        "Hack Nerd Font",
        "assets/fonts/hack.ttf"
    ),

    "4": (
        "SauceCodePro Nerd Font",
        "assets/fonts/sauce-code-pro.ttf"
    ),

    "5": (
        "Ubuntu Mono Nerd Font",
        "assets/fonts/ubuntu-mono.ttf"
    )
}


def apply_font(font_name, font_file):
    if not os.path.exists(font_file):
        print(f"{RED}[ERROR] Font file not found!{RESET}")
        input("\nPress Enter to continue...")
        return

    os.makedirs(TERMUX_DIR, exist_ok=True)

    target = os.path.join(TERMUX_DIR, "font.ttf")
    backup = f"{target}.bac"

    # Backup existing font
    if os.path.exists(target):
        subprocess.run([
            "mv",
            target,
            backup
        ])

    # Copy new font
    result = subprocess.run(
        [
            "cp",
            font_file,
            target
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"{RED}[ERROR] Failed to apply font!{RESET}")

        if result.stderr:
            print(result.stderr)

        input("\nPress Enter to continue...")
        return

    print(f"{GREEN}[SUCCESS] Applied {font_name}!{RESET}")

    print(f"{CYAN}[INFO] Reload Termux settings:{RESET}")
    print(f"{YELLOW}termux-reload-settings{RESET}")

    input("\nPress Enter to continue...")


def font_menu():
    while True:
        clear()

        banner("CUSTOM FONT")

        for key, (font_name, _) in FONTS.items():
            print(f"{key}. {font_name}")

        print(f"\n{RED}0. Back{RESET}")

        choice = input("\nFont >> ").strip()

        if choice == "0":
            break

        if choice not in FONTS:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)
            continue

        font_name, font_path = FONTS[choice]

        apply_font(font_name, font_path)
