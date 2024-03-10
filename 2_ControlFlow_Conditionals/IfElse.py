bill_total=114
discount=10

if bill_total>100:
    print("Bill is greater than 100")
    bill_total=bill_total-discount
elif bill_total<10:
    print("Bill is lesser than 10")
else:
    print("Bill is between 10 and 100")
    
print("The total amount after discount is :",bill_total)
print("total bill: "+str(bill_total))