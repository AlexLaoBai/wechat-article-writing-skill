@echo off
chcp 65001 >nul
echo Cleaning up files...

:: Delete __pycache__ directory
if exist "scripts\__pycache__" (
    rmdir /s /q "scripts\__pycache__"
    echo Deleted: scripts\__pycache__
) else (
    echo Not found: scripts\__pycache__
)

:: Delete nul file (special handling for Windows)
if exist "nul" (
    del /f /q "nul" 2>nul
    if exist "nul" (
        :: Try alternative method
        type nul > nul.tmp 2>nul
        del nul 2>nul
        del nul.tmp 2>nul
        echo Attempted to delete: nul
    ) else (
        echo Deleted: nul
    )
) else (
    echo Not found: nul
)

:: List remaining Python cache files
echo.
echo Checking for remaining cache files...
dir /s /b *.pyc 2>nul | findstr "__pycache__" && echo Found pycache files || echo No pycache files found

echo.
echo Cleanup complete!
pause