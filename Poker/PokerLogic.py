def checkStraight(hand, communityHand):
    nummedCommunityHand = []
    for card in communityHand:
        nummedCommunityHand.append(int(card.Number))
    nummedHand = []
    for card in hand:
        nummedHand.append(int(card.Number))
    totalHand = nummedCommunityHand + nummedHand
    print(totalHand)
    totalHand.sort()
    runLength = 0
    highCard = 0 
    for index, i in enumerate(totalHand):
        if index == len(totalHand) - 1:
            break
        if totalHand[index + 1] - totalHand[index] == 1:
            runLength += 1
            highCard = i
        else:
            runLength = 0
    if runLength >= 5:
        return (highCard + 400)
    else:
        return 0
        
    



def winningPlay(num):
    print(num)
    if num < 100:
        return "High Card"
    if num < 200 and num > 100:
        return "Pair"
    if num < 300  and num > 200:
        return "Two Pair"
    if num < 400 and num > 300:
        return "3 Of A Kind"
    if num < 500 and num > 400:
        return "Straight"
    if num < 600 and num > 500:
        return "Flush"
    if num < 700 and num > 600:
        return "Full House"
    if num < 800 and num > 700:
        return "4 of a Kind"


    
def addHighCard(hand):
    nummedHand = []
    for card in hand:
        nummedHand.append(card.Number)
    return int(max(nummedHand))


def checkDouble(hand, communityHand):
    nummedCommunityHand = []
    for card in communityHand:
        nummedCommunityHand.append(card.Number)
    nummedHand = []
    for card in hand:
        nummedHand.append(card.Number)
    totalHand = nummedCommunityHand + nummedHand
    countedItems = {i:totalHand.count(i) for i in totalHand}
    print(countedItems)
    pairs = []
    threeKind = []
    fourKind = []
    for key, value in countedItems.items():
        if value == 2:
            pairs.append(int(key))
        if value == 3:
            threeKind.append(int(key))
        if value == 4:
            fourKind.append(int(key))
    if threeKind and pairs and not fourKind:
        print("ROADHOUSE")
        return (pairs[0] + threeKind[0] + 600)
    if threeKind and not fourKind:
        print("THREE KIND")
        return (threeKind[0] + 300)
    if len(pairs) >= 2 and not fourKind:
        print("two pair")
        return (sum(pairs) + 200)
    if len(pairs) == 1:
        print("pair")
        return (pairs[0] + 100)
    if not pairs and not threeKind and not fourKind:
        print("high card")
        return 0
    if fourKind:
        print("Four Kind")
        return (fourKind[0]+700)
        

def pokerMain(hands, communityHand):
    for key, hand in hands.items():
        runningTotal = 0
        valueToAdd = checkStraight(hand, communityHand)
        runningTotal = runningTotal + valueToAdd
        if runningTotal == 0:
            valueToAdd = checkDouble(hand, communityHand)
            runningTotal = runningTotal + valueToAdd
        print(key)
        valueToAdd = addHighCard(hand)
        runningTotal = runningTotal + valueToAdd
        hands[key] = runningTotal
        ##print(hands[key])
    winnerKey = max(hands, key=hands.get)
    ##print(winnerKey)
    winReason = winningPlay(hands[winnerKey])
    ##print(winReason)
    return(winnerKey, winReason)
    
        
