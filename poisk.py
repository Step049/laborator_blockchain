# функции поиска линейный и бинарный

def linPoisk(number, ss):
    if not ss:
        return None
    
    a = [ blockNum for blockNum in range(len(ss)) if ss[blockNum]['index'] == number  ]
    if not a:
        return None
    else:
        return a[0]
    


def binPoisk(number, ss): # ну вроде как работает с транзанкциями
    if not ss:
        return None
    first = 0
    last = len(ss) - 1

    if ss[first]['index'] == number:
        return first
    if ss[last]['index'] == number:
        return last
    
    while (first != last):

        middl = (last + first) // 2

        if ss[middl]['index'] == number:
            return middl
        if ss[middl]['index'] > number:
            last = middl - 1
        else:
            first = middl + 1
    
    return None
    


