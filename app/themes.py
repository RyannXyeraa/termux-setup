import os
import shutil

from constants import *
from ui import banner
from system import clear, run

TERMUX_DIR = os.path.expanduser("~/.termux")
COLORS_FILE = os.path.join(TERMUX_DIR, "colors.properties")
BACKUP_FILE = os.path.join(TERMUX_DIR, "colors.properties.bac")

def apply_theme(name, theme_path):
    if not os.path.exists(theme_path):
        print(f"{RED}[ERROR] Theme not found!{RESET}")
        input("\nPress Enter...")
        return

    os.makedirs(TERMUX_DIR, exist_ok=True)

    if os.path.exists(COLORS_FILE):
        shutil.copy(COLORS_FILE, BACKUP_FILE)

    shutil.copy(theme_path, COLORS_FILE)

    print(f"{GREEN}[SUCCESS] {name} applied!{RESET}")

    reload_choice = input("Reload Termux now? [Y/n] ").strip().lower()

    if reload_choice in ["", "y"]:
        run("termux-reload-settings")

    input("\nPress Enter to continue...")

def theme_menu():
    while True:
        clear()
        banner("COLOR THEME MENU")

        for key, (name, _) in THEMES.items():
            print(f"{key}. {name}")

        print(f"\n{RED}0. Back{RESET}")

        choice = input("\nTheme >> ").strip()

        if choice == "0":
            break

        if choice not in THEMES:
            print(f"{RED}Invalid option!{RESET}")
            continue

        name, path = THEMES[choice]
        apply_theme(name, path)
