# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os
file_path = r"C:\Users\griva\Desktop\test.txt"

def split_file_path(file_path):
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    directory = os.path.dirname(file_path)
    return directory, file_name, file_extension

result = split_file_path(file_path)
print(result)