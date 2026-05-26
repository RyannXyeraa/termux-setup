#!/usr/bin/env python3

import subprocess


def check_internet():
    result = subprocess.run(
        ["ping", "-c", "1", "8.8.8.8"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0
