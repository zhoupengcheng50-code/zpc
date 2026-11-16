@echo off
chcp 65001 >nul
cd /d "%~dp0"
python auto_translate_match.py
echo.
pause
