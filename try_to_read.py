file = open('data_base_info.txt', 'r')
# for line in file:
#     print(line)
print(file.read())

try_base = []


output = []

with open('data_base_info.txt', 'r') as file:
    for line in file:
        output += line.strip().split(", ")


with open('data_base_info.txt', 'r') as len_file:
    print(len(len_file.read().split(", ")))


print(output)
# чтенние через readline() и split + заполнение массива сплитом

# колисчетсво элементов берём из файла со структурой (список элементов для шапки таблицы)