def add_to_top(val_2, list_2):
    list_2.insert(0, val_2)
    if len(list_2) > 5:
        list_2.pop()

    return list_2


list_2 = [12, 134, 13, 14, 44]
index_2 = int(input("Enter your index  for task 2::"))
val_2 = int(input("please enter value::"))

print(add_to_top(val_2, list_2))
