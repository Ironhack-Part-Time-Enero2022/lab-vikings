# Soldier

class Soldier:
    """
    Clase contiene tres funciones que definen las 
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
        Return:
            Devuelve la fuerza del soldado
        """
        return self.strength

    def receiveDamage(self, damage):
        """
        Resta de la salud del soldado los puntos de daño recibidos
        Arg:
            damage (int): numero que indica el daño recibido
        Method:
            self.health -= damage: resta de la salud del soldado 
                los puntos de daño recibidos
        """
        self.health -= damage
        return


# Viking

class Viking(Soldier):
    """
    Subclase de Soldier que contiene las caracteristicas 
    particulares de los soldados vikingos
    """
    def __init__(self, name, health, strength):
        """
        Define las caracteristicas del soldado vikingo
        Args:
            name (string): nombre del soldado
            health (int): vida inicial del soldado. Importado de Soldier
            strength (int): fuerza de ataque del soldado. Importado de Soldier
        """
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        """
        Nos la fuerza de ataque del soldado utilizando 
        la funcion attack() de Soldier
        Return:
            Devuelve la fuerza del soldado
        """
        return super().attack()

    def receiveDamage(self, damage):
        """
         Resta de la salud del soldado los puntos de daño recibidos
        Arg:
            damage (int): numero que indica el daño recibido
        Method
            self.health -= damage: resta de la salud del soldado 
                los puntos de daño recibidos
        Return:
            Si la salud del soldado es mayor que cero devuelve su nombre y el daño recibido
            Si la salud del soldado es menor o igual a cero indica que ha muerto
        """
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        """
        Grito de guerra vikingo
        Return:
            Imprime 'Odin Owns You All!'
        """
        return 'Odin Owns You All!'


# Saxon

class Saxon(Soldier):
    """
    Subclase de Soldier que contiene las caracteristicas 
    particulares de los soldados sajones
    """
    def __init__(self, health, strength):
        super().__init__(health, strength)
        """
        Define las caracteristicas del soldado vikingo
        Args:
            health (int): vida inicial del soldado. Importado de Soldier
            strength (int): fuerza de ataque del soldado. Importado de Soldier
        """

    def attack(self):
        """
        Nos la fuerza de ataque del soldado utilizando 
        la funcion attack() de Soldier
        Return:
            Devuelve la fuerza del soldado
        """
        return super().attack()

    def receiveDamage(self, damage):
        """
         Resta de la salud del soldado los puntos de daño recibidos
        Arg:
            damage (int): numero que indica el daño recibido
        Method:
            self.health -= damage: resta de la salud del soldado 
                los puntos de daño recibidos
        Return:
            Si la salud del soldado es mayor que cero devuelve el daño recibido
            Si la salud del soldado es menor o igual a cero indica que ha muerto
        """
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'


# War
import random

class War:
    """
    Clase que contiene dos ejercitos, uno vikingo y otro sajón, 
    y las reglas de la batalla
    """
    def __init__(self):
        """
        Contiene los dos ejercitos
        Atributes:
            vikingArmy (list): lista del ejercito vikingo
            saxonArmy (list): lista del ejercito sajon
        """
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        """
        Añade un soldado al ejercito vikingo
        Arg:
            Viking (obj): soldado de la clase Viking
        """    
        self.vikingArmy.append(Viking)
        return

    def addSaxon(self, Saxon):
        """
        Añade un soldado al ejercito sajon
        Arg:
            Saxon (obj): soldado de la clase Saxon
        """
        self.saxonArmy.append(Saxon)
        return

    def vikingAttack(self):
        """
        Condiciones del ataque vikingo
        Methods:
            vik: elige aleatoriamente un soldado del ejercito vikingo
            sax: elige aleatoriamente un soldado del ejercito sajon
            clash: resta al soldado sajon el daño recibido llamando 
                a la funcion receiveDamage de la subclase Saxon
            Si la salud del soldado es igual o menor a cero, 
            lo retira de la lista saxonArmy
        Return:
            Devuelve la salud que le quede al soldado sajon
        """
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)
        clash = sax.receiveDamage(vik.attack())
        if sax.health <= 0:
            self.saxonArmy.remove(sax)
        return clash

    def saxonAttack(self):
        """
        Condiciones del ataque sajon
        Methods:
            vik: elige aleatoriamente un soldado del ejercito vikingo
            sax: elige aleatoriamente un soldado del ejercito sajon
            clash: resta al soldado viquingo el daño recibido llamando 
                a la funcion receiveDamage de la subclase Viking
            Si la salud del soldado es igual o menor a cero, 
            lo retira de la lista vikingArmy
        Return:
            Devuelve la salud que le quede al soldado vikingo
        """
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)
        clash = vik.receiveDamage(sax.attack())
        if vik.health <= 0:
            self.vikingArmy.remove(vik)
        return clash

    def showStatus(self):
        """
        Indica el estado en el que se encuentra la batalla
        Return:
            Si el ejercito sajon se queda vacio da la victoria a los vikingos
            Si el ejercito vikingo se queda vacio da la victoria a los sajones
            Si ambos ejercitos tienen soldados indica que la batalla continua
        """
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
