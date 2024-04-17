# функции поиска линейный и бинарный
# + счетчик 

def get_block_by_index_linear(number, spisok):
    if not spisok:
        return None
    # if not number:
    #     return None
    counter = 0
    index = None
    for i in range(len(spisok)):
        counter += 1
        if spisok[i]['index'] == number:
            index = i
            break
    print('Счетчик: ',counter)
    return index


def get_block_by_index_binary(number, spisok): 
    if not spisok:
        return None
    first = 0
    last = len(spisok) - 1
    counter = 0

    if spisok[first]['index'] == number:
        print('Счетчик: ',counter)
        return first
    if spisok[last]['index'] == number:
        print('Счетчик: ',counter)
        return last
    
    while (first != last):
        counter += 1
        middl = (last + first) // 2

        if spisok[middl]['index'] == number:
            print(counter)
            return middl
        if spisok[middl]['index'] > number:
            last = middl - 1
        else:
            first = middl + 1
    else:
        print('Счетчик: ',counter)
        return None
    


