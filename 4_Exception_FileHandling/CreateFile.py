with open('newfile.txt',mode='w') as file:
    file.write("FIle created")

with open('newfile.txt',mode='a') as file:
    file.write("I am appended")