#____________________________________________________________________
#1. Фильтрация по ключевому слову
#____________________________________________________________________
import os
print(os.getcwd())


def filter_file(fn, kw):
    if not os.path.exists(fn):
        print("Error: file not exists")
        return

    with open(fn, "r", encoding="utf-8") as f:
        matched_lines = [line for line in f if kw.lower() in line.lower()]

    if matched_lines:
        new_filename = f"{kw}_{fn}"
        with open(new_filename, "w", encoding="utf-8") as new_f:
            new_f.writelines(matched_lines)
        print(f"Строки, содержащие '{kw}', сохранены в {new_filename}.")
    else:
        print("No matches found. The file was not created.")


filename = input("Введите имя файла для поиска: ")
keyword = input("Введите ключевое слово: ")

filter_file(filename, keyword)

#____________________________________________________________________
#2. Фильтрация по ключевому слову
#____________________________________________________________________
import os

def remove_duplicates(fn):
    if not os.path.exists(fn):
        print("Error: file not exists")
        return

    unique_lines = []
    seen = set()

    with open(fn, "r", encoding="utf-8") as f:
        for line in f:
            if line not in seen:
                unique_lines.append(line)
                seen.add(line)

    new_filename = f"unique_{fn}"

    with open(new_filename, "w", encoding="utf-8") as new_file:
        new_file.writelines(unique_lines)

    print(f"Дубликаты удалены. Уникальные строки сохранены в {new_filename}.")


filename = input("Введите имя файла: ")
remove_duplicates(filename)