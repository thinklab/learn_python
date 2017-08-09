#!/usr/bin/env python3

import random

card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
               'J', 'Q', 'K', 'A']
card_suits = ['♦', '♣', '♥', '♠']

card_costs = {
    '2': 2,
    '3': 3,
    '4': 4, 
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 4, 
    'Q': 3,
    'K': 2, 
    'A': 1    
    }
    
def get_random_card():
    cvalue = random.choice(card_values)
    csuite = random.choice(card_suits)
    cscore = get_card_score(cvalue)
    return cvalue + csuite, cscore 

def get_card_score(card):
    d = dict(card_costs)
    return d.get(card)

class MyDeckOfCards:
    def __init__(self):
        ...
    def __iter__(self):
        return MyDeckIterator()

class MyDeckIterator:
    def __init__(self):
        self.score = 0
    def __next__(self):
        if self.score > 21:
            print ("21!!!")        
            raise StopIteration()
        new_card, new_card_score = get_random_card()
        print (new_card, new_card_score)
        self.score += new_card_score  
        return new_card

if __name__ == '__main__':
   #print(random.choice(card_values) + random.choice(card_suits))
   print(list(MyDeckOfCards(0)))

