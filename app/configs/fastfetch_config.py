#!/usr/bin/env python3

import os

from constants import *
from ui import banner
from system import clear, run


def generate_fastfetch_config():
    config_dir = os.path.expanduser("~/.config/fastfetch")

    os.makedirs(config_dir, exist_ok=True)

    result = run(
        [
            "fastfetch",
            "--gen-config"
        ],
        silent=True
    )

    if result.returncode == 0:
        print(f"{GREEN}[SUCCESS] Fastfetch config generated!{RESET}")

    else:
        print(f"{RED}[ERROR] Failed to generate config!{RESET}")

        if result.stderr:
            print(result.stderr)

    input("\nPress Enter to continue...")
