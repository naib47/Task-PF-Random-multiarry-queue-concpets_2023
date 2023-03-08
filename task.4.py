""""rite a method which can create a multi die-mention array by getting number
of values of first list and number of values for the associative list, display the list as value in table formate"""

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
# Create an empty multi-dimensional array with the specified size

multi_array = [[None] * cols for i in range(rows)]

# Loop through each element in the multi-dimensional array and get the value from the user
for i in range(rows):
    for j in range(cols):
        multi_array[i][j] = input(
            "Enter the value for element at row " + str(i) + " and column " + str(j) + ": ")

# Print the multi-dimensional array
print("Multi-dimensional array:")
for i in range(rows):
    for j in range(cols):
        print(multi_array[i][j], end="\t")

print()
