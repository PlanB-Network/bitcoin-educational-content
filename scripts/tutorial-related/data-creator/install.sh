#!/usr/bin/env bash
set -e

echo "🔧 Installing system dependencies…"
sudo apt-get update
sudo apt-get install -y python3-tk

echo "🐍 Installing Python dependencies…"
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "✅ Installation complete. Launch the application with: python3 main.py"
