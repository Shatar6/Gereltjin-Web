@echo off
echo ========================================
echo Gereltjin LLC Website - Setup Script
echo ========================================
echo.

echo Step 1: Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo ✓ Virtual environment created
echo.

echo Step 2: Activating virtual environment...
call venv\Scripts\activate.bat
echo ✓ Virtual environment activated
echo.

echo Step 3: Upgrading pip...
python -m pip install --upgrade pip
echo ✓ Pip upgraded
echo.

echo Step 4: Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo ✓ Dependencies installed
echo.

echo Step 5: Setting up environment file...
if not exist .env (
    copy .env.example .env
    echo ✓ .env file created - PLEASE EDIT IT WITH YOUR SETTINGS
    echo   - Generate a new SECRET_KEY
    echo   - Configure email settings
) else (
    echo ✓ .env file already exists
)
echo.

echo Step 6: Running migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: Failed to run migrations
    pause
    exit /b 1
)
echo ✓ Database migrations completed
echo.

echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo Next steps:
echo 1. Edit .env file with your settings
echo 2. Create superuser: python manage.py createsuperuser
echo 3. Run server: python manage.py runserver
echo.
pause