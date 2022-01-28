
# Soldier


from unicodedata import name


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strenght = strength

    def attack (self):
        return self.strength

    def receiveDamage (self, damage):
        self.damage = damage
        self.health -= damage




# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(self, health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage, name):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"{name} has received {damage} points of damage"
        else:
            return f"{name} has died in act of combat"
   
    def battleCry(self):
        return "ODIN OWNS YOU ALL"

    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(self, health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"A saxon has received {damage} points of damage"
        else:
            return "A saxon has died in combat"




# War


class War(Viking, Saxon):
    def __init__(self, name, health, strength):
        super().__init__(self, health, strength)

    vikingArmy = ""
    saxonArmy = ""   

    def addViking(Viking):
        Viking()

    def addSaxon(Saxon):
        Saxon()

    def vikingAttack(): 
        Saxon.receiveDamage(damage) -= attack(Viking)

    def saxonAttack():
        Viking.receiveDamage(damage, name)-= attack(Saxon)

    def showSatus():
        if saxonArmy == "":
            return "Vikings have won the war of the century"  
        elif vikingArmy == "":
            return "Saxons have won the war of the century"
        elif saxonArmy != "" and vikingArmy != "":
            return "Vikings and Saxons are still in the thick of battle"
            
                      














