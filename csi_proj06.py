##################################################################
#    Computer Project 6
#    
#    Algorithm
#        initialize functions to play the poker game
#        deal out cards
#        search through possible hands to find the winning hand
#        print out winner
#        ask to play again
##################################################################
import cards

def less_than(c1, c2):
    '''Return 
           True if c1 is smaller in rank, 
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False
    
def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i, c in enumerate(L):
        if less_than(c,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index
        
def cannonical(H):
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for i,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
    return H

def flush_7(H):
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards, 
       False otherwise.'''
    clubs_list = []
    diamonds_list = []
    hearts_list = []
    spades_list = []
    
    for card in H:
        suite = card.suit()
        if suite == 1:
            clubs_list.append(card)
        elif suite == 2:
            diamonds_list.append(card)
        elif suite == 3:
            hearts_list.append(card)
        elif suite == 4:
            spades_list.append(card)
    
    if len(clubs_list) >= 5:
        clubs_list = clubs_list[:5]
        return clubs_list
    elif len(diamonds_list) >= 5:
        diamonds_list = diamonds_list[:5]
        return diamonds_list
    elif len(hearts_list) >= 5:
        hearts_list = hearts_list[:5]
        return hearts_list
    elif len(spades_list) >= 5:
        spades_list = spades_list[:5]
        return spades_list
    else: 
        return False

def straight_7(H):
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards, 
       False otherwise.'''
    count = 0
    hand = cannonical(H)
    temp_hand = []
    
    for card in hand:
        try:
            rank1 = card.rank()
            rank2 = hand[count + 1].rank()
            if rank2 == (rank1 + 1):
                temp_hand.append(card)
            count += 1
        except IndexError:
            continue

    if len(temp_hand) >= 5:
        temp_hand = temp_hand[:5]
        return temp_hand
    else:
        return False

def straight_flush_7(H):
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.'''
    cards_dict = {}
    for card in H:
        suite = card.suit()
        if suite == 1:
            if suite not in cards_dict.keys():
                cards_dict[suite] = [card]
            else:
                cards_dict[suite].append(card)
                
        elif suite == 2:
            if suite not in cards_dict.keys():
                cards_dict[suite] = [card]
            else:
                cards_dict[suite].append(card)
        
        elif suite == 3:
            if suite not in cards_dict.keys():
                cards_dict[suite] = [card]
            else:
                cards_dict[suite].append(card)
        
        elif suite == 4:
            if suite not in cards_dict.keys():
                cards_dict[suite] = [card]
            else:
                cards_dict[suite].append(card)
    
    temp_hand = []
    for key in cards_dict.keys():
        if len(cards_dict[key]) >+ 5:
            count = 0
            hand = cannonical(H)
            
            for card in hand:
                try:
                    rank1 = card.rank()
                    rank2 = hand[count + 1].rank()
                    if rank2 == (rank1 + 1):
                        temp_hand.append(card)
                    count += 1
                except IndexError:
                    continue
        
    if len(temp_hand) >= 5:
        temp_hand = temp_hand[:5]
        return temp_hand
    else:
        return False

def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.'''
    cards_dict = {}
    
    for card in H:
        rank = card.rank()
        if rank not in cards_dict.keys():
            cards_dict[rank] = [card]
        else:
            cards_dict[rank].append(card)
    
    for key in cards_dict.keys():
        if len(cards_dict[key]) == 4:
            return cards_dict[key]
    
    return False

def three_7(H):
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
    cards_dict = {}
    
    for card in H:
        rank = card.rank()
        if rank not in cards_dict.keys():
            cards_dict[rank] = [card]
        else:
            cards_dict[rank].append(card)
    
    for key in cards_dict.keys():
        if len(cards_dict[key]) == 3:
            return cards_dict[key]
        
    return False
        
def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H) and three_7(H) are both False.'''
    cards_dict = {}
    temp_list = []
    count = 0
    for card in H:
        rank = card.rank()
        if rank not in cards_dict.keys():
            cards_dict[rank] = [card]
        else:
            cards_dict[rank].append(card)
    
    for key in cards_dict.keys():
        if len(cards_dict[key]) == 2:
            for item in cards_dict[key]:
                temp_list.append(item)
                    
    if len(temp_list) == 4:
        return temp_list
    else:
        return False
            
def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    cards_dict = {}
    count = 0
    for card in H:
        rank = card.rank()
        if rank not in cards_dict.keys():
            cards_dict[rank] = [card]
        else:
            cards_dict[rank].append(card)
    
    for key in cards_dict.keys():
        if len(cards_dict[key]) == 2:
            count += 1
            index = key
            
    if count == 1:
        return cards_dict[index]
    else:
        return False

def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''    
    three_of_a_kind = three_7(H)
    one_pair = one_pair_7(H)
    temp_list = []
    
    if three_of_a_kind != False and one_pair != False:
        for item in three_of_a_kind:
            temp_list.append(item)
        for item in one_pair:
            temp_list.append(item)
        return temp_list
    else:
        return False 
               
