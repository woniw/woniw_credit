#!/bin/zsh

if [ -d "venv" ]; then
  echo "venv already exists, skipping creation"
else
  echo "making venv"
  python3 -m venv venv
fi

echo "activating venv"
source venv/bin/activate

echo "upgrading pip"
pip install --upgrade pip

echo "installing requirements"
pip install -r requirements.txt
