# Juego
import sys
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
    def __init__(self, player_army_name, computer_army_name, iterable_jug, iterable_com, army_player, army_computer, reserve_player, reserve_computer):
        self.player_army_name = player_army_name
        self.computer_army_name = computer_army_name
        self.iterable_jug = iterable_jug
        self.iterable_com = iterable_com
        self.army_player = army_player
        self.army_computer = army_computer
        self.reserve_player = reserve_player
        self.reserve_computer = reserve_computer

        self.contador_1 = 0
        self.contador_2 = 0

    def ejercito_player(self):
        print(self.player_army_name)
        for i in self.iterable_jug:
            print(i[0], i[1].__dict__)
            print('patata')
        print('\n')
        return self.ejercito_com()

    def ejercito_com(self):
        print(self.computer_army_name)
        for y in self.iterable_com:
            print(y[0], y[1].__dict__)
        print('\n')
        return self.soldierChoice_1()

    def soldierChoice_1(self):
        player_choice = int(input('Elige con que soldado quieres atacar: '))
        computer_choice = int(input('Elige a que soldado quieres atacar: '))
        player = self.army_player[player_choice-1]
        computer = self.army_computer[computer_choice-1]

        return self.ataque_1(player, computer)

    def ataque_1(self, soldier_player, soldier_computer):
        self.contador_1 += 1
        soldier_computer.receiveDamage(soldier_player.strength)
        if soldier_computer.health <= 0 and len(self.reserve_computer) > 0:
            self.army_computer.remove(soldier_computer)
            x = random.choice(self.reserve_computer)
            self.army_computer.append(x)
            self.reserve_computer.remove(x)
            return self.endGame()
        elif soldier_computer.health <= 0 and len(self.reserve_computer) == 0:
            self.army_computer.remove(soldier_computer)
            return self.endGame()
        else:
            return self.endGame()

    def endGame(self):
        if len(self.army_player) == 0 and len(self.army_computer) > 0:
            print(f'Los {self.computer_army_name} ganaron la batalla')
            return sys.exit()
        elif len(self.army_player) > 0 and len(self.army_computer) == 0:
            print(f'Los {self.computer_army_name} ganaron la batalla')
            return sys.exit()
        else:
            if self.contador_2 -self.contador_1 == 0:
                return self.ejercito_player()
            else:
                return self.soldierChoice_2()

    def soldierChoice_2(self):
        player_choice = random.choice(self.army_player)
        computer_choice = random.choice(self.army_computer)
        return self.ataque_2(player_choice, computer_choice)

    def ataque_2(self, soldier_player, soldier_computer):
        self.contador_2 += 1
        soldier_computer.receiveDamage(soldier_player.strength)
        if soldier_computer.health <= 0 and len(self.reserve_computer) > 0:
            self.army_computer.remove(soldier_computer)
            x = random.choice(self.reserve_computer)
            self.army_computer.append(x)
            self.reserve_computer.remove(x)
            return self.endGame()
        elif soldier_computer.health <= 0 and len(self.reserve_computer) == 0:
            self.army_computer.remove(soldier_computer)
            return self.endGame()
        else:
            return self.endGame()

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
        iterable_jug = vik_mano_1
        iterable_com = sax_mano_1
        player_army_name = 'Vikingos'
        computer_army_name = 'Sajones'
    else:
        ejer_jug = sax_army
        ejer_com = vik_army
        mano_jug = sax_mano
        mano_com = vik_mano
        iterable_jug = sax_mano_1
        iterable_com = vik_mano_1
        player_army_name = 'Sajones'
        computer_army_name = 'Vikingos'
    return AtaqueJugador(player_army_name, computer_army_name, iterable_jug, iterable_com, mano_jug, mano_com, ejer_jug, ejer_com).ejercito_player()

chooseArmy()