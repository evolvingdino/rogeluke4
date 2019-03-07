from random import randrange

class WorldSpace(object):
    world_object_list = ['forest', 'mountain', 'ocean', 'other']

    def __init__(self, row, col, world_array):
        self.row = row # Number of created lists
        self.col = col # Number of indexes inside of each row
        self.world_array = world_array

    def genSingle_Char(self, char, count):
        # 'genSingle_Char' = Generate single character world objects
        # Adds a number of random, specific characters to the world array.
        original_count = count
        while count != 0:
            row = randrange(len(self.world_array))
            column = randrange(len(self.world_array[0]))
            if self.world_array[row][column] == ' ':
                self.world_array[row][column] = char
                count -= 1

        print('Generated {} {}\'s...'.format(original_count, char))