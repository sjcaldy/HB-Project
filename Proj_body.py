
#figure out hit (store +1 and add to hand)
#score fxn work with win decision and dealer stay at 17
#win fxn broken

def deal():
    import random

    deck = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH", "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC", "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD", "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS", "JS", "QS", "KS"]

    random.shuffle(deck)

    return deck

deck = deal()
player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0

def hand(player, dealer):
    #deal cards (2 first, then 1 by 1)
    #can this be cleaned up?

    while len(dealer) < 2:
        d = deck.pop()
        dealer_hand.append(d)

    while len(player) < 2:
        c = deck.pop()
        player_hand.append(c)

    print "DEALER"
    print dealer_hand
    dealer_score = score(dealer_hand)

    print "PLAYER"
    print player_hand
    player_score = score(player_hand)
    
    #return player_score
    #return dealer_score
    hit_or_stay()

    """if len(player_hand) >= 2:
        e = deck.pop()
        player_hand.append(e)
        print player_hand   
    if len(dealer_hand) >= 2: #and score <17
        f = deck.pop()
        dealer_hand.append(f)"""


def score(hand):

    count_score = 0
    ace_count = 0

    for a in hand:
        if a[0] == "A":
            ace_count += 1
        
    for b in hand:
        if ((b[0] == "J" or b[0] == "Q" or b[0] == "K" or b[0] == "T") and ace_count == 1) and len(hand) == 2:
            print "Blackjack!"
            break
            win_decision()

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
        
        
    print count_score

def hit_or_stay():

    decide = raw_input("hit or stay? ").lower()
    
    if decide == "hit":
        print "DEALER"
        f = deck.pop()
        dealer_hand.append(f)
        print dealer_hand
        print "PLAYER"
        e = deck.pop()
        player_hand.append(e)
        print player_hand
    else:
        print "stay"
        win_decision()

def win_decision():

    #draw option also

    if player_score > 21:
    	print "Bust, dealer wins!"
    elif dealer_score > 21:
        print "Dealer bust, you win!"
    elif player_score > dealer_score:
        print "You win!"
    else:
        print "Dealer wins!"
    intro()
    
def intro():

    initiate = raw_input("Would you like to play blackjack Y/N? ").upper()

    if initiate == "Y":
        hand(player_hand, dealer_hand)
        hit_or_stay()
    else:
        print "OK"
        #weirdness here
        
    
intro()
