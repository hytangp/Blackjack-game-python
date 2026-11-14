import art, random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_choices_to_continue = [True, False]
continue_playing_game = True

def deal_card():
    return random.choice(cards)

def calculate_score(list_of_cards):
    sum_of_cards = sum(list_of_cards)

    if len(list_of_cards) == 2 and sum_of_cards == 21:
        return 0
    else:
        return sum_of_cards

def compare(player_cards_total, dealer_cards_total):
    if player_cards_total > 21:
        print("You went over. You lose 😭")
    elif dealer_cards_total > 21:
        print("Opponent went over. You win 😁")
    else:
        if player_cards_total > dealer_cards_total:
            print("You win 😃")
        elif player_cards_total == dealer_cards_total:
            print("Draw 🙃")
        else:
            print("You lose 😤")

def print_final_cards_and_score(player_cards, player_cards_total, dealers_cards, dealer_cards_total):
    print(f"   Your final hand: {player_cards} , final score: {player_cards_total}")
    print(f"   Computer's final hand: {dealers_cards}, final score: {total_of_dealer_cards}")

while continue_playing_game:
    play_or_no = input("Do you want to play the game of Blackjack? type 'y' or 'n': ")

    if play_or_no != 'y':
        continue_playing_game = False
        print("Goodbye. Cya!")
    else:
        print("\n" * 50)
        print(art.logo)
        player_want_to_continue_dealing = dealer_want_to_continue_dealing = True

        player_card1 = deal_card()
        player_card2 = deal_card()
        player_all_cards = [player_card1, player_card2]
        total_of_player_cards = 0

        dealers_card1 = deal_card()
        dealers_card2 = deal_card()
        dealers_all_cards = [dealers_card1, dealers_card2]

        if calculate_score(player_all_cards) == 0:
            print_final_cards_and_score(player_all_cards, calculate_score(player_all_cards), [dealers_card1], calculate_score([dealers_card1]))
            print("Win with a Blackjack 😎")
        elif calculate_score(dealers_all_cards) == 0:
            print_final_cards_and_score(player_all_cards, calculate_score(player_all_cards), dealers_all_cards, calculate_score(dealers_all_cards))
            print("Lose, opponent has Blackjack 😱")
        else:
            # Players dealing
            while total_of_player_cards < 21 and player_want_to_continue_dealing:
                if total_of_player_cards > 0:
                    play_continue_card = deal_card()
                    player_all_cards.append(play_continue_card)
                else:
                    play_continue_card = None

                if play_continue_card is not None and play_continue_card == 11 and (calculate_score([total_of_player_cards, play_continue_card]) > 21):
                    total_of_player_cards += 1
                else:
                    total_of_player_cards = calculate_score(player_all_cards)

                print(f"    Your cards: {player_all_cards}, current score: {total_of_player_cards}")
                print(f"    Computer's first card: {dealers_card1}")

                if total_of_player_cards < 21:
                    continue_or_not = input("Type 'y' to get another card, type 'n' to pass: ")

                    if continue_or_not != 'y':
                        player_want_to_continue_dealing = False

            # Computers dealing
            total_of_dealer_cards = calculate_score(dealers_all_cards)

            while total_of_dealer_cards < 21 and dealer_want_to_continue_dealing:
                dealer_want_to_continue_or_not = random.choice(dealer_choices_to_continue)

                if dealer_want_to_continue_or_not:
                    play_continue_card = deal_card()
                    dealers_all_cards.append(play_continue_card)

                    if play_continue_card == 11 and (calculate_score([total_of_dealer_cards,  play_continue_card]) > 21):
                        total_of_dealer_cards += 1
                    else:
                        total_of_dealer_cards = calculate_score(dealers_all_cards)
                else:
                    dealer_want_to_continue_dealing = False

            print_final_cards_and_score(player_all_cards, total_of_player_cards, dealers_all_cards, total_of_dealer_cards)

            compare(total_of_player_cards, total_of_dealer_cards)
