
# Soldier


from unittest import result


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage
        

# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon (Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War
class War(Viking, Saxon):
    def __init__(self):
        super(War,self).__init__()
        self.vikingArmy = list()
        self.saxonArmy = list()


    def addViking(self,VikingObject):
        self.vikingArmy.append(Viking(VikingObject))
    
    def addSaxon(self,SaxonObject):
        self.saxonArmy.append(Saxon(SaxonObject))

    def vikingAttack(self):
        from random import randint
        n_chosen_viking = randint(0,len(self.vikingArmy)-1)
        n_chosen_saxon = randint(0,len(self.saxonArmy)-1)

        chosen_viking = self.vikingArmy(n_chosen_viking)
        chosen_saxon = self.saxonArmy(n_chosen_saxon)

        chosen_saxon.receiveDamage(chosen_viking.strength)

        if chosen_saxon.health <= 0:
            self.vikingArmy.remove(n_chosen_viking)
        
        return f"result of calling {chosen_viking.strength} of a `Saxon``" 
    
    def saxonAttack(self):
        from random import randint
        n_chosen_viking = randint(0,len(self.vikingArmy)-1)
        n_chosen_saxon = randint(0,len(self.saxonArmy)-1)

        chosen_viking = self.vikingArmy(n_chosen_viking)
        chosen_saxon = self.saxonArmy(n_chosen_saxon)

        chosen_viking.receiveDamage(chosen_saxon.strength)

        if chosen_saxon.health <= 0:
            self.saxonArmy.remove(n_chosen_saxon)
        
        return f"result of calling {chosen_saxon.strength} of a `Viking`" 

    def showStatus(self):

        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else: 
            return "Vikings and Saxons are still in the thick of battle."



