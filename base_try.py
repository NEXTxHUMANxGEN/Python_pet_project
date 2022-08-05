

#This is first comment to try commits in VS

from urllib.request import parse_keqv_list


data_base = []

id = 0

# name = ""
# surname = ""
# otchestvo = ""
# crim_case = ""
# status = ""
# details = ""

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
        

#def search_for_member():
#    index_of_plate = input("Choose category for search :\n1 = id; 2 = name; 3 = surname; 4 = otchestvo; 5 = case number; 6 = status = details\n")
#    call_for_search = input()
#    if call_for_search is int:
#        for i in range(len(data_base)):
#            if call_for_search == data_base[i][index_of_plate-1]:
#                print("This is yout result :")
#                print(data_base[y])        
#                break
#    elif call_for_search is str:
#        for i in range(len(data_base)):
#            if call_for_search in data_base[i][index_of_plate-1]:
#                print("This is yout result :")
#                print(data_base[y])        
#                break
#    else:
#        print("Please, type right search info\n")


def search_for_member():
    index_of_plate = input("Choose category for search :\n1 = id; 2 = name; 3 = surname; 4 = otchestvo; 5 = case number; 6 = status = details\n")
    flag
    while flag != 1 or flag != 2:
        call_for_search = int(input())
        if call_for_search == str(call_for_search):
            flag = 2
            break
        elif call_for_search == int(call_for_search):
            flag = 1
            break
        else:
            print("Please, type right search info\n")
    if flag == 1:
        for i in range(len(data_base)):
            if call_for_search == data_base[i][index_of_plate-1]:
                print("This is yout result :")
                print(data_base[y])        
                break
    elif flag == 2:
        for i in range(len(data_base)):
            if call_for_search in data_base[i][index_of_plate-1]:
                print("This is yout result :")
                print(data_base[y])        
                break


#Вписываем строку - ищем в выбранной категории совпадение (либо везде), выводим только ту строку, где встречается совпадение


    # for i in range(len(data_base)):
    #     for y in range(len(data_base[i])):
    #         if call_for_search == data_base[y]:
    #             print("This is yout result :")
    #             print(data_base[y])        
    #             break
















