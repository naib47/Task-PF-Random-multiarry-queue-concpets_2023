# def add_to_list(key, value, lst):
#     if len(lst) >= 10:
#         print("List is already full.")
#         return lst
#     for i, item in enumerate(lst):
#         if item[0] == key:
#             print("Key already exists. Please choose a different key.")
#             return lst

#     lst.append((value))
#     return lst


# my_list = []

# # Prompt user to enter key-value pairs until list is full or user enters 'q for resultant list'
# while len(my_list) < 10:
#     key = input("Enter a key (or 'q' to result): ")
#     if key == 'q':
#         break
#     value = input("Enter a value: ")
#     my_list = add_to_list(key, value, my_list)

# print("Final list:", my_list)

# 2nd method
def Check_list_add(index, val):
    # functions definations
    if list_1[index] is not None:
        print("This key is already filled.")
    else:
        list_1.insert(index, val)
        print("Value added successfully.")


# variable declarations for checkindexis filled functions
list_1 = [10, 2, 3, 4, 5, 6]
index = int(input("please enter the index:"))
val = int(input("please enter the value:"))
# functiona calling
Check_list_add(index, val)
# Rask 2
