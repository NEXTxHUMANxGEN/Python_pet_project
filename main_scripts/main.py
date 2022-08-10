
import base_init
import base_io
import base_search
import base_save_del

while True:
    choice = int(input("Choose the operation to do:\n0)end programm\n1)add new members to base;\n2)search for data in base;\n3)print base;\n4)delete all base;\n"))
    if choice ==0:
        break
    elif choice == 1:
        base_init.add_new_members()
        base_save_del.base_save_in_file()
        continue
    elif choice == 2:
        base_search.search_for_few_member()
        continue
    elif choice == 3:
        base_io.print_base()
        continue
    elif choice == 4:
        base_save_del.base_del_full()
        continue
    else:
        print("Make the existing choice please")