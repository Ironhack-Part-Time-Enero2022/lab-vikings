
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack (self):
        return self.strength
    
    def receiveDamage (self, damage):
        self.damage = damage
        self.health -= damage


# Viking


class Viking (Soldier):
    def __init__(self, name, health, strenght):
        super().__init__(health, strenght)
        self.name = name

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage

        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        
        else:
            return f'{self.name} has died in act of combat'
        
    def battleCry(self):
        return 'Odin Owns You All!'


    

# Saxon


class Saxon (Soldier):
    def __init__(self, health, strenght):
        super().__init__(health,strenght)
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage

        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'

    

# War


class War(Soldier):
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):

        import random #(https://www.delftstack.com/es/howto/python/python-randomly-select-from-list/)
        vikingatacante = random.choice(self.vikingArmy)
        saxonatacado = random.choice(self.saxonArmy)

        ataque = vikingatacante.attack() #Llamamos al ataque creado en Soldier
        dañosaxon = saxonatacado.receiveDamage(ataque) #Establecemos el daño producido a Saxon

        if saxonatacado.health <= 0:
            self.saxonArmy.remove(saxonatacado)
        
        return dañosaxon

    def saxonAttack(self):
        import random
        saxonatacante = random.choice(self.saxonArmy)
        vikingatacado = random.choice(self.vikingArmy)

        ataque = saxonatacante.attack() 
        dañoviking = vikingatacado.receiveDamage(ataque) #Establecemos el daño producido a Saxon

        if vikingatacado.health <= 0:
            self.vikingArmy.remove(vikingatacado)
        
        return dañoviking

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'

        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'

        else:
            return 'Vikings and Saxons are still in the thick of battle.'

    
