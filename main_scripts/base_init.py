from data_form import elems_of_base
from data_form import save_file_adress


def init_base():
    save_file = open(save_file_adress, "w")
    save_file.close()

def add_new_members(data_base):
    id = int(data_base[-1][0])+1
    new_data = ""
    while new_data.lower() != "end":
        name = ""
        surname = ""
        otchestvo = ""
        crim_case = ""
        status = ""
        details = ""
        members_args = [id, name, surname, otchestvo, crim_case, status, details]
        new_member = members_args
        for i in range (len(elems_of_base)-1):
            print("Enter " + elems_of_base[i+1] + " : ")
            new_data = input()
            if new_data.lower() == "end":
                break
            new_member[i+1] = new_data
        if new_data.lower() == "end":
            break
        data_base.append(new_member)

        print("Member " + new_member[1] + " was added to list\n")
        print("Type - end - to stop programm\n")