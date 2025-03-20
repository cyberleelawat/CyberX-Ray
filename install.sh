#!/bin/bash

echo "🔥 Checking for Go installation..."
if ! command -v go &> /dev/null
then
    echo "[!] Go is not installed! Please install Go and run this script again."
    exit 1
else
    echo "[+] Go is already installed!"
fi

# Set Go path in bashrc/zshrc if not set
if [ -z "$GOPATH" ]; then
    echo "🔥 Setting up Go environment variables..."
    echo 'export GOPATH=$HOME/go' >> ~/.bashrc
    echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc
    source ~/.bashrc
    echo "[+] Go environment variables set!"
fi

echo "🔥 Installing dependencies..."
go mod tidy

echo "🔥 Building the tool..."
go build -o cyberx-ray main.go

echo "🔥 Moving binary to /usr/local/bin/"
sudo mv cyberx-ray /usr/local/bin/

echo "🔥 Setting permissions..."
sudo chmod +x /usr/local/bin/cyberx-ray

echo "✅ Installation complete! Now you can run the tool from anywhere using: cyberx-ray"
