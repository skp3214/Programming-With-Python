# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination,count):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        count+=1
        return count

    # Recursive calls in which function calls itself
    count=hanoi(disks - 1, source, destination, helper,count)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    count+=1
    count=hanoi(disks - 1, helper, source, destination,count)
    return count

# Driver code
disks = int(input('Number of disks to be displaced: '))

# Actual function call
count=0
count=hanoi(disks, 'A', 'B', 'C',count)
print(count)