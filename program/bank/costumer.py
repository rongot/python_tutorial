class Customer:
    count=0
    @classmethod
    def getCostumerAmount(cls):
        return cls.count
     
    def __init__(self,firstName:str,lastName:str,age:int) -> None:
        self._firstName=firstName
        self._lastName=lastName
        self._age=age
        Customer.count += 1
    @property
    def firstName(self):
        return self._firstName
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,newAge):
        if newAge> 0:
            self._age=newAge
        else:
            raise TypeError(f"{newAge} cant be under 0")

    def __repr__(self) -> str:
        return f"{self.firstName} {self._lastName} is added"
    
    def fullName(self):
        return f"{self._firstName} {self._lastName}"
    
    def is_senior(self):
        return self.age >= 65



    
# print(Customer.count)
# c1=Customer("ronen","gotliv",48)
# print(c1.firstName)
# c1.age=24
# print(c1.age)
# c2=Customer("moshe","mmm",23)
# print(Customer.getCostumerAmount())

