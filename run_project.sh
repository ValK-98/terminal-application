#!/bin/bash

# Check if python3 is installed
command -v python3 &>/dev/null || { echo "Python 3 is required but it's not installed. Exiting."; exit 1; }

# Navigate to the directory containing the Python scripts
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Run the main.py script using Python 3
python3 main.py

