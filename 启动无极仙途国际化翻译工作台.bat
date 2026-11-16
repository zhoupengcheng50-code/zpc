@echo off
cd /d "%~dp0"
chcp 65001 >nul
python workbench\launch.py
pause
