@echo off
chcp 65001 >nul
echo ===================================
echo   小六壬占卜程序 - 透明推算版
echo ===================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误：未找到Python，请先安装Python 3.6或更高版本
    echo 下载地址：https://www.python.org/downloads/
    pause
    exit /b 1
)

echo 正在启动小六壬占卜程序（透明推算版）...
echo.
echo 特色功能：
echo   ✓ 分步骤显示推算过程
echo   ✓ 月起始 → 日走位 → 时落位
echo   ✓ 总体判断和详细解读
echo.

REM 启动透明推算版GUI程序
python "%~dp0gui_divination_transparent.py"

if %errorlevel% neq 0 (
    echo.
    echo 程序运行出错，请检查错误信息
    pause
)
