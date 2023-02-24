def check_and_add_value(random_numbers):
    new_value = input("Enter a new value to add to the list: ")
    if new_value in random_numbers:
        print("Value already in the list.")
    else:
        index_to_stop = len(random_numbers)
        random_numbers.append(new_value)
        while index_to_stop < len(random_numbers):
            print(random_numbers[:index_to_stop+1])
            index_to_stop += 1


random_numbers = [2, 3, 4, 5, 6, 7, 8]
# func call
check_and_add_value(random_numbers)
