#!/usr/bin/env python3

import subprocess


def clear():
    subprocess.run(["clear"])


def run(command, silent=False):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if not silent:
        if result.stdout:
            print(result.stdout)

        if result.stderr:
            print(result.stderr)

    return result


def check_package(package):
    """
    Check whether package/binary exists.
    """

    result = subprocess.run(
        [
            "sh",
            "-c",
            f"command -v {package}"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0
