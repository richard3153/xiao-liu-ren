@echo off
chcp 65001 >nul
echo ===================================
echo     小六壬占卜程序 - 完整增强版
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

echo 正在启动小六壬占卜程序（完整增强版）...
echo.
echo 提示：增强版包含详细解读和完整卦象分析
echo.

REM 启动增强版GUI程序
python "%~dp0gui_divination_enhanced.py"

if %errorlevel% neq 0 (
    echo.
    echo 程序运行出错，请检查错误信息
    pause
)
