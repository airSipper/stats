# roll x y-sided dice z times and get some stats
# set number of dice in Cup class
# set number of sides on die in Die class
# set number of rolls in main()

import random
from collections import Counter
from matplotlib import pyplot as plt


class Cup:
    """ a cup to hold some dice """
    def __init__(self):
        self.number_of_dice = 3
        self.dice = []

    def roll_dice(self):
        for die in self.dice:
            die.roll()

    def get_rolls(self):
        for die in self.dice:
            print("{}:{}".format(self.dice.index(die) + 1, die.rolls))

    def set_dice(self):
        for die in self.dice:
            die.set_nums()

    def setup(self):
        self.dice = [Die() for i in range(self.number_of_dice)]
        self.set_dice()

    def get_roll_count(self):
        for die in self.dice:
            die.roll_count()

class Die:
    """ class for a single die """
    def __init__(self):
        self.sides = 12
        self.numbers = []
        self.rolls = []
        self.rollcount = {}

    def set_nums(self):
        self.numbers = [i for i in range(1,self.sides+1)]

    def roll(self):
        a = random.choice(self.numbers)
        self.rolls.append(a)

    def roll_count(self):
        for i in range(1, self.sides +1):
            self.rollcount[i] = 0
        for k, v in Counter(self.rolls).items():
            self.rollcount[k] = v


def main():
    n_rolls = 1000
    cup = Cup()
    cup.setup()

    # roll the dice n times
    for i in range(n_rolls):
        cup.roll_dice()

    #cup.get_rolls()
    cup.get_roll_count()

    for die in cup.dice:
        a = []
        b = [i for i in range(1, cup.dice[0].sides +1)]
        x = die.rollcount

        for k, v in sorted(x.items()):
            a.append(x[k])

        fig,ax = plt.subplots()
        plt.bar(b,a)
        plt.title("dice {}".format(cup.dice.index(die)+1))
        plt.show()


main()
