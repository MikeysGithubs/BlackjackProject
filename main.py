# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sample_blackjack_game as bg
import db


def main():
    print("BlackJack Project")
    deck = bg.create_deck()
    bg.shuffle_deck(deck)
    money = 100.0
    db.write_money(money, "money")
    player_hand = []
    dealer_hand = []
    while True:
        money = float(db.read_money())
        print(f"money: {money}")
        while True:
            try:
                bet = float(input("Enter the bet amount: "))
                break
            except Exception as e:
                print(e)
                continue
        if not (5 <= bet <= 1000):
            if 0 < bet < 5:
                while True:
                    try:
                        add_chips = float(input("Insufficient bet\n Do you want to buy more chips? Number of chips to buy(No chips = 0):  "))
                        if add_chips < 0:
                            continue
                        break
                    except Exception as e:
                        print(e)
                        continue
                money += add_chips
                db.write_money(money)
            elif bet > 1000:
                print("Bet too large. Must be less than 1000 ")
            else:
                print("Invalid bet amount")
            continue
        if bet > money:
            print("cannot bet insufficient remaining funds")
            continue

        print("BET: ", bet)
        db.write_money(bet, "bet")
        bg.add_card_to_hand(deck, dealer_hand)
        bg.add_card_to_hand(deck, dealer_hand)

        bg.add_card_to_hand(deck, player_hand)
        bg.add_card_to_hand(deck, player_hand)

        #bg.add_card_to_hand(deck, player_hand)

        while True:
            print("Dealer's Show Hand")
            bg.show_top_card(dealer_hand)

            print("Players card: ")
            bg.show_hand(player_hand)

            choice = input("Hit or stand? (hit/stand): ")
            if choice.lower() == "hit":
                bg.add_card_to_hand(deck, player_hand)

            elif choice.lower() == "stand":
                if bg.get_hand_value(dealer_hand) <= 17:
                    bg.add_card_to_hand(deck, dealer_hand)
                    continue

                elif bg.calculate_winner(player_hand, dealer_hand) == bg.CONST["player"]:
                    if bg.get_hand_value(player_hand) == 21:
                        money += round(bet * 1.5, 2)
                        db.write_money(money, "money")
                        print("Blackjack")
                        print("Dealer's Show Hand")
                        bg.show_hand(dealer_hand)
                        print("#"*20)
                        print("Players card: ")
                        bg.show_hand(player_hand)
                        print("#"*20)

                        bg.clear_hand(dealer_hand)
                        bg.clear_hand(player_hand)
                        if input("play again? (y/n):").lower() == "y":
                            break
                        else:
                            return
                    else:
                        money += bet
                        db.write_money(money, "money")
                        print("player wins!!")
                        print("Dealer's Show Hand")
                        bg.show_hand(dealer_hand)
                        print("#"*20)
                        print("Players card: ")
                        bg.show_hand(player_hand)
                        print("#"*20)
                        bg.clear_hand(dealer_hand)
                        bg.clear_hand(player_hand)
                        if input("play again? (y/n):").lower() == "y":
                            break
                        else:
                            return
                else:
                    money -= bet
                    db.write_money(money, "money")
                    print("Dealer wins!!")
                    print("Dealer's Show Hand")
                    bg.show_hand(dealer_hand)
                    print("#"*20)
                    print("Players card: ")
                    bg.show_hand(player_hand)
                    print("#"*20)
                    bg.clear_hand(dealer_hand)
                    bg.clear_hand(player_hand)
                    if input("play again? (y/n):").lower() == "y":
                        break
                    else:
                        return

            player_hand_value = bg.get_hand_value(player_hand)
            dealer_hand_value = bg.get_hand_value(dealer_hand)
            if player_hand_value < 21 and dealer_hand_value < 21:
                continue
            winner = bg.calculate_winner(player_hand, dealer_hand)

            if winner == bg.CONST["player"]:
                if player_hand_value == 21:
                    money += bet * 1.5
                    db.write_money(money, "money")
                    print("Blackjack, player wins")
                    print("Dealer's Show Hand")
                    bg.show_hand(dealer_hand)
                    print("#"*20)
                    print("Players card: ")
                    bg.show_hand(player_hand)
                    print("#"*20)
                    bg.clear_hand(dealer_hand)
                    bg.clear_hand(player_hand)
                    if input("play again? (y/n):").lower() == "y":
                        break
                    else:
                        return
                else:
                    money += bet
                    db.write_money(f"money: {money}")
                    print("player wins!!")
                    print("Dealer's Show Hand")
                    bg.show_hand(dealer_hand)
                    print("#"*20)
                    print("Players card: ")
                    bg.show_hand(player_hand)
                    print("#"*20)
                    bg.clear_hand(dealer_hand)
                    bg.clear_hand(player_hand)
                    if input("play again? (y/n):").lower() == "y":
                        break
                    else:
                        return

            elif winner == bg.CONST["dealer"]:
                money -= bet
                db.write_money(f"money: {money}")
                print("Dealer wins!!")
                print("Dealer's Show Hand")
                bg.show_hand(dealer_hand)
                print("#"*20)
                print("Players card: ")
                bg.show_hand(player_hand)
                print("#"*20)
                bg.clear_hand(dealer_hand)
                bg.clear_hand(player_hand)
                if input("play again? (y/n):").lower() == "y":
                    break
                else:
                    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    print("Good Bye!!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
