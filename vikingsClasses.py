# Soldier

class Soldier:
    """
    Contiene tres funciones que definen las 
    características generales de los soldados
    """
    def __init__(self, health, strength):
        """
        Define la fuerza y vida del soldados
        Args:
            health (int): numero que indica la vida del soldado
            strength (int): numero que indica la fuerza de ataque del soldado
        """
        self.health = health
        self.strength = strength

    def attack(self):
        """
        Returns:
            Devuelve la fuerza del soldado
        """
        return self.strength

    def receiveDamage(self, damage):
        """
        """
        self.health -= damage
        return


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return super().attack()

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

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'


# War
import random

class War:
    def __init__(self):

        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):      
        self.vikingArmy.append(Viking)
        return

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        return

    def vikingAttack(self):
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)
        clash = sax.receiveDamage(vik.attack())
        if sax.health <= 0:
            self.saxonArmy.remove(sax)
        return clash

    def saxonAttack(self):
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)
        clash = vik.receiveDamage(sax.attack())
        if vik.health <= 0:
            self.vikingArmy.remove(vik)
        return clash

    def showStatus(self):
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0:
            #print(len(self.saxonArmy))
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
