
from costumer import Customer
from bank import Bank


c1=Customer("ronen","gotliv",48)
b1=Bank(c1.fullName())
b1.Deposit(1000)
b1.withdrawal(500)
b1.withdrawal("200")
print(b1.totalAmount())