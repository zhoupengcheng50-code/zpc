@echo off
chcp 65001 >nul
title 推送项目到 GitHub - 无极仙途国际化工作台
cd /d "%~dp0"
set "PATH=%LOCALAPPDATA%\Programs\Git\cmd;%PATH%"

echo ========================================================
echo    无极仙途国际化翻译工作台 - 正在推送到 GitHub...
echo    远程仓库: https://github.com/zhoupengcheng50-code/zpc.git
echo ========================================================
echo.
echo 如果系统弹出 GitHub 登录窗口，请点击【Sign in with your browser】进行授权即可。
echo.

git push -u origin main

if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================================
    echo  [成功] 项目已全部成功推送到 GitHub！
    echo  访问地址: https://github.com/zhoupengcheng50-code/zpc
    echo ========================================================
) else (
    echo.
    echo ========================================================
    echo  [提示] 推送遇到问题，请检查网络或授权。
    echo ========================================================
)

echo.
pause
