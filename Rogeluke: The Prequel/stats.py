import math
from random import randint
from colors import *

STR = randint(6, 18)
DEX = randint(6, 18)
CON = randint(6, 18)
INT = randint(6, 18)
LCK = randint(6, 18)

STRmod = math.floor((STR - 10) / 2)
DEXmod = math.floor((DEX - 10) / 2)

MDC = math.floor(10 + (INT / 8 + DEX / 15 + LCK / 10) * 3)
LPC = math.floor(10 + (DEX / 8 + LCK / 10) * 3)
ALC = math.floor(10 + (INT / 8 + CON / 15 + LCK / 10) * 3)

if DEXmod > STRmod:
    DXF = math.floor(10 + (DEX / 8 + STR / 30 + INT / 20 + LCK / 10) * 3)
    SRF = math.floor(5 + (STR / 8 + DEX / 30 + INT / 20 + LCK / 10) * 2)
elif STRmod > DEXmod:
    DXF = math.floor(5 + (DEX / 8 + STR / 30 + INT / 20 + LCK / 10) * 2)
    SRF = math.floor(10 + (STR / 8 + DEX / 30 + INT / 20 + LCK / 10) * 3)
else:
    DXF = math.floor(10 + (DEX / 8 + STR / 30 + INT / 20 + LCK / 10) * 3)
    SRF = math.floor(10 + (STR / 8 + DEX / 30 + INT / 20 + LCK / 10) * 3)


class Stat:
    """
    An empty stat template with the default grade of minor.
    """

    def __init__(self, name, formula, grade='minor'):
        self.name = name
        self.formula = formula
        self.modifier = math.floor((formula - 10) / 2)
        self.grade = grade


        if grade == 'main':

            self.yellowval= 6
            self.lgval= 9
            self.greenval= 11
            self.purpleval= 19

        elif grade == 'minor':

            self.yellowval= 9
            self.lgval= 12
            self.greenval= 19
            self.purpleval= 29

    def printstat(self, printmod=False):

        def _colorgrade(yellowval, lgval, greenval, purpleval,):

             if self.formula > purpleval:
                 if printmod is True:
                     prPurple('{1} {0} ({2})'.format(self.formula, self.name, self.modifier))
                 elif printmod is False:
                     prPurple('{1} {0}'.format(self.formula, self.name))
             elif self.formula > greenval:
                 if printmod is True:
                     prGreen('{1} {0} ({2})'.format(self.formula, self.name, self.modifier))
                 elif printmod is False:
                     prGreen('{1} {0}'.format(self.formula, self.name))
             elif self.formula > lgval:
                 if printmod is True:
                     prLightGray('{1} {0} ({2})'.format(self.formula, self.name,
 self.modifier))
                 elif printmod is False:
                     prLightGray('{1} {0}'.format(self.formula, self.name))
             elif self.formula > yellowval:
                 if printmod is True:
                     prYellow('{1} {0} ({2})'.format(self.formula, self.name, self.modifier))
                 elif printmod is False:
                     prYellow('{1} {0}'.format(self.formula, self.name))
             else:
                 if printmod is True:
                     prRed('{1} {0} ({2})'.format(self.formula, self.name, self.modifier))
                 elif printmod is False:
                     prRed('{1} {0}'.format(self.formula, self.name))

        _colorgrade(self.yellowval, self.lgval, self.greenval, self.purpleval)