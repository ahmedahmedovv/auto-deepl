@echo off
pyinstaller --onefile --console ^
--hidden-import deepl ^
--hidden-import dotenv.main ^
--name AutoTranslator ^
a.py

echo Cleaning up...
del /Q build\TextTranslatorGUI *.spec
echo Copying .env...
copy .env dist\.env /Y
echo Build complete. Check dist folder. 