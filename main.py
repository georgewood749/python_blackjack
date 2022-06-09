import random
import art


def hit():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, dealer_score):
    if user_score > 21 and dealer_score > 21:
        return "\nYou went bust. Game over!"
    if user_score == dealer_score:
        return "\nPush."
    elif dealer_score == 0:
        return "\nDealer has Blackjack. Game over!"
    elif user_score == 0:
        return "\nBlackjack! You win!"
    elif user_score > 21:
        return "\nYou went bust. Game over!"
    elif dealer_score > 21:
        return "\nDealer went bust. You win!"
    elif user_score > dealer_score:
        return "\nYou win!"
    else:
        return "\nYou lose."


def play():
    print(art.logo)

    user_hand = []
    dealer_hand = []
    is_game_over = False

    for _ in range(2):
        user_hand.append(hit())
        dealer_hand.append(hit())

    while not is_game_over:
        user_score = calculate_score(user_hand)
        dealer_score = calculate_score(dealer_hand)
        print(f"\nYour cards are: {user_hand}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_hand[0]}\n")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_hit = input("Would you like another card? Y or N\n").lower()
            if user_hit == "y":
                user_hand.append(hit())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(hit())
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand is {user_hand}, final score: {user_score}")
    print(f"Dealer's final hand is {dealer_hand}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))


while input("Would you like to play a hand? Y or N\n").lower() == "y":
    play()
