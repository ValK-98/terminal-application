#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Display help message
if [[ "$1" == "--help" || "$1" == "-h" ]]; then
    echo "Usage: $0"
    echo "Runs the Workout Application. Make sure you have Python 3 installed."
    exit 0
fi

# Check if python3 is installed
command -v python3 &>/dev/null || {
    echo -e "${RED}Python 3 is required but it's not installed. Exiting.${NC}"
    exit 1
}

# Navigate to the directory containing the Python scripts
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if main.py exists
if [[ ! -f "main.py" ]]; then
    echo -e "${RED}main.py not found in the script directory. Please ensure it exists.${NC}"
    exit 1
fi

# Welcome message
echo -e "${GREEN}Welcome to the Workout Application!${NC}"

# Run the main.py script using Python 3 and log the output
python3 main.py 2>&1

# Exit message
echo -e "${GREEN}Thank you for using the Workout Application! Have a great day!${NC}"

# Confirm before exit
read -p "Press any key to exit..."
