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
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'
    
# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, v):
        self.vikingArmy.append(v)

    def addSaxon(self, s):
        self.saxonArmy.append(s)

    def vikingAttack(self):
        random_viking1 = random.choice(self.vikingArmy)
        random_saxon1 = random.choice(self.saxonArmy)
        a = random_saxon1.receiveDamage(random_viking1.attack())
        if random_saxon1.health <= 0:
            self.saxonArmy.remove(random_saxon1)
        return a

    def saxonAttack(self):
        random_viking2 = random.choice(self.vikingArmy)
        random_saxon2 = random.choice(self.saxonArmy)
        b = random_viking2.receiveDamage(random_saxon2.attack())
        if random_viking2.health <= 0:
            self.vikingArmy.remove(random_viking2)
        return b

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

