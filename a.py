import deepl
import os
import glob
from dotenv import load_dotenv
import sys
import io

# Fix console encoding for Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def main():
    load_dotenv()
    auth_key = os.getenv("DEEPL_KEY")
    if not auth_key:
        print("Error: DEEPL_KEY not found in .env file")
        return
    translator = deepl.Translator(auth_key)

    try:
        # Find all txt files in current directory
        txt_files = glob.glob('*.txt')
        
        # Filter out already translated files
        files_to_translate = [f for f in txt_files if not f.endswith('_translated.txt')]

        if not files_to_translate:
            print("No .txt files found in current directory")
            return

        for input_file in files_to_translate:
            # Read file content with UTF-8 encoding
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
            
            # Translate to Turkish
            result = translator.translate_text(text, target_lang="TR")
            
            # Create output filename
            base_name = os.path.splitext(input_file)[0]
            output_file = f"{base_name}_translated.txt"
            
            # Save translation with UTF-8 encoding
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result.text)
            print(f"Translated {input_file} -> {output_file}")

    except deepl.exceptions.DeepLException as e:
        print(f"DeepL API Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()