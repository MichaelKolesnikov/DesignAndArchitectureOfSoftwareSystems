import os
import re
import shutil
import argparse
from pathlib import Path

def create_and_process_files(start_letter='a', end_letter='p'):
    # 1. Создание папки txtFiles
    txt_folder = Path("txtFiles")
    txt_folder.mkdir(exist_ok=True)
    
    # 2. Копирование файлов с числовыми именами и изменение расширения на .txt
    current_dir = Path(".")
    
    for file_path in current_dir.iterdir():
        if file_path.is_file():
            stem = file_path.stem
            if re.match(r'^\d+(\.\d+)?$', stem):
                new_path = txt_folder / f"{stem}.txt"
                shutil.copy2(file_path, new_path)
    
    # 3. Конкатенация всех txt файлов
    concatenated_string = ""
    txt_files = sorted(txt_folder.glob("*.txt"), key=lambda x: x.stem)
    
    for txt_file in txt_files:
        with open(txt_file, 'r', encoding='utf-8') as f:
            concatenated_string += f.read()
    
    # 4. Создание отсортированного списка букв
    letters = [chr(i) for i in range(ord(start_letter), ord(end_letter) + 1)]
    first_occurrence = {}
    
    for letter in letters:
        pattern = f'\\[{letter}\\]'
        match = re.search(pattern, concatenated_string)
        first_occurrence[letter] = match.start() if match else float('inf')
    
    sorted_letters = sorted(letters, key=lambda x: first_occurrence[x])
    replacement_dict = {letter: index for index, letter in enumerate(sorted_letters)}
    
    # 5. Замена вхождений в файлах
    for txt_file in txt_files:
        with open(txt_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for letter, index in replacement_dict.items():
            pattern = f'\\[{letter}\\]'
            content = re.sub(pattern, f"[{index + 1}]", content)
        
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return txt_files, concatenated_string, sorted_letters, replacement_dict

def main():
    parser = argparse.ArgumentParser(description='Обработка файлов с числовыми именами')
    parser.add_argument('--start', default='a', help='Начальная буква диапазона')
    parser.add_argument('--end', default='p', help='Конечная буква диапазона')
    
    args = parser.parse_args()
    
    if len(args.start) != 1 or len(args.end) != 1:
        print("Ошибка: каждая буква должна быть одним символом")
        return
    
    if not ('a' <= args.start <= 'z') or not ('a' <= args.end <= 'z'):
        print("Ошибка: буквы должны быть строчными латинскими")
        return
    
    if args.start > args.end:
        print("Ошибка: начальная буква должна быть раньше конечной")
        return
    
    txt_files, concatenated_string, sorted_letters, replacement_dict = create_and_process_files(
        args.start, args.end
    )
    
    # Вывод результатов
    print(f"\nОбработанные файлы (в порядке ls):")
    for f in txt_files:
        print(f"  {f.name}")
    
    print(f"\nОтсортированные буквы от '{args.start}' до '{args.end}':")
    for i, letter in enumerate(sorted_letters):
        print(f"  {i}: {letter}")
    
    print(f"\nЗамены, выполненные в файлах:")
    for letter, index in sorted(replacement_dict.items()):
        print(f"  [{letter}] -> [{index}]")
    
    print(f"\nСтатистика:")
    print(f"  Всего файлов: {len(txt_files)}")
    print(f"  Длина конкатенированной строки: {len(concatenated_string)}")
    print(f"  Диапазон: {args.start}-{args.end} ({len(sorted_letters)} букв)")

if __name__ == "__main__":
    main()
