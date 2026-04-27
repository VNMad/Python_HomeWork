#____________________________________________________________________
#1. Фильтрация по ключевому слову
#____________________________________________________________________
import os
print(os.getcwd())


def filter_file(fn, kw):
    if not os.path.exists(fn):
        return "Error: file not exists"

    with open(fn, "r", encoding="utf-8") as f:
        matched_lines = [line for line in f if kw.lower() in line.lower()]

    if matched_lines:
        new_filename = f"{kw}_{fn}"

        with open(new_filename, "w", encoding="utf-8") as new_f:
            new_f.writelines(matched_lines)

        #return f"Строки, содержащие '{kw}', сохранены в {new_filename}."
        return {"keyword": kw, "filename": new_filename}
    else:
        return {"error": "No matches found. The file was not created."}

filename = input("Введите имя файла для поиска: ")
keyword = input("Введите ключевое слово: ")

result = filter_file(filename, keyword)

if "error" in result:
    print(result["error"])
else:
    print(f"Строки, содержащие '{result['keyword']}', сохранены в {result['filename']}.")
#print(filter_file(filename, keyword))

#____________________________________________________________________
#2. Поиск и удаление дубликатов
#____________________________________________________________________
import os


def remove_duplicates(fn):
    if not os.path.exists(fn):
        #return "Error: file not exists"
        return {"error": "Error: file not exists"}
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

    #return f"Дубликаты удалены. Уникальные строки сохранены в {new_filename}."
    return {"filename": new_filename}

filename = input("Введите имя файла: ")
result = remove_duplicates(filename)

if "error" in result:
    print(result["error"])
else:
    print(f"Дубликаты удалены. Уникальные строки сохранены в {result['filename']}.")
#print(remove_duplicates(filename))