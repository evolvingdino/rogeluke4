from stats import *

class Player(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        self.descStats = {'name': None, 'race': None, 'class': None, 'description': None}

        self.health = 80+CON
        self.mana = 80+INT
        self.equip_load = 0
        self.level = 1

        self.strength = STR
        self.dexterity = DEX
        self.constitution = CON
        self.intellect = INT
        self.luck = LCK

        self.medicine = MDC
        self.lockpicking = LPC
        self.alchemy = ALC

        self.inventory = {'weapons': [], 'armors': [], 'rings': [], 'spells': [], 'gold': None, 'keys': []}

        self.equipment = {'weapon': None, 'armors': None, 'rings': []}

        self.directions = dict(w=(0, 1), s=(0, -1), d=(1, 0), a=(-1, 0))

    def movement(self):
        while True:
            movement_inp = input("""
            W. | Move North
            S. | Move South
            D. | Move East
            A. | Move West
            > """).lower()
            try:
                direction = self.directions[movement_inp]
            except KeyError:
                print('Not a valid command')
            else:
                self.x, self.y = self.x + direction[0], self.y + direction[1]
                break