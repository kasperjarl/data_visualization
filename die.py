from time import sleep
from random import randint

class Die:
    """ A class representing a die """

    def __init__(self, num_sides=6) -> None:
        # Default sides = 6
        self.num_sides = num_sides
        self.results = []

    def roll(self):
        """ return a random value between 1 and num_sides"""
        return(randint(1, self.num_sides))
    
    def store_results(self, num_throws=10):
        # Default throws = 10
        while num_throws > len(self.results):
            self.results.append(self.roll())

    def frequencies(self):
        frequencies = []
        poss_results = range(1, self.num_sides+1)
        for value in poss_results:
            frequencies.append(self.results.count(value))
        return frequencies
        

    def show_results(self):
        print(self.results)
        