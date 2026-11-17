@echo off
chcp 65001 >nul
title 推送项目到 GitHub - 无极仙途国际化工作台
cd /d "%~dp0无极仙途国际化翻译"
call 一键推送GitHub.bat
