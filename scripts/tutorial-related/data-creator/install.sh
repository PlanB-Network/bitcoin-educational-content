#!/usr/bin/env bash
set -euo pipefail

if [[ $EUID -ne 0 ]]; then
  echo "🔐  Switching to root to install system packages…"
  exec sudo "$0" "$@"
fi

apt-get update -qq
apt-get install -y python3-tk python3-venv

su - "$SUDO_USER" <<'EOF'
set -euo pipefail

APP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV="$HOME/.planb-creator-venv"

echo "🐍  Creating/using virtualenv at $VENV"
python3 -m venv "$VENV"
source "$VENV/bin/activate"

python -m pip install --upgrade pip
python -m pip install -r "$APP_DIR/requirements.txt"

echo -e "\n✅ Installation finished."
echo "Run the app with:"
echo "  source \"$VENV/bin/activate\" && python \"$APP_DIR/main.py\""
EOF
