#!/bin/bash

echo "🔥 Checking for Go installation..."
if ! command -v go &> /dev/null
then
    echo "❌ Go is not installed. Please install Golang first."
    exit 1
fi
echo "[+] Go is already installed!"

echo "🔥 Installing dependencies..."
go mod init cyberxray 2>/dev/null
go mod tidy

echo "🔥 Building the tool..."
go build -o cyberx-ray main.go

if [ ! -f "cyberx-ray" ]; then
    echo "❌ Build failed! Check your Go code."
    exit 1
fi

echo "🔥 Moving binary to /usr/local/bin/"
sudo mv cyberx-ray /usr/local/bin/

echo "🔥 Setting permissions..."
sudo chmod +x /usr/local/bin/cyberx-ray

echo "✅ Installation complete! Now you can run the tool from anywhere using: cyberx-ray"
