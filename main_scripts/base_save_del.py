from data_form import save_file_adress
from data_form import elems_of_base


def base_save_in_file(data_base):
    base_file = open(save_file_adress, 'w')
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
        del_file = open(save_file_adress, 'w')
        for elems in range(len(elems_of_base)):
            del_file.write(elems_of_base[elems] + ", ")
        del_file.write("\n")
        for zeros in range(len(elems_of_base)):
            del_file.write("0, ")
        del_file.write("\n")
        del_file.close()
        print("Base has been deleted\n")
    else:
        print("Your answer was not like DELETE BASE")


