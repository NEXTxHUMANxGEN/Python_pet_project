from data_form import *



def base_save_in_file():
    base_file = open(save_file_adress, 'a')
    for i in range(len(data_base)):
        for z in range(len(data_base[i])):
            base_file.write(str(data_base[i][z]) + ", ")
        base_file.write("\n")
    base_file.close()

def base_del_full():
    check_for_del = input("Type DELETE BASE (register is important) to delete all base\n")
    if check_for_del.strip() == "DELETE BASE":
        del_file = open(save_file_adress, 'w')
        del_file.close()
    

















