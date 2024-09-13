import random
def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10]
    return random.choice(cards)

def cal_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score,c_score):
    if u_score==c_score:
        return 'Draw'
    elif u_score==0:
        return 'Lose, opponent has black jack'
    elif c_score==0:
        return 'Won, you have have black jack'
    elif u_score>21:
        return 'You went over, you lose'
    elif c_score>21:
        return 'Opponent went over, you won'
    elif u_score>c_score:
        return 'You win'
    else:
        return 'Yor lose'

def play_game():
    user_cards=[]
    comp_cards=[]
    comp_score=-1
    user_score=-1
    gameov=False

    for _ in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    while not gameov:
        user_score=cal_score(user_cards)
        comp_score=cal_score(comp_cards)
        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f'Computer first card: {comp_cards[0]}')

        if user_score==0 or comp_score==0 or user_score>21:
            gameov=True
        else:
            user_deal=input('Do you want to get another card(y/n): ')
            if user_deal=='y':
                user_cards.append(deal_cards())
            else:
                gameov=True

    while comp_score!=0 and comp_score<17:
        comp_cards.append(deal_cards())
        comp_score=cal_score(comp_cards)

    print(f'Your final hand: {user_cards}, final score: {user_score}')
    print(f'Computer final hand: {user_cards}, final score: {user_score}')
    print(compare(user_score,comp_score))

while input('Do you want to play a game of blackjack(y/n): ')=='y':
    print('\n'*8)
    play_game()