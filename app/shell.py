#!/usr/bin/env python3

import os

from constants import GREEN, YELLOW, RED, RESET


def get_shell():
    shell = os.environ.get("SHELL", "")

    if "bash" in shell:
        return {
            "name": "bash",
            "rc": os.path.expanduser("~/.bashrc")
        }

    elif "zsh" in shell:
        return {
            "name": "zsh",
            "rc": os.path.expanduser("~/.zshrc")
        }

    return None


def enable_starship():
    shell_data = get_shell()

    if not shell_data:
        print(f"{RED}[ERROR] Unsupported shell!{RESET}")
        return

    shell_name = shell_data["name"]
    rc_file = shell_data["rc"]

    init_line = f'eval "$(starship init {shell_name})"'

    # Create rc file if missing
    if not os.path.exists(rc_file):
        open(rc_file, "w").close()

    # Read existing content
    with open(rc_file, "r") as f:
        content = f.read()

    # Prevent duplicate config
    if init_line in content:
        print(f"{YELLOW}[INFO] Starship already enabled.{RESET}")
        return

    # Append config
    with open(rc_file, "a") as f:
        f.write(f"\n{init_line}\n")

    print(f"{GREEN}[SUCCESS] Starship enabled for {shell_name}!{RESET}")
    print(f"Please restart your shell.\nRun: source ~/.{shell_name}rc")
