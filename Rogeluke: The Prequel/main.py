import stats
from colors import *
from os import system

system('clear')
prRed('=========')
prRed('Stat Test')
prRed('=========')

mainstats = [
stats.Stat('Strength', stats.STR, 'main'),
stats.Stat('Dexterity', stats.DEX, 'main'),
stats.Stat('Constitution', stats.CON, 'main'),
stats.Stat('Intellect', stats.INT, 'main'),
stats.Stat('Luck', stats.LCK, 'main')
]

minorstats = [
stats.Stat('Medicine', stats.MDC),
stats.Stat('Lockpicking', stats.LPC),
stats.Stat('Alchemy', stats.ALC)
]

prGreen("\nHere are your main stats:\n")

for stat in mainstats:
    stats.Stat.printstat(stat, True)

prGreen("\nHere are your minor stats:\n")

for stat in minorstats:
    stats.Stat.printstat(stat, False)

print('')