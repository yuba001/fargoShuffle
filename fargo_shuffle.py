#implement the fargo shuffle and find  the minimum number of shuffle
#required to achieve the original arranement

def faro_cycles(deck_size):
    if deck_size == 2:
        return 1
    else:
        allcards = list(range(1,deck_size+1))
        newList = faro_shuffle(allcards)
        #print(allcards)
        #print(newList)
        n_cycles = 1
        while (allcards != newList):
            newList = faro_shuffle(newList)
            n_cycles += 1
        return n_cycles

def faro_shuffle(card_list):
        setA = card_list[:int(len(card_list)/2)]
        setB = card_list[int(len(card_list)/2):]
        # print(setA)
        # print(setB)
        newList = []
        for i in range(0, len(setA)):
            newList.extend([setA[i],setB[i]])
        return newList



print(faro_cycles(52))
