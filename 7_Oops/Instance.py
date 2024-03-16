class Payslips:
    def __init__(self,name,payment,amount) -> None:
        self.name=name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment="Yes"
        
    def status(self):
        if self.payment=="Yes":
            return self.name+" is paid "+str(self.amount)
        else:
            return self.name+" is not paid yet"
        

roger=Payslips("Roger", "Yes", 1500)
print(roger.status())
mark=Payslips("Mark","No",2345)
print(mark.status())
mark.pay()  # Mark gets paid
print(mark.status())