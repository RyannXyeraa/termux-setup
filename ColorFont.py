#!/usr/bin/env python3
import os
import subprocess
import shutil

# Menggunakan os.path.expanduser("~") agar Python paham direktori Home Termux
TERMUX_DIR = os.path.expanduser("~/.termux")
PATH = os.path.join(TERMUX_DIR, "colors.properties")
BAC = os.path.join(TERMUX_DIR, "colors.properties.bac")

# Warna ANSI untuk tampilan CLI profesional
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

def setColorFont():
    while True:
        try:
            subprocess.run(["clear"])
            print(f"{CYAN}=============================================={RESET}")
            print(f"{CYAN}            COLOR & FONT SELECTION            {RESET}")
            print(f"{CYAN}=============================================={RESET}")
            print("1. Catppuccin Mocha")
            print("2. Dracula")
            print("3. Nord (Coming Soon)")
            print(f"{RED}0. Back to Main Menu{RESET}")
            print(f"{CYAN}----------------------------------------------{RESET}")

            c = input("Color&Font >> ").strip()
            
            if not c:
                continue
            if c == "0":
                break
            if c < "0" or c > "3":
                print(f"{RED}Invalid selection!{RESET}")
                import time; time.sleep(1)
                continue

            if c == "1":
                theme_file = "themes/catppuccin-mocha.properties"
                
                if not os.path.exists(theme_file):
                    print(f"{RED}[ERROR] Theme file '{theme_file}' not found!{RESET}")
                    input("\nPress Enter to continue...")
                    continue

                # Pastikan folder ~/.termux/ ada sebelum dipakai
                if not os.path.exists(TERMUX_DIR):
                    os.makedirs(TERMUX_DIR)

                # Backup file lama jika ada
                if os.path.exists(PATH):
                    shutil.copy(PATH, BAC)

                # Salin isi tema ke colors.properties
                try:
                    shutil.copy(theme_file, PATH)
                    print(f"{YELLOW}Applied Catppuccin Mocha theme..{RESET}")
                    i = input("Do you want to reload now? [Y/n] ") 
                    if i == "Y" or i == "y" or not i:
                        subprocess.run(["termux-reload-settings"])
                    elif i == "N" or i == "n":
                        break
                    print(f"{GREEN}[SUCCESS] Successful apply theme!{RESET}")
                except Exception as e:
                    print(f"{RED}[ERROR] Failed to apply theme: {e}{RESET}")
                
                input("\nPress Enter to return...")
                break

            elif c == "2":
                theme_file = "themes/dracula.properties"

                if not os.path.exists(theme_file):
                    print(f"{RED}[ERROR] Theme file '{theme_file}' not found!{RESET}")
                    input("\nPress Enter to continue...")
                    continue

                # Pastikan folder ~/.termux/ ada sebelum dipakai
                if not os.path.exists(TERMUX_DIR):
                    os.makedirs(TERMUX_DIR)

                # Backup file lama jika ada
                if os.path.exists(PATH):
                    shutil.copy(PATH, BAC)

                # Salin isi tema ke colors.properties
                try:
                    shutil.copy(theme_file, PATH)
                    print(f"{YELLOW}Applied Dracula theme..{RESET}")
                    i = input("Do you want to reload now? [Y/n] ")
                    if i == "Y" or i == "y" or not i:
                        subprocess.run(["termux-reload-settings"])
                    elif i == "N" or i == "n":
                        break
                    print(f"{GREEN}[SUCCESS] Successful apply theme!{RESET}")
                except Exception as e:
                    print(f"{RED}[ERROR] Failed to apply theme: {e}{RESET}")

                input("\nPress Enter to return...")
                break

        except (KeyboardInterrupt, EOFError):
            print(f"\n{YELLOW}Returning to main menu...{RESET}")
            break
