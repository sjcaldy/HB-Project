#here goes game invite prompt

def deck():
    import random

    deck = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"]

    random.shuffle(deck)

    player_hand = []

    # if len(player_hand) < 2: (for initial draw)
        
    card = deck.pop()
    player_hand.append(card)
    print player_hand

def hit_or_stay():

    decide = raw_input("hit or stay? ")
    
    if decide == "hit":
        deck()
    else:
        print "stay"

def deal():

    initiate = raw_input("Would you like to play blackjack Y/N? ")

    if initiate == "Y":
        deck()
        deck()
        hit_or_stay()
    else:
        print "OK"
    
deal()

#need:
#Computer player
#Scoring mechanism
#Final win/loss message
