class Recipe():
    # def __new__(cls:type[Self]) -> Self:
    #     pass
    def __init__(self,dish,items,time) -> None:
        self.dish=dish
        self.items=items
        self.time=time

    def contents(self):
        print(" The "+str(self.dish)+" has "+str(self.items)+\
              " and takes "+str(self.time)+" min to prepare")
        
pizza=Recipe("Pizza",["cheese","bread","tomato"],45)
pizza.contents()
