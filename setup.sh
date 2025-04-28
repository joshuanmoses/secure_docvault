#!/bin/bash

echo "===================================="
echo " Secure DocVault Setup Script"
echo "===================================="

# Step 1: Update and install system dependencies
echo "[+] Updating system packages..."
sudo apt update

echo "[+] Installing Python3, pip, and essential packages..."
sudo apt install -y python3 python3-pip python3-venv

# Step 2: Create Python virtual environment
echo "[+] Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Step 3: Install Python requirements
echo "[+] Installing Python libraries..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 4: Create necessary folders
echo "[+] Creating data directories..."
mkdir -p data/vault
mkdir -p models

# Step 5: Create initial users.json if missing
if [ ! -f data/users.json ]; then
  echo "[+] Creating initial user database..."
  cat <<EOT > data/users.json
{
  "admin": {
    "password_hash": "$(echo -n 'admin123' | sha256sum | awk '{print $1}')",
    "role": "admin"
  }
}
EOT
  echo "[!] Default admin user created (username: admin, password: admin123)"
fi

# Step 6: Generate dummy encryption key and TOTP seed if missing
if ! grep -q "your_32_byte_aes_key_here" config/settings.py; then
  echo "[+] Generating AES-256 key and updating settings.py..."
  AES_KEY=$(openssl rand -hex 32)
  TOTP_SEED=$(openssl rand -hex 10)
  sed -i "s|your_32_byte_aes_key_here___|${AES_KEY}|" config/settings.py
  sed -i "s|your_totp_seed_here|${TOTP_SEED}|" config/settings.py
fi

echo "===================================="
echo " Setup Complete!"
echo " To run the application:"
echo " 1. Activate your environment: source venv/bin/activate"
echo " 2. Start the server: python3 web/app.py"
echo "===================================="
