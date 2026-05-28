import sys

from constants import *
from ui import banner
from system import clear
from themes import theme_menu
from packages import package_menu
from pconfig import pconfig_menu

def main():
    while True:
        try:
            clear()

            banner("TERMUX CUSTOM SETUP")

            print("1. Customize Theme")
            print("2. Install Packages")
            print("3. Package Configuration")
            print(f"{RED}0. Exit{RESET}")

            choice = input("\n>> ").strip()

            if choice == "0":
                print(f"\n{GREEN}Goodbye!{RESET}")
                break

            elif choice == "1":
                theme_menu()

            elif choice == "2":
                package_menu()

            elif choice == "3":
                pconfig_menu()

            else:
                print(f"{RED}Invalid option!{RESET}")

        except (KeyboardInterrupt, EOFError):
            print(f"\n{GREEN}Exiting...{RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()
