"""
From previous CMSC201 Project
  Attempting to recreate first project from CMSC201

Cannot use dictionaries

            BLACKJACK
By: Christian De Guzman
Code done from Online Compiler
"""
import random

#create a deck function
def create_deck(deck, retrievers, num_decks):
  card_sym = ['\u2660', '\u2663', '\u2661', '\u2662']
  card_val = ['2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K", "A"]
  
  for value in card_val: #adding value and symbol to card
    for symbol in card_sym:
      card = value + symbol
      deck.append(card)
  
  deck *= num_decks #< -- making the amount of decks inputted by user
  
  if retrievers != 0: #adding retriever cards
    for i in range(retrievers):
      deck.append("R")
      
  return deck

#shuffles the deck
def shuffle_deck(deck):
  random.shuffle(deck)
  print(deck) #< -- cannot be in the final product, but it's here for checking

#quatloos bet function
def get_bet(bet):#<-- tested and it works
    quatloos = 100
    bet = int(input(f"You have {quatloos}, how many would you like to bet? "))
    quatloos -= bet
    return quatloos 

#deal cards to player
def deal_cards_player(deck, player_hand): #<-- tested and it works
  if not player_hand:
    player_hand.append(deck[0])
    deck.remove(deck[0])
    player_hand.append(deck[0])
    deck.remove(deck[0])
  else:
    player_hand.append(deck[0])
    deck.remove(deck[0])
  
  return player_hand

#deal cards to player
def deal_cards_comp(deck, computer_hand): #<-- tested and it works
  if not computer_hand:
    computer_hand.append(deck[0])
    deck.remove(deck[0])
    computer_hand.append(deck[0])
    deck.remove(deck[0])
  else:
    computer_hand.append(deck[0])
    deck.remove(deck[0])
  
  return computer_hand

#get value of the card
def get_val(hand):
  value = 0
  
  for card in hand:
    if "R" in hand: #<- Design says, if either dealer or player has R, their hand is valued 21 regardless.
      value += 21
      return value
    elif card[0] in ['1', 'J', 'Q', 'K', 'A']:
      value += 10
    else:
      value += int(card[0])

  return value

#display card for player
def display_player(player_hand):
  if player_hand:
    #It works, but try to understand the one liner and why it works. Can be done without using one line?
    cards = " ".join(card for card in player_hand)
    return cards
    
#display card for player
def display_dealer(dealer_hand, flag):
    if flag:
        cards = " ".join(card for card in dealer_hand)
        return cards
    else:
    #It works, but try to understand the one liner and why it works. Can it be done without using one liner?
        dealer_hand[0] = '\u2588\u2588'
        cards = " ".join(card for card in dealer_hand)
        return cards

#You win if dealer bust or if your score is > dealer's score 
#You lose if you bust or if your score < delaer's score
#check if player or dealer wins or busts
def check_score(score, comp_hand, player_hand):
    #"Push" means both dealer and player ties or dealer gets 21 when they get first get their hand
    if len(comp_hand) == 2:
        if score == 21:
          print("Push, no one wins")
          return True
    else: 
        if score == 21:
            print("Dealer wins!")
            return True

    #if len(player_hand) > 0:
    
#main game loop
def game_loop(num_decks, num_retrievers):
  deck = []
  player_hand = []
  comp_hand = []
  win_flag = False
  
  
  #betting quatloos
  quatloos = (get_bet(bet))
  print(quatloos)

  if len(deck) == 0:
    #creating and shuffling cards
    create_deck(deck, num_retrievers, num_decks)
    shuffle_deck(deck)

  #dealing hand to dealer
  comp_hand = (deal_cards_comp(deck, comp_hand))
  dealer_hand_val = get_val(comp_hand)
  print("dealer's value", dealer_hand_val) #<- cannot be printed in the final, but it's here for checking
  win_flag = check_score(dealer_hand_val, comp_hand, player_hand)
  display_card_dealer = display_dealer(comp_hand, win_flag)

  if win_flag:
    print(f"The dealer hand is: {display_card_dealer} and value has value ", dealer_hand_val)
    
    play_again = input("Would you like to play again? [y/yes] ").lower()
    if play_again == "y" or play_again == "yes":
      game_loop(num_decks, num_retrievers)  
    
  else:
    print(f"The dealer hand is: {display_card_dealer}")
    
    #dealing hand to player and displaying them
    player_hand = (deal_cards_player(deck, player_hand))
    player_hand_val = get_val(player_hand)
    display_card_player = display_player(player_hand)
    print(f"Your hand is: {display_card_player} and the value is {player_hand_val}")
    
    #You win if dealer bust or if your score is > dealer's score 
    #You lose if you bust or if your score < delaer's score
    
    #while loop for the game
    hit_stay = input("What would you like to do? [hit, stay] ")
    if hit_stay == "hit":
      while win_flag != True: #Temporary: Need to change when someone wins or busted
        player_hand = (deal_cards_player(deck, player_hand))
        player_hand_val = get_val(player_hand)
        display_card_player = display_player(player_hand)
        print(f"Your hand is: {display_card_player} and the value is {player_hand_val}")
        hit_stay = input("What would you like to do? [hit, stay] ")

if __name__ == "__main__":
  num_decks = int(input("How many decks of cards would you like to use? "))
  random_seed = input("What seed would you like to use? ")
  random.seed(random_seed)
  num_retrievers = int(input("How many Retriever cards would you like to add? "))

  game_loop(num_decks, num_retrievers)

"""
Reminder:
  Currently working on checking if player or dealer wins or bust - Next thing to work on
  Currently working on while loop for the game. - Last thing you were working on
  Currently making display function to show cards - DONE
  Currently working on deck - updating the deck [I think when playing again, it shuffles the deck, but other than that deck gets updated]
  Future Work:
    Quatloos update when player wins - Currently working on - 06/07/2023

"""