def main():
    play_again = True
    D = cards.Deck()
    D.shuffle()
       
    while play_again:
        hand_1_list = [] # two cards dealt to player 1
        hand_2_list = [] # two cards dealt to player 2
        community_list = [] # five cards in the community pool
        cardlist_1 = [] # seven cards, holds hand 1 and community pool
        cardlist_2 = [] # seven cards, holds hand 2 and community pool
        for y in range(0,9):
            if y < 5:
                card = D.deal()
                community_list.append(card)
                cardlist_1.append(card)
                cardlist_2.append(card)
            if y == 5 or y == 6:
                card = D.deal()
                hand_1_list.append(card)
                cardlist_1.append(card)
            if y == 7 or y == 8:
                card = D.deal()
                hand_2_list.append(card)
                cardlist_2.append(card)
            
    
        print("-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",hand_1_list)
        print("Player 2:",hand_2_list)
        print()
        
        if straight_flush_7(cardlist_1) != False and \
            straight_flush_7(cardlist_2) == False:
            print("Player 1 wins with a straight flush: {}"
                  .format(straight_flush_7(cardlist_1)))
        
        elif straight_flush_7(cardlist_1) == False and \
            straight_flush_7(cardlist_2) != False:
            print("Player 2 wins with a straight flush: {}"
                  .format(straight_flush_7(cardlist_2)))
        
        elif straight_flush_7(cardlist_1) != False and \
            straight_flush_7(cardlist_2) != False:
            print("TIE with a straight flush: {}"
                  .format(straight_flush_7(cardlist_1)))
        
        
        elif four_7(cardlist_1) != False and four_7(cardlist_2) == False:
            print("Player 1 wins with four of a kind: {}"
                  .format(four_7(cardlist_1)))
        
        elif four_7(cardlist_1) == False and four_7(cardlist_2) != False:
            print("Player 2 wins with a four of a kind: {}"
                  .format(four_7(cardlist_2)))
        
        elif four_7(cardlist_1) != False and four_7(cardlist_2) != False:
            print("TIE with four of a kind: {}".format(four_7(cardlist_1)))
        
        
        elif full_house_7(cardlist_1) != False and \
            full_house_7(cardlist_2) == False:
            print("Player 1 wins with a full house: {}"
                  .format(full_house_7(cardlist_1)))
        
        elif full_house_7(cardlist_1) == False and \
            full_house_7(cardlist_2) != False:
            print("Player 2 wins with a full house: {}"
                  .format(full_house_7(cardlist_2)))
        
        elif full_house_7(cardlist_1) != False and \
            full_house_7(cardlist_2) != False:
            print("TIE with a full house: {}".format(full_house_7(cardlist_1)))
        
        
        elif flush_7(cardlist_1) != False and flush_7(cardlist_2) == False:
            print("Player 1 wins with a flush: {}".format(flush_7(cardlist_1)))
        
        elif flush_7(cardlist_1) == False and flush_7(cardlist_2) != False:
            print("Player 2 wins with a flush: {}".format(flush_7(cardlist_2)))
        
        elif flush_7(cardlist_1) != False and flush_7(cardlist_2) != False:
            print("TIE with a flush: {}".format(flush_7(cardlist_1)))
        
        
        elif straight_7(cardlist_1) != False and \
            straight_7(cardlist_2) == False:
            print("Player 1 wins with a straight: {}"
                  .format(straight_7(cardlist_1)))
        
        elif straight_7(cardlist_1) == False and \
            straight_7(cardlist_2) != False:
            print("Player 2 wins with a straight: {}"
                  .format(straight_7(cardlist_2)))
        
        elif straight_7(cardlist_1) != False and \
            straight_7(cardlist_2) != False:
            print("TIE with a straight: {}".format(straight_7(cardlist_1)))
        
        
        elif three_7(cardlist_1) != False and three_7(cardlist_2) == False:
            print("Player 1 wins with a three of a kind: {}"
                  .format(three_7(cardlist_1)))
        
        elif three_7(cardlist_1) == False and three_7(cardlist_2) != False:
            print("Player 2 wins with a three of a kind: {}"
                  .format(three_7(cardlist_2)))
        
        elif three_7(cardlist_1) != False and three_7(cardlist_2) != False:
            print("TIE with a three of a kind: {}".format(three_7(cardlist_1)))
        
        
        elif two_pair_7(cardlist_1) != False and \
            two_pair_7(cardlist_2) == False:
            print("Player 1 wins with a two pair: {}"
                  .format(two_pair_7(cardlist_1)))
        
        elif two_pair_7(cardlist_1) == False and \
            two_pair_7(cardlist_2) != False:
            print("Player 2 wins with a two pair: {}"
                  .format(two_pair_7(cardlist_2)))
        
        elif two_pair_7(cardlist_1) != False and \
            two_pair_7(cardlist_2) != False:
            print("TIE with two pairs: {}".format(two_pair_7(cardlist_1)))
        
        
        elif one_pair_7(cardlist_1) != False and \
            one_pair_7(cardlist_2) == False:
            print("Player 1 wins with one pair: {}"
                  .format(one_pair_7(cardlist_1)))
        
        elif one_pair_7(cardlist_1) == False and \
            one_pair_7(cardlist_2) != False:
            print("Player 2 wins with one pair: {}"
                  .format(one_pair_7(cardlist_2)))
        
        elif one_pair_7(cardlist_1) != False and \
            one_pair_7(cardlist_2) != False:
            print("TIE with one pair: {}".format(one_pair_7(cardlist_1)))
        
        
        else:
            hand1 = cannonical(cardlist_1)
            hand2 = cannonical(cardlist_2)
            if hand1[-1].rank() > hand2[-1].rank():
                print("Player 1 wins with the high card: {}".format(hand1[-1]))
            elif hand1[-1].rank() < hand2[-1].rank():
                print("Player 2 wins with the high card: {}".format(hand2[-1]))
            elif hand1[-1].rank() == hand2[-1].rank():
                print("TIE with the high card: {}".format(hand1[-1]))
                
        if len(D) < 9:
            play_again = False
            print("Deck has too few cards so game is done.")
            break
        
        choice = input("\nDo you wish to play another hand?(Y or N) ")
        if choice.upper() == "N":
            play_again = False
    


if __name__ == "__main__":
    main()