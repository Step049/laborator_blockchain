# функции поиска линейный и бинарный
# + счетчик 

def linPoisk(number, ss):

    if not ss:
        return None
    if not number:
        return None
    coun = 0

    for i in range(len(ss)):
        coun += 1
        if ss[i] == number:
            print(coun)
            return i


def binPoisk(number, ss): 
    if not ss:
        return None
    first = 0
    last = len(ss) - 1
    coun = 0

    if ss[first]['index'] == number:
        print(coun)
        return first
    if ss[last]['index'] == number:
        print(coun)
        return last
    
    while (first != last):
        coun += 1
        middl = (last + first) // 2

        if ss[middl]['index'] == number:
            print(coun)
            return middl
        if ss[middl]['index'] > number:
            last = middl - 1
        else:
            first = middl + 1

    print(coun)
    
    return None
    


