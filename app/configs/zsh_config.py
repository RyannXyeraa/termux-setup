#!/usr/bin/env python3

import os
import time
import subprocess

from constants import *
from ui import banner
from system import (
    clear,
    run,
    check_package
)


ZSH_THEMES = {
    "1": (
        "Robbyrussell",
        "robbyrussell",
        False
    ),

    "2": (
        "Agnoster",
        "agnoster",
        True
    ),

    "3": (
        "Bira",
        "bira",
        False
    ),

    "4": (
        "No Theme (Use Starship)",
        "",
        False
    )
}


STARSHIP_INIT = 'eval "$(starship init zsh)"'


def get_zshrc():
    return os.path.expanduser("~/.zshrc")


def ensure_zshrc():
    zshrc = get_zshrc()

    if not os.path.exists(zshrc):
        open(zshrc, "w").close()

    return zshrc


def read_zshrc():
    zshrc = ensure_zshrc()

    with open(zshrc, "r") as f:
        return f.readlines()


def write_zshrc(lines):
    zshrc = ensure_zshrc()

    with open(zshrc, "w") as f:
        f.writelines(lines)


def replace_theme(theme):
    lines = read_zshrc()

    updated = []
    found = False

    for line in lines:
        if line.startswith("ZSH_THEME="):
            updated.append(f'ZSH_THEME="{theme}"\n')
            found = True

        else:
            updated.append(line)

    if not found:
        updated.append(f'\nZSH_THEME="{theme}"\n')

    write_zshrc(updated)


def remove_starship():
    lines = read_zshrc()

    updated = []

    for line in lines:
        if STARSHIP_INIT in line:
            continue

        updated.append(line)

    write_zshrc(updated)


def enable_starship():
    lines = read_zshrc()

    for line in lines:
        if STARSHIP_INIT in line:
            return

    lines.append(f"\n{STARSHIP_INIT}\n")

    write_zshrc(lines)


def ensure_ohmyzsh_source():
    lines = read_zshrc()

    source_line = 'source $ZSH/oh-my-zsh.sh'

    for line in lines:
        if source_line in line:
            return

    lines.append(f"\n{source_line}\n")

    write_zshrc(lines)


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

    if result.returncode == 0:
        print(
            f"{GREEN}[SUCCESS] "
            f"Default shell changed to ZSH!{RESET}"
        )

        print(
            f"{CYAN}[INFO] "
            f"Restart Termux to apply changes.{RESET}"
        )

    else:
        print(
            f"{RED}[ERROR] "
            f"Failed to change shell!{RESET}"
        )

        if result.stderr:
            print(result.stderr)

    input("\nPress Enter to continue...")


def install_ohmyzsh():
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

    clear()

    banner("INSTALLING OH-MY-ZSH")

    print(
        f"{CYAN}[INFO] "
        f"Downloading installer...{RESET}\n"
    )

    result = subprocess.run(
        (
            "curl -fsSL "
            "https://raw.githubusercontent.com/"
            "ohmyzsh/ohmyzsh/master/tools/install.sh | sh"
        ),
        shell=True,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        ensure_ohmyzsh_source()

        print(
            f"\n{GREEN}[SUCCESS] "
            f"Oh-My-Zsh installed successfully!{RESET}"
        )

    else:
        print(
            f"\n{RED}[ERROR] "
            f"Failed to install Oh-My-Zsh!{RESET}"
        )

        if result.stderr:
            print()
            print(result.stderr)

    input("\nPress Enter to continue...")


def apply_theme(theme_name, theme_value):
    replace_theme(theme_value)

    if theme_value == "":
        enable_starship()

    else:
        remove_starship()

    print(
        f"{GREEN}[SUCCESS] "
        f"Applied theme: {theme_name}{RESET}"
    )

    print()

    if theme_value == "":
        print(
            f"{CYAN}[INFO] "
            f"Starship prompt enabled.{RESET}"
        )

    else:
        print(
            f"{YELLOW}[INFO] "
            f"Starship prompt disabled.{RESET}"
        )

    print(
        f"{CYAN}[INFO] "
        f"Restart shell to fully apply changes.{RESET}"
    )

    print(f"{GREEN}Run: exec zsh{RESET}")

    input("\nPress Enter to continue...")


def zsh_theme_menu():
    while True:
        clear()

        banner("ZSH THEMES")

        print(
            f"{CYAN}[INFO] "
            f"ZSH themes and Starship cannot{RESET}"
        )

        print(
            f"{CYAN}be used together simultaneously.{RESET}\n"
        )

        for key, (
            theme_name,
            _,
            requires_font
        ) in ZSH_THEMES.items():

            print(f"{key}. {theme_name}")

            if requires_font:
                print(
                    f"   {YELLOW}"
                    f"Requires Nerd Font"
                    f"{RESET}"
                )

        print(f"\n{RED}0. Back{RESET}")

        choice = input("\nTheme >> ").strip()

        if choice == "0":
            break

        if choice not in ZSH_THEMES:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)
            continue

        theme_name, theme_value, _ = (
            ZSH_THEMES[choice]
        )

        apply_theme(
            theme_name,
            theme_value
        )


def zsh_menu():
    while True:
        clear()

        banner("ZSH CONFIGURATION")

        installed = (
            f"{GREEN}[INSTALLED]{RESET}"
            if check_package("zsh")
            else
            f"{RED}[NOT INSTALLED]{RESET}"
        )

        print(f"Status : {installed}\n")

        print("1. Set ZSH as Default Shell")
        print("2. Install Oh-My-Zsh")
        print("3. ZSH Theme")

        print(f"\n{RED}0. Back{RESET}")

        choice = input("\nZSH >> ").strip()

        if choice == "0":
            break

        elif choice == "1":
            set_zsh_default()

        elif choice == "2":
            install_ohmyzsh()

        elif choice == "3":
            if not check_package("zsh"):
                print(
                    f"{RED}[ERROR] "
                    f"ZSH is not installed!{RESET}"
                )

                print(
                    f"{CYAN}[INFO] "
                    f"Install it from:{RESET}"
                )

                print(
                    f"{GREEN}"
                    f"Main Menu -> Install Packages"
                    f"{RESET}"
                )

                input("\nPress Enter to continue...")
                continue

            zsh_theme_menu()

        else:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)
