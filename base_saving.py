


def base_save_in_file(data_base):
    base_file = open('data_base.txt', 'w')
    for i in range(len(data_base)):
        for z in range(len(data_base[i])):
            base_file.write(str(data_base[i][z]) + ", ")
        base_file.write("\n")
    base_file.close()