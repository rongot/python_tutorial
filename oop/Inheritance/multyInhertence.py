class Aquatic:
  def __init__(self,name):
    self.name = name

  def swim(self):
    return f"{self.name} is swimming"

  def greet(self):
    return f"I am {self.name} of the sea!"

class Ambulatory:
  def __init__(self,name):
    self.name = name

  def walk(self):
    return f"{self.name} is walking"

  def greet(self):
    return f"I am {self.name} of the land!"

class Penguin(Aquatic, Ambulatory):
  def __init__(self,name):
    super().__init__(name=name)

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

#       
Penguin.__mro__ 

# (<class 'multiple.Penguin'>, <class 'multiple.Aquatic'>, 
#  <class 'multiple.Ambulatory'>, <class 'object'>)

Penguin.mro() 

# [__main__.Penguin, __main__.Aquatic, __main__.Ambulatory, object]

help(Penguin) # best for HUMAN readability -> gives us a detailed chain 

