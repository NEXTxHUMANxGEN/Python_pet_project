from data_form import *
# from data_form import data_base
import base_init
import base_io
import base_search
import base_save_del



while True:
    choice = int(input("Choose the operation to do:\n0)end programm\n1)add new members to base;\n2)search for data in base;\n3)print base;\n4)delete all base;\n"))
    if int(choice) ==0:
        print("Programm has been closed\n")
        break
    elif choice == 1:
        data_base = read_base_from_file()
        base_init.add_new_members(data_base)
        base_save_del.base_save_in_file(data_base)
        data_base = read_base_from_file()
        continue
    elif choice == 2:
        base_search.search_for_few_member(data_base)
        continue
    elif choice == 3:
        data_base = read_base_from_file()
        base_io.print_base(data_base)
        continue
    elif choice == 4:
        base_save_del.base_del_full()
        data_base = read_base_from_file()
        continue
    elif choice == 99:
        del_file_no = open('data_base_info.txt', 'w')
        del_file_no.close()
    else:
        print("Make the existing choice please")