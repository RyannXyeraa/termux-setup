#!/bin/bash

# Ensure Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python is required but not installed. Installing Python silently..."
    pkg update -y > /dev/null 2>&1
    pkg install python -y > /dev/null 2>&1
fi

# Run the interactive custom installer
python3 installer.py
