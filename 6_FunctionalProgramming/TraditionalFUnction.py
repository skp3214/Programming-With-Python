# Traditional function with side effects
def calculate_and_print_square(num):
    result = num ** 2
    print(f"The square of {num} is: {result}")
    # Modifying external state (printing to console)
    # No pure output, as it also has a side effect (printing)
    return result

# Example usage
calculate_and_print_square(5)

#Example 2
my_list=[1,2,3]
def addtolist(item):
    return my_list.append(item)  # my_list is manipulated
addtolist(4)
print(my_list)