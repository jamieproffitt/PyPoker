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
        return "Full House"


    
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
    for key, value in countedItems.items():
        if value == 2:
            pairs.append(int(key))
        if value == 3:
            threeKind.append(int(key))
    if threeKind and pairs:
        return (pairs[0] + threeKind[0] + 400)
    if threeKind:
        return (threeKind[0] + 300)
    if len(pairs) == 2:
        return (sum(pairs) + 200)
    if len(pairs) == 1:
        return (pairs[0] + 100)
    if not pairs and not threeKind:
        return 0
        

def pokerMain(hands, communityHand):
    for key, hand in hands.items():
        runningTotal = 0
        valueToAdd = checkDouble(hand, communityHand)
        print(key)
        runningTotal += valueToAdd
        if runningTotal == 0:
            valueToAdd = addHighCard(hand)
            runningTotal += valueToAdd
        hands[key] = runningTotal
    winnerKey = max(hands)
    print(winnerKey)
    winReason = winningPlay(hands[winnerKey])
    print(winReason)
    return(winnerKey, winReason)
    
        
