from random import choice, randint, shuffle
from statistics import mean


coin = choice(["heads", "tails"])

qbit = randint(1, 10)

cards = ["ten", "jack", "queen", "king", "ace"]
shuffle(cards)

#for card in cards:
#    print(card)
    
grades = mean([100, 90])
print(grades)
