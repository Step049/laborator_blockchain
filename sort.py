# сортировка пузырьком        
def sortBubble(spisok):
    for index in range(len(spisok)-1):
        for index2 in range(len(spisok)-index-1):
            if spisok[index2]['index'] > spisok[index2+1]['index']:
                spisok[index2]['index'], spisok[index2+1]['index'] = spisok[index2+1]['index'], spisok[index2]['index'] 
    return spisok

# сортировка выбором/отбором     

