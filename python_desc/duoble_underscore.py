class Human:
    def __init__(self, height,name="ronen"):
        self.height = height  # in inches
        self.name = name

    def __len__(self):
        return self.height
    def __repr__(self):
        return self.name
'''
Therefore, you can declare special methods on your own classes to mimic the behavior of builtin objects, like so using __len__:
'''
Colt = Human(60)
print(len(Colt))  # 60
print(Colt)  # "somebody"
