from costumer import Customer


class Bank:
    
    def __init__(self,mafkid) -> None:
        self._mafkid=mafkid
        self._amount=0

    def Deposit(self,value):
        if type(value) is not str or value < 0:
            self._amount +=value
        else:
            raise TypeError (f"{value} value is not correct")
    
    def withdrawal(self,value):
        
        if self._amount < 0:
            raise TypeError(f"you have {self._amount} no able to withdraw ")
        if type(value) is not int:
            raise TypeError(f" {value} is not correct")
        else:
             self._amount -=value
    def totalAmount(self):
        return f"{self._mafkid} has {self._amount}"

        
            
