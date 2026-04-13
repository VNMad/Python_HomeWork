#____________________________________________________________________
#1. Список файлов и папок
#____________________________________________________________________
import sys
import os

if len(sys.argv) == 1: print("Ошибка: укажите путь к директории"); sys.exit()

path = sys.argv[1]

if not os.path.exists(path): print("Ошибка: путь не существует"); sys.exit()
if not os.path.isdir(path): print("Ошибка: это не директория"); sys.exit()

items = [(item, os.path.join(path, item)) for item in os.listdir(path)]

folders = [name for name, full_path in items if os.path.isdir(full_path)]
files = [(name, os.path.getsize(full_path)) for name, full_path in items if os.path.isfile(full_path)]

def format_size(s):
    if s < 1024:
        return f"{s} B"
    if s < 1024**2:
        return f"{s // 1024} KB"
    if s < 1024**3:
        return f"{s // (1024**2)} MB"
    return f"{s // (1024**3)} GB"


print(f"Содержимое директории '{path}':\n")
print("Папки:\n" + "\n".join(f"- {folder}" for folder in folders))
print("\nФайлы:\n" + "\n".join(f"- {file} ({format_size(size)})" for file, size in files))

#____________________________________________________________________
#2. Поиск и удаление файлов с указанным расширением
#____________________________________________________________________

import sys
import os

if len(sys.argv) != 3: print("Ошибка: укажите путь и расширение"); sys.exit()

path = sys.argv[1]
extension = sys.argv[2]

if not os.path.exists(path): print("Ошибка: путь не существует"); sys.exit()
if not os.path.isdir(path): print("Ошибка: это не директория"); sys.exit()

files = []

for root, dirs, filenames in os.walk(path):
    for file in filenames:
        if file.endswith(extension):
            files.append(os.path.join(root, file))

if files:
    print(f"Найдены файлы с расширением '{extension}':\n")
    print("\n".join(f"- {file}" for file in files))

    answer = input("\nВы хотите удалить эти файлы? (y/n): ")

    if answer.lower() in ("y", "yes"):
        for file in files:
            try:
                os.remove(file)
            except FileNotFoundError:
                print(f"Файл не найден: {file}")
            except PermissionError:
                print(f"Нет прав для удаления: {file}")
            except OSError as e:
                print(f"Ошибка при удалении {file}: {e}")
        print("Удаление завершено.")
    else:
        print("Удаление отменено.")
else:
    print("Файлы не найдены.")
