#!/usr/bin/env bash
set -euo pipefail


if ! command -v apt-get >/dev/null 2>&1; then
  echo "❌  Unsupported distribution (requires apt-get)" >&2
  exit 1
fi


if [[ $EUID -ne 0 ]]; then
  echo "🔐  Elevating privileges…"
  exec sudo -E "$0" "$@"
fi


apt-get update -qq
apt-get install -y python3-tk python3-venv


: "${SUDO_USER:=$(logname)}"
APP_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="/home/$SUDO_USER/.planb-creator-venv"

export APP_DIR VENV


sudo -u "$SUDO_USER" -E bash - <<EOS
set -euo pipefail

echo "🐍  Using virtualenv at $VENV"
if [ ! -d "$VENV" ]; then
  python3 -m venv "$VENV"
fi
source "$VENV/bin/activate"

python -m pip install --upgrade pip
python -m pip install --upgrade-strategy eager -r "$APP_DIR/requirements.txt"

echo -e "\n✅  Installation finished."
echo "Run the app with:"
echo "  source \"$VENV/bin/activate\" && python \"$APP_DIR/main.py\""
EOS
