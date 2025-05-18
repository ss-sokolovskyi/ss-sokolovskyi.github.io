import os
import re
import htmlmin

def optimize_html_files():
    print("Optimizing HTML files...")
    
    # Проходимо по всіх HTML файлах
    for root, dirs, files in os.walk('.'):        
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                if '.git' in file_path:
                    continue
                
                try:
                    # Читаємо вміст файлу
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Оптимізуємо HTML
                    optimized_content = htmlmin.minify(
                        content,
                        remove_comments=True,
                        remove_empty_space=True,
                        remove_all_empty_space=True,
                        remove_optional_attribute_quotes=False
                    )
                    
                    # Зберігаємо оптимізовану версію
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(optimized_content)
                    
                    print(f"Optimized: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")

def optimize_css_links():
    print("Optimizing CSS links...")
    
    # Проходимо по всіх HTML файлах
    for root, dirs, files in os.walk('.'):        
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                if '.git' in file_path:
                    continue
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Оптимізуємо CSS лінки
                    content = re.sub(r'\s+href="', ' href="', content)
                    content = re.sub(r'"\s+', '"', content)
                    
                    # Зберігаємо зміни
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"Optimized CSS links in: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")

def main():
    optimize_html_files()
    optimize_css_links()

if __name__ == '__main__':
    main()
