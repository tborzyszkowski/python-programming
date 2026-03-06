#!/usr/bin/env bash
# setup_venv.sh – Tworzy i konfiguruje środowisko wirtualne (Linux/macOS/Git Bash)
# Uruchomienie: bash scripts/setup_venv.sh

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENV_DIR="$ROOT/.venv"
REQ="$ROOT/requirements.txt"

echo ">>> Katalog projektu: $ROOT"

# 1. Utwórz venv (jeśli nie istnieje)
if [ ! -f "$VENV_DIR/pyvenv.cfg" ]; then
    echo ">>> Tworzę venv w $VENV_DIR ..."
    python3 -m venv "$VENV_DIR"
else
    echo ">>> venv już istnieje – pomijam tworzenie."
fi

# 2. Zainstaluj / zaktualizuj zależności
PIP="$VENV_DIR/bin/pip"
echo ">>> Aktualizuję pip ..."
"$PIP" install --upgrade pip --quiet

echo ">>> Instaluję zależności z $REQ ..."
"$PIP" install -r "$REQ"

echo ""
echo ">>> Gotowe! Aby aktywować środowisko:"
echo "    source .venv/bin/activate"
echo ""
echo ">>> Aby uruchomić testy:"
echo "    python -m pytest src/_01-introduction -v"

