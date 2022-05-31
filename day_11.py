# blackjack game

import random

# returning a random card rom deck.
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10];
    card = random.choice(cards);
    return card;

# take a list of card an return the score cal by cards.

def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0;
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11);
        cards.append(1);
        
    return sum(cards);

user_card = [];
computer_card = [];
game_over = False;

for _ in range(2):
   new_card =  deal_card();
   user_card.append(new_card);
   computer_card.append(deal_card());
   
while not game_over:
    user_score = cal_score(user_card);
    computer_score = cal_score(computer_card);

    print(f"your cards: {user_card}, current score :{user_score}")
    print(f"computers first card: {computer_card[0]}");


    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True;
    else:
        user_deal = input("type 'y' to get another card, type 'n' to pass:")
    if user_deal == 'y':
        user_card.append(deal_card());
    else:
        game_over = True;
        
        
while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card());
    computer_score = cal_score(computer_card);
    
    
   


    
    





    
    
    
    
    


