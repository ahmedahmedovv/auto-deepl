# Text File Translator

Automated translation tool for converting .txt files using DeepL API

![Console Interface Demo](https://via.placeholder.com/600x300.png?text=Console+Translation+Demo)

## Features
- 🚀 Automatic detection of .txt files in executable directory
- 🌍 Translates content to Turkish (easily configurable to other languages)
- 📁 Creates *_translated.txt files for each source file
- 🔒 Secure API key management via .env file
- 🛠 Error handling with per-file error reporting
- 📦 Standalone Windows executable

## Requirements
- Windows 10/11 (64-bit)
- `TextTranslator.exe` in target directory
- `.env` file with valid DeepL API key
- Text files to translate (.txt format)

## Installation
1. Download latest release from [Releases page](#)
2. Create `.env` file in same directory as EXE with:
   ```text
   DEEPL_KEY=your_api_key_here
   ```
3. Place text files in the same directory

## Usage
1. Prepare text files in the EXE directory
2. Double-click `TextTranslator.exe`
3. Console window will show:
   - Number of files found
   - Progress for each file
   - Success/error messages
4. Translated files appear as `[original_name]_translated.txt`

Example directory structure: 