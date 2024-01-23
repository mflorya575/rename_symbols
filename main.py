"""
Данный скрипт работает следующим образом: программа проходит в указанной папке по всем файлам
с расширением .html и делает 2 действия:
- меняет какие-то данные на другие (строчка 15), функция replace_symbols
- меняет .htm на .html
"""

import os

def replace_symbols(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Заменить нужные символы
    content = content.replace('старое слово (фраза)', 'новое слово (фраза)')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


# def update_html_links(html_path):
#    with open(html_path, 'r', encoding='utf-8') as file:
#        content = file.read()
#
#    # Заменить ссылки .htm на .html и выполнить дополнительные проверки
#    content = content.replace('.htm', '.html')
#
#    # Проверить количество 'l' в конце строки и добавить только одну 'l'
#    if content.endswith('l') and content.rstrip('l'):
#        content = content.rstrip('l') + 'l'

#    with open(html_path, 'w', encoding='utf-8') as file:
#        file.write(content)

def process_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            if file.endswith('.html'):
                replace_symbols(file_path)
#                update_html_links(file_path)

if __name__ == "__main__":
    folder_path = 'C:/vs_code/webbbbbbb/gdvl.ru/'  # Заменить на свой путь
    process_files(folder_path)
