import os

# Путь к папке (укажите свой путь)
folder_path = 'music'  # Замените на нужный путь

# Получаем список файлов в папке
files = os.listdir(folder_path)

# Сортируем файлы по имени
files.sort()

# Выводим файлы с нумерацией
for index, file in enumerate(files, start=1):
    print(f"{index}. {file}")
    
