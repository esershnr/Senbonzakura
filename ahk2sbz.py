import os
import re
import sys
import argparse

# Değiştirilecek eşleşmeler
REPLACEMENTS = {
    r'(?i)\bahk_id\b': 'sbz_id',
    r'(?i)\bahk_class\b': 'sbz_class',
    r'(?i)\bahk_exe\b': 'sbz_exe',
    r'(?i)\bahk_pid\b': 'sbz_pid',
    r'(?i)\bahk_group\b': 'sbz_group',
    r'(?i)#Requires\s+AutoHotkey': '#Requires Senbonzakura'
}

def convert_content(content):
    modified = content
    for pattern, replacement in REPLACEMENTS.items():
        modified = re.sub(pattern, replacement, modified)
    return modified

def convert_file(file_path):
    if not os.path.exists(file_path):
        print(f"Hata: {file_path} bulunamadı.")
        return False
        
    try:
        # Dosya içeriğini oku
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
            
        modified_content = convert_content(content)
        
        # Yeni dosya yolunu belirle (.ahk -> .sbz)
        base, _ = os.path.splitext(file_path)
        new_file_path = base + '.sbz'
        
        # Yeni dosyayı yaz
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
            
        print(f"Başarıyla Dönüştürüldü: {file_path} -> {new_file_path}")
        return True
    except Exception as e:
        print(f"Hata oluştu ({file_path}): {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="AutoHotkey (.ahk) betiklerini Senbonzakura (.sbz) formatına dönüştürür.")
    parser.add_argument("path", help="Dönüştürülecek dosya veya klasörün yolu.")
    
    args = parser.parse_args()
    target_path = args.path
    
    if os.path.isdir(target_path):
        # Klasör tarama
        print(f"Klasör taranıyor: {target_path}")
        converted_count = 0
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.lower().endswith('.ahk'):
                    full_path = os.path.join(root, file)
                    if convert_file(full_path):
                        converted_count += 1
        print(f"Toplam {converted_count} adet dosya dönüştürüldü.")
    else:
        # Tek dosya dönüştürme
        convert_file(target_path)

if __name__ == "__main__":
    main()
