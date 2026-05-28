#!/usr/bin/env python3

import time

from constants import *
from ui import banner
from system import clear, run
from shell import enable_starship
from network import check_internet

def pconfig_menu():
    while True:
        banner("Package Configuration")
        print(f"{RED}0. Back{RESET}")

        choice = input("\nSelect >> ").strip().lower()
        if choice == "0":
            break

