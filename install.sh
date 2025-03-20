#!/bin/bash

echo "🔥 Checking for Go installation..."
if ! command -v go &> /dev/null
then
    echo "[+] Go not found! Installing Go..."
    sudo apt update && sudo apt install -y golang
else
    echo "[+] Go is already installed!"
fi

echo "🔥 Installing dependencies..."
go mod init professor-scan > /dev/null 2>&1
go mod tidy

echo "🔥 Building the tool..."
go build -o professor-scan test.go

echo "🔥 Moving binary to /usr/local/bin/"
sudo mv professor-scan /usr/local/bin/professor-scan

echo "🔥 Setting permissions..."
sudo chmod +x /usr/local/bin/professor-scan

echo "✅ Installation complete! Now you can run the tool from anywhere using: professor-scan"
