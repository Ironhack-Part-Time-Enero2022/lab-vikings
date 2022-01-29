
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack (self):
         return f'El/ella, tiene una fuerza de {self.strength}'

    def receivedamage (self):
        receivedamage= int(input("cuantos damage has recibido"))
        self.health -= receivedamage
    

# Viking


class Viking (Soldier):
    class Viking (Soldier):
        
    def __init__(self, nombre, health, strength):
        super().__init__(health, strength)

        self.nombre= nombre
        
    def receivedamage (self):
        receivedamage= int(input("cuantos damage has recibido"))
        self.health -= receivedamage
        if self.health > 0:
            return f'{self.nombre} has received {receivedamage} points of damage'
        if self.health < 0:
            return f'{self.nombre} has died in act of combat'
    
    def battleCry (self):
        return "Odin Owns You All!"

# Saxon


class Saxon (Soldier):
        
    def __init__(self, health, strength):
        super().__init__(health, strength)
        
    def receivedamage (self):
        receivedamage= int(input("cuantos damage has recibido"))
        self.health -= receivedamage
        if self.health > 0:
            return 'A Saxon has received {receivedamage} points of damage'
        if self.health < 0:
            return 'A Saxon has died in combat'


# War


class War:
    pass
