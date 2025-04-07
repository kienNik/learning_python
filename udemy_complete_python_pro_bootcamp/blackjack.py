'''
rules:
- sum of card must <= 21, else will lose
- J, Q, K equals 10
- A equals 1 or 11
- if dealer's sum < 17 then must pick 1 more card
- infinite deck of cards (1 card can be drawn multiple times)

gameplay:
- dealer a.k.a PC
- dealer has 1 card, player has 2
- player can choose to stop (stand) or keep drawing (keep dealing)
- if sum > 21, player lose
- if player choose stand, dealer draw 1 more then compare sums, 1 more if sum < 17

TODO:
- choose value of A, currently 11
- raplace 10 or 11 with J, Q, K, A
'''

from random import choice

# J, Q, K has value 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def print_cards(cards: list):
    for card in cards:
        print(f'{card} ', end=' ')

def compare_sums(player_cards, dealer_cards):
    if sum(player_cards) > sum(dealer_cards) or sum(dealer_cards) > 21:
        print('Win.')
    elif sum(player_cards) == sum(dealer_cards):
        print('Draw.')
    else:
        print('Lose.')

def print_info(player_cards, dealer_cards):
    print('Player\'s cards:')
    print_cards(player_cards)
    print(f'\nPlayer\'s sum: {sum(player_cards)}\n')

    print('Dealer\'s cards:')
    print_cards(dealer_cards)
    print(f'\nDealer\'s sum: {sum(dealer_cards)}\n')

def change_ace_value(cards: list):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

def blackjack():
    player_cards = []
    dealer_cards = []

    # seed
    player_cards.append(choice(cards))
    player_cards.append(choice(cards))
    dealer_cards.append(choice(cards))

    keep_dealing = True
    while keep_dealing:
        print_info(player_cards, dealer_cards)
        if sum(player_cards) == 21:
            print('Win')
            return
        elif sum(player_cards) > 21:
            print('Lose')
            return

        deal = input('Keep dealing? y or n: ')
        if deal == 'n':
            dealer_cards.append(choice(cards))
            change_ace_value(dealer_cards)
            while sum(dealer_cards) < 17:
                dealer_cards.append(choice(cards))
                change_ace_value(dealer_cards)
            print_info(player_cards, dealer_cards)
            compare_sums(player_cards, dealer_cards)
            keep_dealing = False
        elif deal == 'y':
            player_cards.append(choice(cards))
            change_ace_value(player_cards)
        else:
            print('Invalid input.')
            return

playing = True
while playing:
    keep_playing = input('Start new game? y or n: ')
    if keep_playing == 'y':
        blackjack()
    elif keep_playing == 'n':
        playing = False
        print('Quitting.')
    else:
        print('Invalid input. Quitting.')
        playing = False
