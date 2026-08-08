```bat
@echo off
title MYPASS Manager

cd /d "E:\projects\new_projects\MYPASS_MANAGER"

call ".venv\Scripts\activate.bat"

echo ========================================
echo        MYPASS MANAGER
echo ========================================
echo.
echo URL: http://127.0.0.1:8100
echo USER: hamed
echo PASS: 1111
echo ========================================
echo.

python manage.py runserver 127.0.0.1:8100

echo.
echo Django server stopped.
pause
```
