"""
From previous CMSC201 Project
  Attempting to recreate first project from CMSC201

Cannot use dictionaries

            BLACKJACK
By: Christian De Guzman
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
def get_bet(quatloos, bet): #<-- tested and it works
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
    elif "2" in card:
      value += 2
    elif "3" in card:
      value += 3
    elif "4" in card:
      value += 4
    elif "5" in card:
      value += 5
    elif "6" in card:
      value += 6
    elif "7" in card:
      value += 7
    elif "8" in card:
      value += 8
    elif "9" in card:
      value += 9
    elif "10" in card:
      value += 10
    elif "A" in card:
      value += 10
    elif "J" in card:
      value += 10
    elif "K" in card:
      value += 10
    elif "Q" in card:
      value += 10

  return value

#display card for player
def display_player(player_hand):
  if player_hand:
    #It works, but try to understand the one liner and why it works. Can be done without using one line?
    cards = " ".join(card for card in player_hand)
    return cards
    
#display card for player
def display_dealer(dealer_hand, flag):
  if flag == True:
    cards = " ".join(card for card in dealer_hand)
    return cards
  else:
    #It works, but try to understand the one liner and why it works. Can be done without using one line?
    dealer_hand[0] = '\u2588\u2588'
    cards = " ".join(card for card in dealer_hand)
    return cards

#check if player or dealer wins or busts
#
def check_score(score, flag, comp_hand):
  #"Push" means both dealer and player ties or dealer gets 21 when they get first get their hand
  if len(comp_hand) == 2:
    if score == 21:
      flag = True
      print("Push, no one wins")
      return flag
  
  
#main game loop
def game_loop(num_decks, num_retrievers):
  deck = []
  player_hand = []
  comp_hand = []
  quatloos = 100
  win_flag = False
  
  #betting quatloos
  bet = int(input(f"You have {quatloos}, how many would you like to bet? "))
  quatloos = (get_bet(quatloos, bet))
  print(quatloos)

  if len(deck) == 0:
    #creating and shuffling cards
    create_deck(deck, num_retrievers, num_decks)
    shuffle_deck(deck)

  #dealing hand to dealer
  comp_hand = (deal_cards_comp(deck, comp_hand))
  dealer_hand_val = get_val(comp_hand)
  print("dealer's value", dealer_hand_val) #<- cannot be printed in the final, but it's here for checking
  win_flag = check_score(dealer_hand_val, win_flag, comp_hand)
  display_card_dealer = display_dealer(comp_hand, win_flag)
  if win_flag == False:
    print(f"The dealer hand is: {display_card_dealer}")
    
    #dealing hand to player and displaying them
    player_hand = (deal_cards_player(deck, player_hand))
    player_hand_val = get_val(player_hand)
    display_card_player = display_player(player_hand)
    print(f"Your hand is: {display_card_player} and the value is {player_hand_val}")
    
    #while loop for the game
    hit_stay = input("What would you like to do? [hit, stay] ")
    if hit_stay == "hit":
      while hit_stay != "stay": #Temporary: Need to change when someone wins or busted
        player_hand = (deal_cards_player(deck, player_hand))
        player_hand_val = get_val(player_hand)
        display_card_player = display_player(player_hand)
        print(f"Your hand is: {display_card_player} and the value is {player_hand_val}")
        hit_stay = input("What would you like to do? [hit, stay] ")
    
  else:
    print(f"The dealer hand is: {display_card_dealer} and value has a value of:", dealer_hand_val)

  if win_flag == False:
    #dealing hand to player and displaying them
    player_hand = (deal_cards_player(deck, player_hand))
    player_hand_val = get_val(player_hand)
    display_card_player = display_player(player_hand)
    print(f"Your hand is: {display_card_player} and the value is {player_hand_val}")
    
    #while loop for the game
    hit_stay = input("What would you like to do? [hit, stay] ")
    if hit_stay == "hit":
      while hit_stay != "stay": #Temporary: Need to change when someone wins or busted
        player_hand = (deal_cards_player(deck, player_hand))
        player_hand_val = get_val(player_hand)
        display_card_player = display_player(player_hand)
        print(f"Your hand is: {display_card_player} and the value is {player_hand_val}")
        hit_stay = input("What would you like to do? [hit, stay] ")
  else:
    play_again = input("Would you like to play again? [y/yes] ").lower()
    if play_again == "y" or play_again == "yes":
      game_loop(num_decks, num_retrievers)

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
    Quatloos update when player wins

"""