import random

suits = ("Heart", "Diamond", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


class Card:
    """
    To determine suit, rank and value of a card
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        self.property = 1

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.Deck_to_play = []

        for suit in suits:
            for rank in ranks:
                self.Deck_to_play.append(Card(suit, rank))

    def shuffle_deck(self):
        random.shuffle(self.Deck_to_play)

    def deal_two(self):
        return [self.Deck_to_play.pop(0), self.Deck_to_play.pop(1)]

    def deal_one(self):
        return self.Deck_to_play.pop(0)


class Player:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def bet(self):
        print("-"*50)
        print("Your Balance -", self.balance)
        while True:
            bet_amount = int(input("How much you want to bet?"))
            print("\n" * 25)
            if bet_amount > self.balance:
                print("You have only", self.balance, "left.")
            elif bet_amount < 1:
                print("Invalid bet, please try again.")
            else:
                self.balance -= bet_amount
                return bet_amount


def hit(deck):
    return deck.deal_one()


def stand(deck, dealer_card):
    a = dealer_card[0].value + dealer_card[1].value
    while a < 17:
        cards = hit(deck)
        dealer_card.append(cards)
        a = adjust_ace(dealer_card)
    return dealer_card


def winner_check(player_card, dealer_card):

    p = adjust_ace(player_card)
    d = adjust_ace(dealer_card)

    if p > d:
        Dealer_card[-1].property = 1
        display(Player_card, Dealer_card)
        print("You won this round.")
        Player.balance += 2 * Bet_amount
    elif p == d:
        Dealer_card[-1].property = 1
        display(Player_card, Dealer_card)
        print("!!!!DRAW!!!!")
    else:
        Dealer_card[-1].property = 1
        display(player_card, dealer_card)
        print("You loose this round.")

    return True


def check_bust(cards):

    b = adjust_ace(cards)
    if b > 21:
        return 1
    else:
        return 0


def display(player, dealer):
    print("-" * 50)
    print("Dealer's Card -- ")
    for z in range(len(dealer)):
        if dealer[z].property == 1:
            print("\t", dealer[z])
        else:
            print("\t", "*"*(len(str(dealer[0]))))
    print("-"*50)
    print(f"{Player.name}'s Card -- ")
    for z in range(len(player)):
        print("\t", player[z])
    print("-" * 50)


def adjust_ace(card_list):
    ace = 0
    value = 0
    for q in card_list:
        value += q.value
        if q.rank == "Ace":
            ace += 1

    while value > 21 and ace > 0:
        value -= 10
        ace -= 1

    return value


print("\n"*20, "*"*25, "BLACKJACK", "*"*25, "\n")
Name = input("Your Name: ")
print("\n"*25)
print("Hey", Name + ", Lets play......")
Player = Player(Name, 1000)

game = True
New_Deck = Deck()

while game:

    Deck = New_Deck
    Deck.shuffle_deck()

    if Player.balance == 0:
        print("You can't play further.\n"
              "You don't have enough money to play.")
        game = False
        break

    Bet_amount = Player.bet()
    print("-" * 70)
    print("Your Balance -", Player.balance, "\t\t||\t\t Bet Amount -", Bet_amount)
    print("-" * 70)

    Player_card = []
    Player_card.extend(Deck.deal_two())
    Dealer_card = []
    Dealer_card.extend(Deck.deal_two())

    Dealer_card[-1].property = 0
    display(Player_card, Dealer_card)

    x = 0
    while x <= 21:

        if (Player_card[0].value + Player_card[1].value) == 21:
            Dealer_card[-1].property = 1
            print("\n" * 25)
            display(Player_card, Dealer_card)
            print("You won this round.")
            Player.balance += 2 * Bet_amount
            break

        choice = input("You want to:\n"
                       "1. Hit\n"
                       "2. Stand")
        print("\n" * 25)

        if choice == "1":
            card = hit(Deck)
            Player_card.append(card)
            x = adjust_ace(Player_card)
            if check_bust(Player_card) == 1:
                Dealer_card[-1].property = 1
                display(Player_card, Dealer_card)
                print("!!!!BUSTED!!!!")
                print("-"*50)
                print("Your Balance -", Player.balance)
                print("-" * 50)
                break
            elif x == 21:
                Dealer_card[-1].property = 1
                display(Player_card, Dealer_card)
                Player.balance += 2 * Bet_amount
                print("-" * 50)
                print("You won.")
                print("Your Balance -", Player.balance)
                print("-" * 50)
                break
            display(Player_card, Dealer_card)
        elif choice == "2":
            Dealer_card[-1].property = 1
            Dealer_card = stand(Deck, Dealer_card)
            if check_bust(Dealer_card):
                display(Player_card, Dealer_card)
                print("-"*50)
                print("Dealer Busted.....\n"
                      "You won this round....")
                print("-" * 50)
                Player.balance += 2*Bet_amount
                break

            elif winner_check(Player_card, Dealer_card):
                break
        else:
            print("Invalid choice.")
            break

    choice = input("Do you want to play again?\n"
                   "1. Yes\n"
                   "2. No")
    print("\n" * 25)
    if choice == "1":
        continue
    elif choice == "2":
        game = False
    else:
        print("Invalid choice.")
