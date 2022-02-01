# Juego
from ast import Try
import sys
import random
from traceback import print_stack
from vikingsClasses import War
from vikingsClasses import Viking
from vikingsClasses import Saxon

#import vikingsClasses as vc

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
for i in vik_mano:
    if i in vik_army:
        vik_army.remove(i)

# Construimos el ejercito sajon con 15 efectivos
sax_army = []
for i in range(0, 15):
    sax_army.append(Saxon(random.randint(1, 20), random.randint(1, 20)))


# Hacemos la mano de los sajones con 5 efectivos y asignamos un numero a cada uno
sax_mano = random.sample(sax_army, 5)
for i in sax_mano:
    if i in sax_army:
        sax_army.remove(i)

# class para la pelea
class AtaqueJugador:
    def __init__(self, player_army_name, computer_army_name, army_player, army_computer, reserve_player, reserve_computer, eleccion):
        self.player_army_name = player_army_name
        self.computer_army_name = computer_army_name
        self.army_player = army_player
        self.army_computer = army_computer
        self.reserve_player = reserve_player
        self.reserve_computer = reserve_computer
        self.eleccion = eleccion

        self.contador_1 = 0
        self.contador_2 = 0
        self.contador_3 = 5

    def ejercito_player(self):
        print(self.player_army_name)
        for i in self.army_player:
            print(self.army_player.index(i)+1, i.__dict__)       
        print('\n')
        return self.ejercito_com()

    def ejercito_com(self):
        print(self.computer_army_name)
        for i in self.army_computer:
            print(self.army_computer.index(i)+1, i.__dict__) 
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
        if self.army_computer == 0:
            return self.endGame()
        elif soldier_computer.health <= 0 and len(self.reserve_computer) > 0:
            self.army_computer.remove(soldier_computer)
            x = random.choice(self.reserve_computer)
            self.army_computer.append(x)
            self.reserve_computer.remove(x)
            if self.eleccion == 'V' and self.contador_3 > 0:
                self.grito = input('¿Quieres usar el grito de guerra? Si (s) No (n) ')
                if self.grito == 's':
                    self.contador_1 -= 1
                    self.contador_3 -= 1
                    print('Odin Owns You All!')
                    self.soldierChoice_1()
                else:
                    return self.endGame()
            return self.endGame()
        elif soldier_computer.health <= 0 and len(self.reserve_computer) == 0:
            self.army_computer.remove(soldier_computer)
            if self.eleccion == 'V' and self.contador_3 > 0:
                self.grito = input('¿Quieres usar el grito de guerra? Si (s) No (n) ')
                if self.grito == 's':
                    self.contador_1 -= 1
                    self.contador_3 -= 1
                    print('Odin Owns You All!')
                    self.soldierChoice_1()
                else:
                    return self.endGame()
            return self.endGame()
        else:
            if self.eleccion == 'V' and self.contador_3 > 0:
                self.grito = input('¿Quieres usar el grito de guerra? Si (s) No (n) ')
                if self.grito == 's':
                    self.contador_1 -= 1
                    self.contador_3 -= 1
                    print('Odin Owns You All!')
                    self.soldierChoice_1()
                else:
                    return self.endGame()
            return self.endGame()

    def endGame(self):
        if len(self.army_player) == 0 and len(self.army_computer) > 0:
            print(f'Los {self.computer_army_name} ganaron la batalla')
            return sys.exit()
        elif len(self.army_player) > 0 and len(self.army_computer) == 0:
            print(f'Los {self.player_army_name} ganaron la batalla')
            return sys.exit()
        else:
            if self.contador_2 -self.contador_1 == 0:
                return self.ejercito_player()
            else:
                return self.soldierChoice_2()

    def soldierChoice_2(self):
        player_choice = random.choice(self.army_computer)
        computer_choice = random.choice(self.army_player)
        return self.ataque_2(player_choice, computer_choice)

    def ataque_2(self, soldier_computer, soldier_player):
        self.contador_2 += 1
        soldier_player.receiveDamage(soldier_computer.strength)
        if self.army_player == 0:
            return self.endGame()
        if soldier_player.health <= 0 and len(self.reserve_player) > 0:
            self.army_player.remove(soldier_player)
            x = random.choice(self.reserve_player)
            self.army_player.append(x)
            self.reserve_player.remove(x)
            y = random.randint(0,1)
            if self.eleccion == 'S' and self.contador_3 > 0 and y == 0:
                self.contador_2 -= 1
                self.contador_3 -= 1
                print('Odin Owns You All!')
                self.soldierChoice_2()
            else:
                return self.endGame()
            return self.endGame()
        elif soldier_player.health <= 0 and len(self.reserve_player) == 0:
            self.army_player.remove(soldier_player)
            y = random.randint(0,1)
            if self.eleccion == 'S' and self.contador_3 > 0 and y == 0:
                self.contador_2 -= 1
                self.contador_3 -= 1
                print('Odin Owns You All!')
                self.soldierChoice_2()
            else:

                return self.endGame()
            return self.endGame()
        else:
            y = random.randint(0,1)
            if self.eleccion == 'S' and self.contador_3 > 0 and y == 0:
                self.contador_2 -= 1
                self.contador_3 -= 1
                print('Odin Owns You All!')
                self.soldierChoice_2()
            else:
                return self.endGame()
            return self.endGame()

def chooseArmy():

    eleccion = input('Elige si quieres los vikingos (V) o los sajones (S): ')
    if eleccion == 'V':
        ejer_jug = vik_army
        ejer_com = sax_army
        mano_jug = vik_mano
        mano_com = sax_mano
        player_army_name = 'Vikingos'
        computer_army_name = 'Sajones'
    else:
        ejer_jug = sax_army
        ejer_com = vik_army
        mano_jug = sax_mano
        mano_com = vik_mano
        player_army_name = 'Sajones'
        computer_army_name = 'Vikingos'
    return AtaqueJugador(player_army_name, computer_army_name, mano_jug, mano_com, ejer_jug, ejer_com, eleccion).ejercito_player()

print('1. Instrucciones\n2. Comenzar partida')
instorplay = int(input('¿Quieres ver las instrucciones (1) o empezar a jugar (2)? '))
if instorplay == 1:
    print("BARBARIAN'S CLASH\n\nUna guerra sin cuartel se ha desatado entre vikingos y sajones. Elige tu bando con 'V' o 'S'.")
    print('Dispondras de un total de 15 soldados si eliges los sajones y de 10 si te decantas por los vikingos, pero solo podras jugar con los 5 de la mano. Si muere uno, sera sustituido por otro del mazo tomado al azar.\n')
    print("Cada soldado tiene una cantidad de vida (health) y de fuerza de ataque (strenght). La fuerza de tu soldado será restada de la salud del soldado enemigo y si llega a 0, sera eliminado.\n")
    print('Tanto el soldado CON el que atacas como AL que atacas se eligen introduciendo su numero.\n')
    print("Pero... ¿Por que los vikingos estan en inferioridad numerica? ¡Porque tienen un grito de guerra! Si eliges usar el grito de guerra, tendras un turno extra, pero solo dispones de 5, ¡que Hugin y Munin te ayuden a elegir el mejor momento para utilizarlos!\n")
    jugarono = input('¿Te atreves a pelear? Si, ¡por Midgar! (s) No, soy un cobardica (n) ')
    if jugarono == 's':
        chooseArmy()
    else:
        sys.exit()
else:
    chooseArmy()