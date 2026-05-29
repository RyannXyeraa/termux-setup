#!/usr/bin/env python3

import time

from constants import *
from ui import banner
from system import clear, run
from shell import enable_starship
from network import check_internet


selected_packages = set()


def install_packages(packages):
    clear()

    banner("INSTALLATION PROCESS")

    if not check_internet():
        print(f"{RED}[ERROR] No internet connection!{RESET}")
        input("\nPress Enter to continue...")
        return

    print(
        f"{CYAN}[INFO] Installing:{RESET} "
        f"{', '.join(packages)}\n"
    )

    command = [
        "pkg",
        "install",
        "-y",
        *packages
    ]

    result = run(
        command,
        silent=True
    )

    if result.returncode == 0:
        print(
            f"{GREEN}[SUCCESS] "
            f"Packages installed successfully!{RESET}"
        )

        if "starship" in packages:
            print()
            enable_starship()

    else:
        print(f"{RED}[ERROR] Installation failed!{RESET}")

        if result.stderr:
            print(f"\n{YELLOW}Reason:{RESET}")
            print(result.stderr)

    input("\nPress Enter to continue...")


def package_menu():
    while True:
        clear()

        banner("PACKAGE INSTALLER")

        for key, (label, pkg) in PACKAGES.items():
            status = (
                f"{GREEN}[X]{RESET}"
                if pkg in selected_packages
                else "[ ]"
            )

            print(f"{key}. {status} {label}")

        print(f"\n{GREEN}i. Install Selected{RESET}")
        print(f"{RED}0. Back{RESET}")

        choice = input("\nSelect >> ").strip().lower()

        if choice == "0":
            break

        if choice == "i":
            if not selected_packages:
                print(
                    f"{RED}[ERROR] "
                    f"No package selected!{RESET}"
                )

                time.sleep(1.5)
                continue

            install_packages(selected_packages)
            break

        if choice not in PACKAGES:
            print(f"{RED}[ERROR] Invalid option!{RESET}")
            time.sleep(1)
            continue

        _, package_name = PACKAGES[choice]

        if package_name in selected_packages:
            selected_packages.remove(package_name)

        else:
            for group in EXCLUSIVE_GROUPS:
                if package_name in group:

                    for other_pkg in group:
                        if other_pkg != package_name:
                            selected_packages.discard(other_pkg)

            selected_packages.add(package_name)
