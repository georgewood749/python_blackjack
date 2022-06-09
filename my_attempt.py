import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0


def hit(amount):
    for n in range(0, amount):
        player_hand.append(random.choice(cards))
        global player_score
        player_score += player_hand[-1]


def dealer_hit(amount):
    for n in range(0, amount):
        dealer_hand.append(random.choice(cards))
        global dealer_score
        dealer_score += dealer_hand[-1]


def clear_cards():
    global player_hand
    player_hand = []
    global dealer_hand
    dealer_hand = []
    global player_score
    player_score = 0
    global dealer_score
    dealer_score = 0


def check():
    if player_score > 21:
        print("You have gone bust. You lose.")
    elif dealer_score > 21:
        print("Dealer bust. You win!")
    elif player_score == dealer_score:
        print("Push.")
    elif 21 > dealer_score > player_score:
        print("Dealer wins.")
    elif player_score > dealer_score:
        print("You win!")
    else:
        print("Dealer wins.")


another_hand = True
while another_hand:
    continue_playing = True
    clear_cards()
    print(art.logo)
    dealer_hit(2)
    hit(2)
    print(f"Your cards are: {player_hand}, your current hand = {player_score}")
    print(f"The dealer has {dealer_hand[0]}")
    while player_score <= 21 and continue_playing:
        hit_me = input("\nWould you like another card? Y or N\n").lower()
        if hit_me == "n":
            continue_playing = False
            print(f"Your cards are: {player_hand}, your current hand = {player_score}")
        if hit_me == "y":
            hit(1)
            print(f"Your cards are: {player_hand}, your current hand = {player_score}")
#            print(f"The dealer has {dealer_hand[0]}")
#         for card in player_hand:
#             if card == 11 and player_score > 21:
#                 card = 1
        while dealer_score <= 16:
            dealer_hit(1)

    print(f"Dealer's cards are: {dealer_hand}, dealer's hand = {dealer_score}\n")
    check()
    retry = input("\nWould you like to play another hand? Y or N\n").lower()
    if retry == "n":
        another_hand = False


#   Need to add an argument for when an 11 is drawn.
