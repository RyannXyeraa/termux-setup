#!/usr/bin/env python3                                                                               
import os
import subprocess
import sys
from ColorFont import setColorFont

# Warna ANSI
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

def main():
    while True:
        try:
            subprocess.run(["clear"])
            print(f"{CYAN}=============================================={RESET}")
            print(f"{CYAN}         TERMUX CUSTOM SETUP INTERACTIVE      {RESET}")
            print(f"{CYAN}=============================================={RESET}")
            print("1. Customize Color & Font")
            print("2. Install Packages (Coming Soon)")
            print(f"{RED}q. Exit{RESET}")
            print(f"{CYAN}----------------------------------------------{RESET}")
            
            c = input(">> ").strip().lower()
            
            if c == 'q':
                print(f"\n{GREEN}Thank you for using the script! Bye!{RESET}")
                break
                
            if c == "1":
                # Langsung panggil fungsi dari modul sebelah
                setColorFont()
            elif c in ["2"]:
                print(f"{YELLOW}[INFO] Feature coming soon!{RESET}")
                import time; time.sleep(1)
            else:
                print(f"{RED}You fell into the void (Invalid option).{RESET}")
                import time; time.sleep(1)

        except (KeyboardInterrupt, EOFError):
            print(f"\n{GREEN}Bye!{RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()
