def sum_of(*args):  #args
    sum=0
    for i in args:
        sum+=i
    return sum

print(sum_of(4,5,6))

def sumof(**kwargs):   #kwargs
    total = 0
    for key in kwargs.keys():
        total += kwargs[key]
    return total

print(sumof(a=1,b=2,c=3))