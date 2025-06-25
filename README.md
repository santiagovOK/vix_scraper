# VIX Scraper

This project contains scripts to fetch the current value of the S&P 500 Volatility Index (VIX) and display it on your desktop panel (Debian-based Openbox + tint2 / XFCE oriented).

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/vix-scraper.git
   cd vix-scraper
   ```

2. Create a virtual environment:
   ```sh
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On Unix/macOS:
     ```sh
     source venv/bin/activate
     ```
   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```

4. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the Python script to fetch the VIX value:

   ```sh
   python scripts/vix_scraper.py
   ```

2. Run the shell script to update the VIX value on your desktop panel:

   ```sh
   #!/bin/bash

   # Navigate to the project directory
   cd /path/to/your/project

   # Activate the virtual environment
   source venv/bin/activate

   # Run the Python script and capture the output
   vix_value=$(python scripts/vix_scraper.py)

   # Deactivate the virtual environment
   deactivate

   # Update the desktop panel with the VIX value
   # Make sure to adjust the command according to the panel you are using

   echo "VIX: $vix_value" > /tmp/vix_value.txt
   ```

   Make this script executable and configure it to run at the start of your session:

   ```sh
   chmod +x /path/to/your/script/update_vix.sh
   ```

   And add the script to your login file (e.g., `.bashrc`, `.zshrc`, etc.):

   ```sh
   # Add to the end of the login file
   /path/to/your/script/update_vix.sh &
   ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.