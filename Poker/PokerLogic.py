def checkDouble(nummedHand, communityHand):
    nummedCommunityHand = []
    for card in communityHand:
        nummedCommunityHand.append(card.Number)
    totalHand = nummedCommunityHand + nummedHand
    duplicated = []
    seen = set()
    for num in totalHand:
        if num in seen:
            duplicated.append(num)
        else:
            seen.add(num)
    if not duplicated:
        return (False, 0)
    elif len(duplicated) == 1:
        return (True, duplicated[0])
    else:
        return (True, max(duplicated))
        

def pokerMain(hands, communityHand):
    for key, hand in hands.items():
        nummedHand = []
        for card in hand:
            nummedHand.append(card.Number)
        doubleResults = checkDouble(nummedHand, communityHand)
        hasDouble, doubleValue = doubleResults[0], doubleResults[1]
        if hasDouble:
            hands[key] = int(doubleValue) + 13
        else:
            hands[key] = max(nummedHand)
    return max(hands)
        
