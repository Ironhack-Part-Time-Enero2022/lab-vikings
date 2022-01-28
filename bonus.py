# Juego

import random
from vikingsClasses import War
from vikingsClasses import Viking
from vikingsClasses import Saxon

# Nombres para los vikingos
nombres_vik = ['Arne', 'Birger', 'Bjorn', 'Bo', 'Erik', 'Frode', 'Gorm', 
           'Halfdan', 'Harald', 'Knud', 'Kare', 'Leif', 'Njal', 'Roar',
           'Rune', 'Sten', 'Skarde', 'Sune', 'Svend', 'Troels', 'Toke',
           'Torsten', 'Trygve', 'Ulf', 'Odger', 'Age']
nombres_vik_army = random.sample(nombres_vik, 10)

# Construimos el ejercito vikingo con 10 efectivos
vik_army = []
for i in nombres_vik_army:
    vik_army.append(Viking(i, random.randint(1, 20), random.randint(1, 20)))

# Hacemos la mano de los vikingos con 5 efectivos y asignamos un numero a cada uno
vik_mano = random.sample(vik_army, 5)
num = range(1, 6)
vik_mano_1 = zip(num, vik_mano)
print('Vikings')
for i in vik_mano_1:
    print(i[0], i[1].__dict__)
print('\n')

# Construimos el ejercito sajon con 15 efectivos
sax_army = []
for i in range(0, 15):
    sax_army.append(Saxon(random.randint(1, 20), random.randint(1, 20)))

# Hacemos la mano de los sajones con 5 efectivos y asignamos un numero a cada uno
sax_mano = random.sample(sax_army, 5)
sax_mano_1 = zip(num, sax_mano)
print('Saxons')
for i in sax_mano_1:
    print(i[0], i[1].__dict__)
print('\n')

# class para el ataque del jugador
class AtaqueJugador:
    def __init__(self, army_player, army_computer, reserve_player, reserve_computer):
        self.army_player = army_player
        self.army_computer = army_computer
        self.reserve_player = reserve_player
        self.reserve_computer = reserve_computer

    def soldierChoice(self):
        player_choice = int(input('Elige con que soldado quieres atacar: '))
        computer_choice = int(input('Elige a que soldado quieres atacar: '))
        player = self.army_player[player_choice-1]
        computer = self.army_computer[computer_choice-1]

        return self.ataque(player, computer)

    def ataque(self, soldier_player, soldier_computer):
        soldier_computer.receiveDamage(soldier_player.strength)
        if soldier_computer.health <= 0 and len(self.reserve_computer) > 0:
            self.army_computer.remove(soldier_computer)
            x = random.choice(self.reserve_computer)
            self.army_computer.append(x)
            self.reserve_computer.remove(x)
            return AtaqueOrdenador(self.army_player, self.army_computer, self.reserve_player, self.reserve_computer).soldierChoice()
        elif soldier_computer.health <= 0 and len(self.reserve_computer) == 0:
            self.army_computer.remove(soldier_computer)
            return AtaqueOrdenador(self.army_player, self.army_computer, self.reserve_player, self.reserve_computer).soldierChoice()

class AtaqueOrdenador:
    def __init__(self, army_player, army_computer, reserve_player, reserve_computer):
        self.army_player = army_player
        self.army_computer = army_computer
        self.reserve_player = reserve_player
        self.reserve_computer = reserve_computer

    def soldierChoice(self):
        player_choice = random.choice(self.army_player)
        computer_choice = random.choice(self.army_computer)
        print('patata')
        return self.ataque(player_choice, computer_choice)

    def ataque(self, soldier_player, soldier_computer):
        soldier_computer.receiveDamage(soldier_player.strength)
        if soldier_computer.health <= 0 and len(self.reserve_computer) > 0:
            self.army_computer.remove(soldier_computer)
            x = random.choice(self.reserve_computer)
            self.army_computer.append(x)
            self.reserve_computer.remove(x)
        elif self.computer.health <= 0 and len(self.reserve_computer) == 0:
            self.army_computer.remove(soldier_computer)
        return AtaqueJugador.soldierChoice(self.army_player, self.army_computer, self.reserve_player, self.reserve_computer)

def chooseArmy():
    """
    Arroja el army_player, army_computer, el reserve_player y el reserve_computer
    """
    eleccion = input('Elige si quieres los vikingos (V) o los sajones (S): ')
    if eleccion == 'V':
        ejer_jug = vik_army
        ejer_com = sax_army
        mano_jug = vik_mano
        mano_com = sax_mano
    else:
        ejer_jug = sax_army
        ejer_com = vik_army
        mano_jug = sax_mano
        mano_com = vik_mano
    return AtaqueJugador(mano_jug, mano_com, ejer_jug, ejer_com).soldierChoice()

chooseArmy()

