import data_form


def count_line():
    count_lines = 0
    with open (data_form.save_file_adress) as count_file_strs:
        for line in count_file_strs:
            count_lines+=1
    return(count_lines)

def read_base_from_file():
    output = []
    with open(data_form.save_file_adress, 'r') as base_file:
        for i in range(count_line()):
            output.append(list(base_file.readline().split(', ')))
            output[i].remove("\n")
    return(output)

# for i in output:
#     print(i)