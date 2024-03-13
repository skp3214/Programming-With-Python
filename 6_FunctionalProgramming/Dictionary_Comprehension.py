# Dictionary comprehension
# The syntax for dictionary comprehension is:

# dict = { key:value for key, value in <sequence> if <condition> } 

# Dictionary comprehension takes one or two lists as input and creates a dictionary out of it. 
# I will now demonstrate how this can be done using only one list and by using two lists. 


using_range={x:x+1 for x in range(5)}
print("Using Range Function : ", using_range)

months=["jan","feb","march","april","may"]
number=[1,2,3,4,5]

number_dict={x:x**2  for x in number}
print(f"Number Dictionary {number_dict}")

number_month={x:y for x,y in zip(number, months)}
print(f"\nNumber and Month Dictionary {number_month}\n")


