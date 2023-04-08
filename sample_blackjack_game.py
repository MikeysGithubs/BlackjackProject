import random


suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9","10", "Jack",
         "Queen", "King"]

CONST = {"player": "player", "dealer": "dealer"}


def shuffle_deck(deck):
    random.shuffle(deck)


def create_deck():
    """
    Function creates a deck of cards
    and returns the deck in the form of a list
    No modifications
    :param: None

    :return: list of cards
    """
    deck = []
    for suit in suits:
        for rank in ranks:
            if rank == "Ace":
                value = 11
            elif rank in ["Jack", "Queen", "King"]:
                value = 10
            else:
                value = int(rank)
            card = [suit, rank, value]
            deck.append(card)
    return deck


def get_hand_value(hand_value): #may need to replace with hand instead of hand_value
    """
    setting hand values

    :param hand_value: list of list, [[suit, rank, value], [suit, rank, value]]
    :return: int - total value for hand
    """
    value = 0
    aces = 0
    for card in hand_value:
        value += card[2]
        if card[1] == "Ace":
            aces += 1
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

    # total = 0
    # Ace_count = 0
    # for card in hand_value:
    #     if card[1] == "Ace":
    #         Ace_count += 1
    #     total += card[-1]
    # while total > 21 and Ace_count > 0:
    #     total -= 10
    # return total


def validate_bet(money, bet):
    if bet < 5 or bet >1000:
        return False
    if bet > money:
        return False
    return True


def calculate_winner(player_hand, dealer_hand):
    player_points = get_hand_value(player_hand)
    dealer_points = get_hand_value(dealer_hand)

    if player_points > 21:
        return CONST["dealer"]

    if dealer_points > 21:
        return CONST["player"]

    if player_points > dealer_points:
        return CONST["player"]
    else:
        return CONST["dealer"]


def show_top_card(hand):
     print(f"{hand[0][1]} of {hand[0][0]}")


def clear_hand(hand: list) -> None:
    hand.clear()


def show_hand(hand):
    """

    :param :hand: list of list, [[suit, rank, value], [suit, rank, value]]

    :return:
    """
    for card in hand:
        print(f"{card[1]} of {card[0]}")


def add_card_to_hand(deck, hand):
    # card = deck.pop(0)
    # hand.append(card)
    # if card[1] == "Ace":
    #     hand[2] = 1 if get_hand_value(hand) > 21 else 11
    # return card
    hand.append(deck.pop(0))

