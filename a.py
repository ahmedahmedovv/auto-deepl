import deepl
import os
import glob
from dotenv import load_dotenv

def main():
    # Load DeepL key
    load_dotenv()
    auth_key = os.getenv("DEEPL_KEY")
    if not auth_key:
        print("Error: DeepL API key not found in .env file!")
        return

    translator = deepl.Translator(auth_key)
    
    # Get current directory
    current_dir = os.getcwd()
    
    # Find all .txt files in current directory
    txt_files = glob.glob(os.path.join(current_dir, '*.txt'))
    files_to_translate = [f for f in txt_files if not f.endswith('_translated.txt')]
    
    if not files_to_translate:
        print("No files to translate!")
        return
    
    print(f"Found {len(files_to_translate)} files to translate:")
    for i, file in enumerate(files_to_translate, 1):
        print(f"{i}. {os.path.basename(file)}")
    
    # Process files
    for i, input_file in enumerate(files_to_translate, 1):
        try:
            print(f"\nProcessing {i}/{len(files_to_translate)}: {os.path.basename(input_file)}")
            
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
            
            result = translator.translate_text(text, target_lang="TR")
            
            base_name = os.path.splitext(input_file)[0]
            output_file = f"{base_name}_translated.txt"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result.text)
            
            print(f"Successfully created: {os.path.basename(output_file)}")
            
        except Exception as e:
            print(f"Error processing {os.path.basename(input_file)}: {str(e)}")
    
    print("\nTranslation process completed!")

if __name__ == "__main__":
    main()