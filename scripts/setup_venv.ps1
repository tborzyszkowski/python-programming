# setup_venv.ps1 – Tworzy i konfiguruje środowisko wirtualne dla projektu
# Uruchomienie: .\scripts\setup_venv.ps1
# Wymaganie: Python 3.11+

$Root    = Split-Path $PSScriptRoot -Parent
$VenvDir = Join-Path $Root ".venv"
$Req     = Join-Path $Root "requirements.txt"

Write-Host ">>> Katalog projektu: $Root" -ForegroundColor Cyan

# 1. Utwórz venv (jeśli nie istnieje)
if (-not (Test-Path (Join-Path $VenvDir "pyvenv.cfg"))) {
    Write-Host ">>> Tworzę venv w $VenvDir ..." -ForegroundColor Yellow
    python -m venv $VenvDir
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Nie udało się utworzyć venv. Upewnij się, że Python 3.11+ jest w PATH."
        exit 1
    }
} else {
    Write-Host ">>> venv już istnieje – pomijam tworzenie." -ForegroundColor Green
}

# 2. Zainstaluj / zaktualizuj zależności
$Pip = Join-Path $VenvDir "Scripts\pip.exe"
Write-Host ">>> Aktualizuję pip ..." -ForegroundColor Yellow
& $Pip install --upgrade pip --quiet

Write-Host ">>> Instaluję zależności z $Req ..." -ForegroundColor Yellow
& $Pip install -r $Req

Write-Host ""
Write-Host ">>> Gotowe! Aby aktywować środowisko:" -ForegroundColor Green
Write-Host "    .\.venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host ""
Write-Host ">>> Aby uruchomić testy:" -ForegroundColor Green
Write-Host "    .\.venv\Scripts\python.exe -m pytest src\_01-introduction -v" -ForegroundColor White

