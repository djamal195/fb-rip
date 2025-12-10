#!/bin/bash
# Installation pour Termux/PC
if command -v pkg >/dev/null 2>&1; then
    pkg install python git -y
else
    # Sur PC, assume Python installé
    echo "Assure-toi d'avoir Python 3 installé."
fi
pip install --upgrade pip
git clone https://github.com/djamal195/fb-rip.git
cd fb-rip
chmod +x RIP.py
echo "✅ Installation OK ! Lance : python main.py"
echo "Assure-toi d'être connecté à Facebook sur ton navigateur."
