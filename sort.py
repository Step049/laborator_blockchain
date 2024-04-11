# сортировка пузырьком        
def sortBubble(spisok):
    coun = 0
    for index in range(len(spisok)-1):
        for index2 in range(len(spisok)-index-1):
            coun += 1
            if spisok[index2]['index'] > spisok[index2+1]['index']:
                spisok[index2]['index'], spisok[index2+1]['index'] = spisok[index2+1]['index'], spisok[index2]['index'] 
    print(coun)
    return spisok

# сортировка выбором/отбором     
def sortOtbor(spisok):
    coun = 0
    for index in range(len(spisok)):
        indMin = index
        for index2 in range(index, len(spisok)):
            coun += 1
            if spisok[index2]['index'] < spisok[indMin]['index']:
                indMin = index2
        spisok[index], spisok[indMin] = spisok[indMin], spisok[index]
    print(coun)
    return spisok
