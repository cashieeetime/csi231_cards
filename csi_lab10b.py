import cards

# Create the deck of cards
def deal():
    the_deck = cards.Deck()
    #the_deck.shuffle()
    
    hand1_list=[]
    hand2_list=[]
    for i in range( 5 ):
        hand1_list.append( the_deck.deal() )
        hand2_list.append( the_deck.deal() )
    
    return hand1_list, hand2_list

def play_war(hand1_list, hand2_list):
    hand1_card = hand1_list.pop(0)
    hand2_card = hand2_list.pop(0)
    
    hand1_card_value = hand1_card.rank()
    hand2_card_value = hand2_card.rank()
    
    if hand1_card_value == 1:
        hand1_card_value = 15
    if hand2_card_value == 1:
        hand2_card_value = 15
    
    if hand1_card_value > hand2_card_value:
        hand1_list.append(hand1_card)
        hand1_list.append(hand2_card)
        return hand1_list, hand2_list, hand1_card, hand2_card, "Player 1"
    elif hand1_card_value < hand2_card_value:
        hand2_list.append(hand2_card)
        hand2_list.append(hand1_card)
        return hand1_list, hand2_list, hand1_card, hand2_card, "Player 2"
    elif hand1_card_value == hand2_card_value:
        hand1_list.append(hand1_card)
        hand2_list.append(hand2_card)
        return hand1_list, hand2_list, hand1_card, hand2_card, "Tie"

def main ():
    keep_going = True
    hand1_list, hand2_list = deal()
    
    print("Starting Hands")
    print("Hand1:", hand1_list)
    print("Hand2:", hand2_list)
    print()
        
    while keep_going:
        if len(hand1_list) == 0:
            break
        elif len(hand2_list) == 0:
            break
    
        hand1_list, hand2_list, hand1_card, hand2_card, winner = play_war(hand1_list, hand2_list)
    
        if winner == "Player 1":
            print("Battle was 1: {}, 2: {}. Player 1 wins battle.".format(
                  hand1_card, hand2_card)) 
            print("hand1:", hand1_list)
            print("hand2:", hand2_list)
        elif winner == "Player 2":
            print("Battle was 1: {}, 2: {}. Player 2 wins battle.".format(
                  hand1_card, hand2_card))
            print("hand1:", hand1_list)
            print("hand2:", hand2_list)
        elif winner == "Tie":
            print("Battle was 1: {}, 2: {}. Battle tied.".format(
                  hand1_card, hand2_card))
            print("hand1:", hand1_list)
            print("hand2:", hand2_list)
        
        if len(hand1_list) == 0 or len(hand2_list) == 0:
            keep_going = False
        else:    
            choice = input("Keep Going: (Nn) to stop:")
            if choice.lower() == "n":
                keep_going = False
                
        if keep_going == False:
            if len(hand1_list) > len(hand2_list):
                print("Player 1 wins!!!")
            elif len(hand1_list) < len(hand2_list):
                print("Player 2 wins!!!")
        
            
    
            

main()
