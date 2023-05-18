import random
import os
import time
import PokerLogic

## game classes
class Dealer():
    def __init__(self):
        self.hand = []
        
    def drawHand(self, cards, roundNum):
        if roundNum == 2:
            for i in range(3):
                randInt = random.randrange(0, len(cards))
                self.hand.append(cards[randInt])
                cards.pop(randInt)
        elif roundNum > 2 and roundNum != 5:
            randInt = random.randrange(0, len(cards))
            self.hand.append(cards[randInt])
            cards.pop(randInt)
        

class Card():
    def __init__(self, num, cardSet, path):
        self.Number = str(num)
        self.Set = cardSet

class Player():
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.plrHand = []

    def drawHand(self, cards):
        for i in range(2):
            randInt = random.randrange(0,len(cards))
            self.plrHand.append(cards[randInt])
            cards.pop(randInt)
            
    def bet(self, bet):
        if bet == 0:
            return False
        else:
            if self.cash < bet:
                return False
            else:
                self.cash = self.cash - bet
                return True

## getting cards for use in game
def createCards():
    directory = os.fsencode("Playing Cards/PNG-cards-1.3/")
    cards = []
    for file in os.listdir(directory):
         filename = os.fsdecode(file)
         filename = filename.split(".")[0]
         if "jack" in filename:
             split = filename.split("_")
             card = Card(11, split[2], filename)
             cards.append(card)
             continue
         elif "queen" in filename:
             split = filename.split("_")
             card = Card(12, split[2], filename)
             cards.append(card)
             continue
         elif "king" in filename:
             split = filename.split("_")
             card = Card(13, split[2], filename)
             cards.append(card)
             continue
         elif "ace" in filename:
             split = filename.split("_")
             card = Card(1, split[2], filename)
             cards.append(card)
             continue
         else:
             split = filename.split("_")
             card = Card(split[0], split[2], filename)
             cards.append(card)
             continue
    return cards

## pregame intro
amountPlrs = 0
print("Hello and welcome to Text Poker!")
time.sleep(2)
os.system("cls")
while amountPlrs < 1 or amountPlrs > 4:
    amountPlrs = int(input("How many players?: "))
cash = int(input("What is the starting money?: "))
os.system("cls")

## pregame requisites
cards = createCards()
plrs = []
dealer = Dealer()
for i in range(amountPlrs):
    temp = input("Enter player name: ")
    plr = Player(temp, cash)
    plrs.append(plr)
os.system("cls")
roundNum = 1
pot = 0
## gameloop
while len(plrs) > 1:
    while roundNum < 5:
        dealer.drawHand(cards, roundNum)
        for plr in plrs:
            if roundNum == 1:
                plr.drawHand(cards)
            elif roundNum > 1:
                print("Community Hand:",', '.join([str(str(card.Number) + " of " +card.Set) for card in dealer.hand]))
                print("Player Hand:",', '.join([str(str(card.Number) + " of " +card.Set) for card in plr.plrHand]))
            print("Pot: " + str(pot))
            print(plr.name+": "+str(plr.cash))
            plrBet = int(input("Enter bet amount: "))
            if plr.bet(plrBet) == False:
                print("CHEATER. "+plr.name+" ELIMINATED.")
                plrs.remove(plr)
                time.sleep(1)
            else:
                pot = pot + plrBet
            os.system("cls")
        roundNum = roundNum + 1
    plrHands = {}
    for plr in plrs:
        plrHands[plr.name] = plr.plrHand
    results = PokerLogic.pokerMain(plrHands, dealer.hand)
    winner = results[0]
    for plr in plrs:
        if plr.name == winner:
            actualWinner = plr
    actualWinner.cash += pot
    pot = 0
    input(actualWinner.name + " won via: "+results[1]+". Their cash is now: "+str(actualWinner.cash))
    os.system("cls")
    roundNum = 1
    for plr in plrs:
        plr.plrHand.clear()
    dealer.hand.clear()
    cards.clear()
    cards = createCards()
        
            
