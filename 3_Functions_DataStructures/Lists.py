list1=[1,2,3,4,5]
list2=[1,'a','c',True,4]
print(list1[0])
list1.insert(len(list1),12)
print(list1.pop())
print(list1.append(7))
print(list1)
print(set(list1).union(set(list2)))  #Union operation returns set which contains unique elements from both lists.