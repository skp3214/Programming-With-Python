class Employees:
    def __init__(self,name,last) -> None:
        self.name=name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chef(Employees):
    def leave_request(self,days):
        return "May I take a leave for"+str(days)+"days"

# Testing the code
sachin = Supervisors("John", "Doe", "123")
sameer=Chef("Sameer","Srivastava")
print(sameer.leave_request(3))