import data_form

output = []
count_lines = 0

with open (data_form.save_file_adress) as count_file_strs:
    count_lines
    for line in count_file_strs:
        count_lines+=1
print(count_lines)

with open(data_form.save_file_adress, 'r') as base_file:
    for i in range(count_lines):
        output.append(list(base_file.readline(i)))

for i in output:
    print(i)