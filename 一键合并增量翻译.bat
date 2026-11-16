@echo off
chcp 65001 >nul
cd /d "%~dp0"
python merge_increment_translations.py
echo.
pause
