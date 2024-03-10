def divideby(a,b):
    return a/b

print(divideby(10,2)) # 5.0
# print(divideby(8,0))  throws error ZeroDivisionError

# Exception handling  in Python

try:
   print(divideby(8,0))
except Exception as e:
   print("An error occurred:",e.__class__)
else:
   print("No errors")
finally:
   print("This is the end")