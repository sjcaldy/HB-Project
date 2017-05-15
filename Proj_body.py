
#still needs: figure out hit (store +1 and add to hand)
#integrate scoring mechanism & print score
#integrate win decision

def deal():
    import random

    deck = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH", "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC", "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD", "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS", "JS", "QS", "KS"]

    random.shuffle(deck)

    return deck

deck = deal()

def hand():
    player_hand = []
    dealer_hand = []
    
    while len(player_hand) < 2:
        c = deck.pop()
        player_hand.append(c)

    while len(dealer_hand) < 2:
        d = deck.pop()
        dealer_hand.append(d)

    print "player"
    print player_hand
    print "dealer"
    print dealer_hand

    if len(player_hand) > 2:
        e = deck.pop()
        player_hand.append(e)
        
    if len(dealer_hand) > 2:
        f = deck.pop()
        dealer_hand.append(f)

def score(player_hand,dealer_hand):

    count_score = 0
    ace_count = 0

    for a in hand:
        if a[0] == "A":
            ace_count += 1
        
    for b in hand:
        if (b[0] == "J" or b[0] == "Q" or b[0] == "K" or b[0] == "T" and ace_count == 1) and len(hand) == 2:
            print "blackjack"
            break
            #win fxn

    for c in hand:    
        if (c[0] == "J" or c[0] == "Q" or c[0] == "K" or c[0] == "T"):
            count_score +=10
        elif (c[0] != "A"):
            count_score +=int(c[0])

    for c in hand:
        if (c[0] == "A"):
            if ace_count == 1 and count_score >= 10:
                count_score +=1
            else:
                count_score +=11
        
        
#print count_score

def hit_or_stay():

    decide = raw_input("hit or stay? ")
    
    if decide == "hit":
        hand()
    else:
        print "stay"
        #win or lose decision

def win_decision():

    #player_hand = [10,9]

    #dealer_hand = [10,10]

    if sum(player_hand) > 21:
    	print "Bust, dealer wins!"
    elif sum(dealer_hand) > 21:
        print "Dealer bust, you win!"
    elif sum(player_hand) > sum(dealer_hand):
        print "You win!"
    else:
        print "Dealer wins!"
    
def intro():

    initiate = raw_input("Would you like to play blackjack Y/N? ")

    if initiate == "Y":
        hand()
        #print player_hand + "Player"
        #print dealer_hand + "Dealer"
        #score(player_hand)
        #score(dealer_hand)
        hit_or_stay()
    else:
        print "OK"
    
intro()
