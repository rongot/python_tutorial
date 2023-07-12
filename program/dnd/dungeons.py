import random
class Dragon:
    
    def __init__(self) -> None:
       self.players=["first","second","third"]
       self.abilities=["strength", "dexterity", "constitution", "intelligence", "wisdom","charisma"] 

    def getRandomPlayer(self):
        return random.choice(self.players)
    def score(self):
        score=[]
        for n in range(0,4):
            score.append(random.randint(1,6))
        score.remove(min(score))
        return sum(score)
    def initialPlayer(self):
        points=self.getRandomPlayer()
        player=self.abilities[0]
        if points ==10:
            return player
        

       
        
         
 