import os
import random

# Колода
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4


# Колода
def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11: card = "J"
        if card == 12: card = "Q"
        if card == 13: card = "K"
        if card == 14: card = "A"
        hand.append(card)
    return hand


# Сыграть снова
def play_again():
    again = input("Играть снова? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        game()
    else:
        print("Пока!")
        exit()


# Подсчет карт
def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total


# Взять карту
def hit(hand):
    card = deck.pop()
    if card == 11: card = "J"
    if card == 12: card = "Q"
    if card == 13: card = "K"
    if card == 14: card = "A"
    hand.append(card)
    return hand


# Очистка консоли
def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


# Результаты
def print_results(dealer_hand, player_hand):
    clear()
    print("У диллера " + str(dealer_hand) + " - " + str(total(dealer_hand)) + ' очков')
    print("У вас " + str(player_hand) + " - " + str(total(player_hand)) + " очков")


# У кого очко
def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Очко - ты победил!\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Ты проиграл - у диллера очко.\n")
        play_again()


# Сравнение счетов
def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Очко - ты победил!\n")
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Ты проиграл - у диллера очко.\n")
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Ты проиграл - у тебя больше 21\n")
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Ты победил - у диллера больше 21!\n")
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
    # print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Ты победил - твой счет больше чем у диллера!\n")


# Игра
def game():
    choice = 0
    clear()
    print("ОЧКО THE GAME!\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    while choice != "q":
        print("Диллер показывает " + str(dealer_hand[0]))
        print("У тебя " + str(player_hand) + " - " + str(total(player_hand)) + " очков")
        blackjack(dealer_hand, player_hand)
        choice = input("Взять - [H], Пропустить - [S], или Выйти - [Q]: ").lower()
        clear()
        if choice == "h":
            hit(player_hand)
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "s":
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "q":
            print("Пока")
            exit()


# Запуск
if __name__ == "__main__":
    game()
