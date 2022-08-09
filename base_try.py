
#This is first comment to try commits in VS

data_base = []

id = 1

elems_of_base = ["id", "name", "surname", "otchestvo", "crim_case", "status", "details"]
# this is list of all elemnts in base for easier modification in future

def add_new_members():
    global id
    new_data = ""
    while new_data.lower() != "end":
        name = ""
        surname = ""
        otchestvo = ""
        crim_case = ""
        status = ""
        details = ""
        new_member = [id, name, surname, otchestvo, crim_case, status, details]
        i = 0
        for i in range (len(elems_of_base)-1):
            print("Enter " + elems_of_base[i+1] + " : ")
            new_data = input()
            if new_data.lower() == "end":
                break
            new_member[i+1] = new_data
        if new_data.lower() == "end":
            break
        data_base.append(new_member)
        id+=1
        print("Member " + new_member[1] + " was added to list\n")
        print("Type - end - to stop programm\n")




def print_base():
    print(elems_of_base)
    for z in range(len(data_base)):
        print(data_base[z])




def search_for_few_member():
    while True:
        index_of_plate = int(input("Choose category for search :\n1 = id; 2 = name; 3 = surname; 4 = otchestvo; 5 = case number; 6 = status; 7 = details\n"))
        if (index_of_plate == 1):
            id_tag = int(input("Type id for search : "))
            for i in range(len(data_base)):
                if data_base[i][0] == id_tag:
                    print(data_base[i])
                    break
            break
        elif ((index_of_plate > 1) and (index_of_plate < 8)):
            info_for_search = input("Type info for search : ")
            for i in range(len(data_base)):
                if info_for_search in data_base[i][index_of_plate-1]:
                    print(data_base[i])
            break
        else:
            print("Please, type choose existing category")
            continue




















