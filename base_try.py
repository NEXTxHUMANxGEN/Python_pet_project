




#This is first comment to try commits in VS
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

new_data = ""

while new_data != "end":
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
        if new_data == "end":
            break
        new_member[i+1] = new_data
    if new_data == "end":
        break
    data_base.append(new_member)
    id+=1
    print("Member " + new_member[1] + " was added to list\n")
    print("Type - end - to stop programm\n")

print(elems_of_base)
for z in range(len(data_base)):
    print(data_base[z])
    

