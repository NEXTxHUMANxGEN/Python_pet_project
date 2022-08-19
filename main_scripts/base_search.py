
def search_for_few_member(data_base):
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
