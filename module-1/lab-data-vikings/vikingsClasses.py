import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage): 
        self.health -= damage
       

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health,strength)
        print(health,name,strength)

    def attack(self):
         return super().attack()
        
    def receiveDamage(self, damage):
       self.health -= damage

       if self.health > 0:
           return self.name + " has received " + str(damage) + " points of damage"
       else:
            return self.name + " has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
    

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)
        print(health,strength)
    
    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"
    

# War


class War:
    def __init__(self):
       self.vikingArmy = []
       self.saxonArmy  = []
    
    def addViking(self,viking):
        self.vikingArmy.append(viking)
        

    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
        
    
    def vikingAttack(self):
        randV = random.choice(self.vikingArmy)
        randS = random.choice(self.saxonArmy)
        saxon_result = randS.receiveDamage(randV.strength)

        if randS.health <= 0:
           self.saxonArmy.remove(randS)
        return saxon_result
        
    
    def saxonAttack(self):
        randV = random.choice(self.vikingArmy)
        randS = random.choice(self.saxonArmy)
        viking_result = randV.receiveDamage(randS.strength)

        if randV.health <= 0:
            self.vikingArmy.remove(randV)
        return viking_result
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    

#Battle
class InvalidValueError(Exception):
    '''Introduced number out of range (1,100)'''
    pass
def checkInvalidValueError(value):
    return value > 0 and value <= 100
        

war = War()

while True:

    try:
        saxonsNumber = int(input("The number of soldiers of the Saxon army is:"))
        break
    except ValueError:
        print("The input must be an integer.Please try again.")
    
attributes = input("Do you want to choose (introducing the number) the soldiers' health and strengh? (y/N)")

if attributes[0] == "y" or "Y":
    for s in range(0,saxonsNumber):
        print(f"soldier number {s}")
        while True:
            try:
                saxonHealth = int(input("Introduce the soldier's health choosing a number (1-100):"))
                saxonStrength = int(input("Introduce the soldier's strength choosing a number (1-100):"))
                if checkInvalidValueError(saxonHealth) == False or checkInvalidValueError(saxonStrength) == False:
                    raise InvalidValueError

                break
            except InvalidValueError:
                print("Please introduce a number between 1 and 100")
            except ValueError:
                print("The input must be an integer.Please try again.")
        saxon = Saxon(saxonHealth, saxonStrength)
        war.addSaxon(saxon)
elif attributes[0] == "n" or "N":
    for s in range(0,saxonsNumber):
        saxon = Saxon(random.randint(1,100), random.randint(1,100))
        war.addSaxon(saxon)


while True:
    try:
        vikingsNumber = int(input("The Vikings army is composed by these number of soldiers:"))
        break
    except ValueError:
        print("The input must be an integer.Please try again.")


for v in range(0, vikingsNumber):
  viking = Viking("Viking " + str(v), random.randint(1,100), random.randint(0,100))
  war.addViking(viking)



while len(war.saxonArmy) != 0 and len(war.vikingArmy) != 0 :
  try:
    print(war.saxonAttack())
    print(war.vikingAttack())
  except:
    print(war.showStatus())
  else:
    print(war.showStatus())
