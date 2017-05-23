#hand doesn't clear
#busts wrong time

def deal():
    
    import random

    deck = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH", "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC", "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD", "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS", "JS", "QS", "KS"]

    random.shuffle(deck)

    return deck

 # insert to intro section
deck = deal()
player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0

def hand(player_hand, dealer_hand):

    while len(dealer_hand) < 2:
        d = deck.pop()
        dealer_hand.append(d)

    while len(player_hand) < 2:
        c = deck.pop()
        player_hand.append(c)

    player_score = score(player_hand)
    print "PLAYER: " + str(player_score)
    print player_hand

    dealer_score = score(dealer_hand)
    print "DEALER: " + str(dealer_score)
    print dealer_hand

    
    hit_or_stay(player_hand)

def score(hand):

    count_score = 0
    ace_count = 0

    for a in hand:
        if a[0] == "A":
            ace_count += 1
        
    for b in hand:
        if ((b[0] == "J" or b[0] == "Q" or b[0] == "K" or b[0] == "T") and ace_count == 1) and len(hand) == 2:
            print player_hand
            print "Blackjack! You win"
            win_decision(player_hand, dealer_hand)

    for c in hand:    
        if (c[0] == "J" or c[0] == "Q" or c[0] == "K" or c[0] == "T"):
            count_score +=10
        elif (c[0] != "A"):
            count_score +=int(c[0])

    for c in hand:
        if (c[0] == "A"):
            if ace_count >= 1 and count_score >= 10:
                count_score +=1
            else:
                count_score +=11
        
        
    return count_score

def hit_or_stay(player_hand):

    decide = raw_input("hit or stay? ").lower()

    if decide == "hit":
        e = deck.pop()
        player_hand.append(e)
        player_score = score(player_hand)
        print "PLAYER: " + str(player_score)
        print player_hand
        if player_score > 21:
            win_decision(player_hand, dealer_hand)
        else:
            hit_or_stay(player_hand)
        
    else:
        print "stay"
        player_hand.append("0")
        player_score = score(player_hand)
        if dealer_score >= 17:
            win_decision(player_hand, dealer_hand)
        else:
            dealer(dealer_hand, player_hand)

def dealer(dealer_hand, player_hand):
    
    dealer_score = score(dealer_hand)
        
    if dealer_score < 17:
        f = deck.pop()
        dealer_hand.append(f)
        dealer_score = score(dealer_hand)
        print "DEALER: " + str(dealer_score)
        print dealer_hand
        dealer(dealer_hand, player_hand)

    if dealer_score >= 17 and "0" in player_hand:
        win_decision(player_hand, dealer_hand)

            
def win_decision(player_hand, dealer_hand):

    dealer_score = score(dealer_hand)
    player_score = score(player_hand)
    print "_________________________________"
    print "DEALER: " + str(dealer_score)
    print dealer_hand
    print "PLAYER: " +str(player_score)
    print player_hand
    if player_score == dealer_score:
        print "Draw"
    elif player_score > 21:
    	print "Bust, dealer wins!"
    elif dealer_score > 21:
        print "Dealer bust, you win!"
    elif player_score > dealer_score:
        print "You win!"
    else:
        print "Dealer wins!"

    intro()
    
def intro():

    #old hand not clearing out
    initiate = raw_input("Would you like to play blackjack Y/N? ").upper()

    if initiate == "Y":
        player_hand = []
        dealer_hand = []
        hand(player_hand, dealer_hand)
    else:
        print "OK"
        
    
intro()
