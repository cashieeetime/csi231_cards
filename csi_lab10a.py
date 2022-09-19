##
## Demonstrate some of the operations of the Deck and Card classes
##
import cards

# Seed the random number generator to a specific value so every execution
# of the program uses the same sequence of random numbers (for testing).
import random
random.seed( 100 )

# Create a deck of cards
my_deck = cards.Deck()

# Shuffle the deck, then display it in 13 columns
my_deck.shuffle()
print( "===== shuffled deck =====" )
my_deck.display()

# Deal five cards to each player (alternating)
print( "Dealt five cards to each player (alternating)" )
print()

player1_list=[]
player2_list=[]
for i in range( 5 ):
    player1_list.append( my_deck.deal() )
    player2_list.append( my_deck.deal() )

# Display each player's cards and the cards still in the deck
print( "===== player #1 =====" )
print()
print( player1_list )
print()
print( "===== player #2 =====" )
print()
print( player2_list )
print()
print( "===== remaining cards in deck =====" )
my_deck.display()

# First card dealt to Player #1
player1_card = player1_list.pop( 0 )
print( "First card dealt to player #1:", player1_card )
print("Player #1 hand:", player1_list)

# First card dealt to Player #2
player2_card = player2_list.pop( 0 )
print( "First card dealt to player #2:", player2_card )
print("Player #2 hand:", player2_list)

# Compare the ranks of the two cards
print()
if player1_card.rank() == player2_card.rank():
    print( "Tie:", player1_card, "and", player2_card, "of equal rank" )
elif player1_card.rank() > player2_card.rank():
    print("Player #1 wins:", player1_card, "of higher rank than", player2_card)
else:
    print("Player #2 wins:", player2_card, "of higher rank than", player1_card)

# second card in player1_list
player1_card = player1_list.pop( 0 )
print("\nSecond card dealt to player #1: {}".format(player1_card))
print("Player #1 hand: {}".format(player1_list))

# second card in player2_list
player2_card = player2_list.pop( 0 )
print("\nSecond card dealt to player #2:", player2_card)
print("Player #2 hand: {}".format(player2_list))

# last cards for both hands
player1_card = player1_list.pop( -1 )
player2_card = player2_list.pop( -1 )
print("\nLast card in hand of player #1: {}".format(player1_card))
print("Last card in hand of player #2: {}".format(player2_card))

print()
if player1_card.rank() == player2_card.rank():
    print( "Tie:", player1_card, "and", player2_card, "of equal rank" )
elif player1_card.rank() > player2_card.rank():
    print(player1_card, "of higher rank than", player2_card)
else:
    print(player2_card, "of higher rank than", player1_card)