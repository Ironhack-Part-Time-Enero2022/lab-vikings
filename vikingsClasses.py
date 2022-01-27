import random 
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
#metodo1
    def attack(self):
        return self.strength
#metodo2
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    def battleCry(self):
        return "Odin Owns You All!"
# Saxon
class Saxon(Soldier):    
    def __init__(self, health, strength):
        super().__init__(health, strength)
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return 'A Saxon has died in combat'    
# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    #addvkingmethod
    def addViking(self, Viking):
            self.vikingArmy.append(Viking)
            
    def addSaxon(self, Saxon):
            self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        fighter_v = random.choice(self.vikingArmy)
        fighter_s = random.choice(self.saxonArmy)
        att = fighter_s.receiveDamage(fighter_v.attack())
        if fighter_s.health <= 0:
            self.saxonArmy.remove(fighter_s)
        return att
       
    def saxonAttack(self):
        fighter_v2 = random.choice(self.vikingArmy)
        fighter_s2 = random.choice(self.saxonArmy)
        dec = fighter_v2.receiveDamage(fighter_s2.attack())
        if fighter_v2.health <= 0:
            self.vikingArmy.remove(fighter_v2)
        return dec
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return ("Vikings have won the war of the century!")
        elif len(self.vikingArmy) == 0:
            return ("Saxons have fought for their lives and survive another day...")
        else:
            return ("Vikings and Saxons are still in the thick of battle.")
