@echo off
echo ========================================
echo Compiling Mongolian Translations
echo ========================================
echo.

REM Set the path to gettext tools
set GETTEXT_PATH=C:\Program Files\gettext-iconv\bin

REM Add to PATH temporarily
set PATH=%GETTEXT_PATH%;%PATH%

echo Checking msgfmt...
msgfmt --version
if %errorlevel% neq 0 (
    echo ERROR: msgfmt not found
    echo Please install gettext or check the path
    pause
    exit /b 1
)
echo.

echo Compiling Mongolian translations...
if exist "locale\mn\LC_MESSAGES\django.po" (
    "%GETTEXT_PATH%\msgfmt" -o "locale\mn\LC_MESSAGES\django.mo" "locale\mn\LC_MESSAGES\django.po"
    if %errorlevel% equ 0 (
        echo ✓ Mongolian translations compiled successfully!
        echo   Created: locale\mn\LC_MESSAGES\django.mo
    ) else (
        echo ERROR: Failed to compile translations
        pause
        exit /b 1
    )
) else (
    echo ERROR: Translation file not found!
    echo Please make sure django.po exists in: locale\mn\LC_MESSAGES\
    pause
    exit /b 1
)
echo.

echo ========================================
echo Translation compilation complete!
echo ========================================
echo.
echo Now restart your Django server:
echo python manage.py runserver
echo.
echo Then test language switching in your browser.
echo.
pause
