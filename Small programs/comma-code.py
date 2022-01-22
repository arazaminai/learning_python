def comma_code():
    lists = []

    print("Enter your list options(enter nothing to stop): ")

    while True:
        list_items = input(str(len(lists) + 1) + ") ")
        if list_items == "":
            break
        lists.append(list_items)

    list_print = str(lists[0:-1]).replace("[", "").replace("]", "").replace("'", "")
    #print(list_print + " and " + lists[-1])
    print("%s and %s" % (list_print, lists[-1]))

comma_code()