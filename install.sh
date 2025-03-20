#!/bin/bash

echo "🔥 Checking for Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "[-] Python3 is not installed. Please install it and try again."
    exit 1
else
    echo "[+] Python3 is installed!"
fi

echo "🔥 Installing dependencies..."
pip3 install -r requirements.txt

echo "🔥 Making CyberX-Ray executable..."
chmod +x cyberxray.py

echo "🔥 Moving CyberX-Ray to /usr/local/bin/"
sudo mv cyberxray.py /usr/local/bin/cyberxray

echo "✅ Installation complete! Now you can run the tool from anywhere using: cyberxray"
