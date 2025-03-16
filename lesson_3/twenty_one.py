""" This is the program for playing BlackJack!"""

import os
import random

SUITS = ["Spades", "Clovers", "Hearts", "Diamonds"]
NUMBERS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", 'Queen', 'King']
DECK_OF_CARDS = [[number, suit] for suit in SUITS
                 for number in NUMBERS]
WINNING_VALUE = 21
DEALER_TO_HIT_UNTIL = 17

shuffled_deck = DECK_OF_CARDS[:]
dealers_hand = []
players_hand = []
hit_or_stay = True

def prompt(text):
    """ Allows from prompting to show where program strings occur"""
    print(f'==> {text}')

def match_case_cards(card_string):
    """Reference to help with converting a card string to an integer value"""
    match card_string:
        case 'Ace':
            return 11
        case '2':
            return 2
        case '3':
            return 3
        case '4':
            return 4
        case '5':
            return 5
        case '6':
            return 6
        case '7':
            return 7
        case '8':
            return 8
        case '9':
            return 9
        case '10'|'Jack'|'Queen'|'King':
            return 10
        case 'One':
            return 1

def shuffle_deck(deck):
    """Shuffles the deck randomly"""
    return random.shuffle(deck)

def reshuffle(deck):
    """Clears the dealers and players hand as well as repopulates the deck"""
    dealers_hand.clear()
    players_hand.clear()
    deck = DECK_OF_CARDS[:]
    return deck

def deal_cards(deck):
    """Initiate the game by removing the last 4 values from the deck and placing them 
    into the player and dealers hand"""
    players_hand.append(deck.pop())
    dealers_hand.append(deck.pop())
    players_hand.append(deck.pop())
    dealers_hand.append(deck.pop())
    return len(deck)

def hit_from_deck(deck, receiver):
    """Removes a card from the deck and appends to the receivers hand"""
    receiver.append(deck.pop())
    return receiver

def bust_condition(receiver):
    """Checks to see if the hand is over WINNING_VALUE in value"""
    if hand_total(receiver) > WINNING_VALUE:
        if check_for_ace(receiver):
            convert_ace(receiver)
            return None
        return True
    return None

def check_for_ace(hand):
    """Checks to see if Ace is in a hand"""
    lst_of_values = [value for value, _ in hand]
    if 'Ace' in lst_of_values:
        return True
    return False

def convert_ace(hand):
    """Changes the value of an Ace from 11 to 1"""
    for card in hand:
        if card[0] == 'Ace':
            card[0] = 'One'

def hand_equivalent(receiver):
    """ 
    Returns the integer value of the card based off of 
    the match case reference.
    """
    return [(match_case_cards(card[0]))
            for card in receiver]

def hand_total(hand):
    """Sums the integer hand"""
    return sum(hand_equivalent(hand))

def winning_condition(dealers, players):
    """ Defines what a winning hand is and returns the winner """
    if hand_total(dealers) > hand_total(players):
        prompt('Dealer Wins!')
    elif hand_total(dealers) == hand_total(players):
        prompt('Dealer Wins!')
    else:
        prompt('Player Wins!')

def display_hands_hidden(dealer, player):
    """Shows the hands of the dealer with a hidden card and your hand"""
    prompt('')
    prompt(f"Dealers hand: unknown card and {dealer[1:]}")
    prompt('')
    prompt(f"Your hand: {player}")
    prompt('')

def display_hands_exposed(dealer, player):
    """Shows the hands of the dealer with all cards exposed and your hand"""
    prompt('')
    prompt(f'Dealer has {dealers_hand}')
    prompt('')
    prompt(f'Dealers total is {hand_total(dealers_hand)}')
    prompt(f'You have {hand_total(players_hand)}')
    prompt('')

def play_blackjack(deck):
    """Contains the full game of blackjack"""
    while True:
        os.system('clear')
        prompt('Welcome to Blackjack!')
        shuffle_deck(deck)

        deal_cards(deck)
        display_hands_hidden(dealers_hand, players_hand)
        while hit_or_stay:
            prompt('Hit or Stay? (Type "H" or "S", followed by "Enter" key)')
            response = input().strip().lower()

            if response not in ['h', 's']:
                prompt("Not a valid choice")
    
            elif response == 'h':
                hit_from_deck(deck, players_hand)
                display_hands_hidden(dealers_hand, players_hand)

                if bust_condition(players_hand):
                    break
            elif response == 's':
                break

        if bust_condition(players_hand):
            prompt(f'Dealer has {dealers_hand}')
            prompt(f'Bust! You have {hand_total(players_hand)}. You Lose!')
        else:
            prompt(f"Dealers hand: unknown card and {dealers_hand[1:]}")
            while hand_total(dealers_hand) < DEALER_TO_HIT_UNTIL:
                hit_from_deck(deck, dealers_hand)
                prompt('Dealer Hits')
                prompt('')
                if bust_condition(dealers_hand):
                    break
                display_hands_hidden(dealers_hand, players_hand)
            if bust_condition(dealers_hand):
                display_hands_exposed(dealers_hand, players_hand)
                prompt(f'Dealer Busts! They have {hand_total(dealers_hand)}. You Win!')
            else:
                prompt('Dealer Stays')
                display_hands_exposed(dealers_hand, players_hand)

                winning_condition(dealers_hand, players_hand)

        prompt("Play again? (y or n)")
        answer = input().lower()
        while answer not in ['y', 'yes', 'no', 'n']:
            prompt("Not a valid choice")
            prompt("Play again? (y or n)")
            answer = input().lower()
        if answer in ('y', 'yes'):
            deck = reshuffle(deck)
            continue
        break


play_blackjack(shuffled_deck)
