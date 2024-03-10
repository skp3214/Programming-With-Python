file=open('D:/Lovely Professional University/Educational/Programming-With-Python/4_Exception_FileHandling/test.txt',mode='r')
# data=file.readline()
file.close()
with open('D:/Lovely Professional University/Educational/Programming-With-Python/4_Exception_FileHandling/test.txt',mode='r') as file:
    data=file.readline()

print(data)
print(type(data))

