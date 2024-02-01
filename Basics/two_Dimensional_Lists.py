matrix = [
    [1,2,3], ####### innerlist index is 0
    [4,5,6], ####### innerlist index is 1
    [7,8,9]  ####### innerlist index is 2
]
print(matrix [0][0]) ### first bracjet is for first innerlist
matrix[0][0] = 12 ##### here we are changing the vale in list form index 0
print(matrix [0][0])
print(matrix [1][0])
print(matrix [2][0])

for row in matrix:
    for numbers in row:
        print(numbers)
matrix.append([10,11,12]) ###### to add a new innerlist to the list
print(matrix)
