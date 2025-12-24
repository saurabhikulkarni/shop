@echo off
echo Fixing Gradle and building APK...
echo.

echo Step 1: Stopping all Gradle daemons...
cd /d "d:\shop\E-commerce-Complete-Flutter-UI\android"
call gradlew --stop
timeout /t 3 /nobreak >nul

echo.
echo Step 2: Killing any remaining Java processes...
taskkill /F /IM java.exe /T 2>nul
timeout /t 2 /nobreak >nul

echo.
echo Step 3: Deleting Gradle cache...
rd /s /q "%USERPROFILE%\.gradle" 2>nul
timeout /t 2 /nobreak >nul

echo.
echo Step 4: Cleaning Flutter build...
cd /d "d:\shop\E-commerce-Complete-Flutter-UI"
call flutter clean

echo.
echo Step 5: Building APK...
call flutter build apk --release

echo.
echo Done!
pause
