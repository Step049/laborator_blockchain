# подключение файла с функциями поиска
# import poisk
# print(poisk.linPoisk(number, spisok))


import json
import os


arr = os.listdir('transactions')

spisok =[]
for i in arr:
    with open(f"transactions/{i}","r") as file:
        spisok.append(json.loads(file.read()))


# spisok = sorted(spisok, key = lambda x:x['index'])   #сортировка




# ss = [9,8,7,6,5,4,3,2,1,2,3,4,5,4,3]

# сортировка выбором/отбором






# sortOtbor(spisok)

for i in spisok:
    print(i['index'])



