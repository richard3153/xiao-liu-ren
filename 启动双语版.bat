@echo off
chcp 65001 > nul
echo ================================================
echo    🔮 小六壬占卜程序 - 双语版启动器
echo    Xiao Liu Ren Divination - Bilingual Launcher
echo ================================================
echo.

REM 查找 Python
set PYTHON_CMD=python
python --version >nul 2>&1
if errorlevel 1 (
    set PYTHON_CMD=py
    py --version >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] 未找到 Python！请安装 Python 3.6+
        echo [ERROR] Python not found! Please install Python 3.6+
        pause
        exit /b 1
    )
)

echo [OK] 正在启动双语版程序...
echo [OK] Launching bilingual version...
echo.

cd /d "%~dp0"
%PYTHON_CMD% gui_divination_bilingual.py

if errorlevel 1 (
    echo.
    echo [ERROR] 程序异常退出，错误代码：%errorlevel%
    echo [ERROR] Program exited with error code: %errorlevel%
    pause
)
