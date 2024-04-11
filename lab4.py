


import json
import os

# подключение файла с функциями поиска
# import poisk
# подключение файла с функциями сортировки
import sort




arr = os.listdir('transactions')

spisok =[]
for i in arr:
    with open(f"transactions/{i}","r") as file:
        spisok.append(json.loads(file.read()))


# spisok = sorted(spisok, key = lambda x:x['index'])   #сортировка

# number = int(input())

# print(poisk.linPoisk(number, spisok))












sort.sortBubble(spisok)
 

# sort.sortOtbor(spisok)

for i in spisok:
    print(i['index'])


