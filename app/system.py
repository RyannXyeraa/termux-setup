#!/usr/bin/env python3

import subprocess


def clear():
    subprocess.run(["clear"])


def run(command, silent=False):
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    if not silent and result.stdout:
        print(result.stdout)

    return result
