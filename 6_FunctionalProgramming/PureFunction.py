# Pure function
def calculate_square(num):
    # Pure function with no side effects
    return num ** 2

# Example usage
result = calculate_square(5)
print(f"The square of 5 is: {result}")

#example 2
my_list=[1,2,3]
def addtolist(item):
    newlist=my_list.copy()
    newlist.append(item)     # my_list is not modified
    return newlist

new_list = addtolist(4)
print(f"Original list: {my_list}\nNew list after adding an item: {new_list}")   
