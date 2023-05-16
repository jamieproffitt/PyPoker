def winningPlay(num):
    if num < 14:
        return "High Card"
    if num < 27 and num > 13:
        return "Pair"
    if num < 40 and num > 26:
        return "Two Pair"
    if num < 53 and num > 39:
        return "3 Of A Kind"
    if num < 66 and num > 52:
        return "Full House"


    
def addHighCard(hand):
    nummedHand = []
    for card in hand:
        nummedHand.append(card.Number)
    print(max(nummedHand))
    return max(nummedHand)


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
            pairs.append(key)
        if value == 3:
            threeKind.append(key)
    if threeKind and pairs:
        print(threeKind, pairs)
        return int((sum(pairs)) + int(threeKind[0]) + 52)
    if threeKind:
        print(threeKind)
        return int(threeKind[0]) + 39
    if len(pairs) == 2:
        print(pairs)
        return int((sum(pairs)) + 26)
    if len(pairs) == 1:
        print(pairs)
        return int((pairs[0]) + 13)
    if not pairs and not threeKind:
        return 0
        

def pokerMain(hands, communityHand):
    for key, hand in hands.items():
        runningTotal = 0
        valueToAdd = checkDouble(hand, communityHand)
        runningTotal += valueToAdd
        valueToAdd = addHighCard(hand)
        runningTotal += valueToAdd
        hands[key] = runningTotal
    winnerKey = max(hands.items())
    return(winnerKey, winningPlay(hands[winnerKey]))
    
        
