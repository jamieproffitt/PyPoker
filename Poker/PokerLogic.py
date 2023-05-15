def checkDouble(nummedHand, communityHand):
    nummedCommunityHand = []
    for card in communityHand:
        nummedCommunityHand.append(card.Number)
    totalHand = nummedCommunityHand + nummedHand
    countedItems = {i:totalHand.count(i) for i in totalHand}
    duplicated = []
    for key, value in countedItems.items():
        if value > 1:
            duplicated.append(value)
        
    if not duplicated:              ## high card
        return (1, 0)
    elif len(duplicated) == 1:      ## pair
        return (0, duplicated[0])
    else:                           ## two pair
        return (2, duplicated)
        

def pokerMain(hands, communityHand):
    for key, hand in hands.items():
        nummedHand = []
        for card in hand:
            nummedHand.append(card.Number)
        doubleResults = checkDouble(nummedHand, communityHand)
        hasDouble, doubleValue = doubleResults[0], doubleResults[1]
        if hasDouble == 0: ## pair
            hands[key] = int(doubleValue) + 13
        elif hasDouble == 1: ## high card
            hands[key] = max(nummedHand)
        elif hasDouble == 2: ## two pair
            doubleValue = sum(duplicated.values()) + 13
    if int(hands[max(hands)]) < 14: ## high card
        return (max(hands), "High Card")
    elif int(hands[max(hands)]) >= 14 and int(hands[max(hands)]) < 40: ## pair
        return (max(hands), "Pair")
    elif int(hands[max(hands)]) >= 40: ## two pair
        return (max(hands), "Two Pair")
        
