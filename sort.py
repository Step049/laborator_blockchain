# сортировка пузырьком        
def sortBubble(spisok):
    counter = 0
    for index in range(len(spisok)-1):
        for index2 in range(len(spisok)-index-1):
            counter += 1
            if spisok[index2]['index'] > spisok[index2+1]['index']:
                spisok[index2]['index'], spisok[index2+1]['index'] = spisok[index2+1]['index'], spisok[index2]['index'] 
    print('Счетчик: ',counter)
    return spisok

# сортировка выбором/отбором     
def sortOtbor(spisok):
    counter = 0
    for index in range(len(spisok)):
        indMin = index
        for index2 in range(index, len(spisok)):
            counter += 1
            if spisok[index2]['index'] < spisok[indMin]['index']:
                indMin = index2
        spisok[index], spisok[indMin] = spisok[indMin], spisok[index]
    print('Счетчик: ',counter)
    return spisok
