print('Hello world!', end = "\n\n") 
#for index, value in enumerate(spisok):



# ss = [(elem['secret_info'],elem['index']) for elem in spisok if elem['secret_info'] != '']
# print(ss)

# bytearray.fromhex("str").decode

import re 
import json
import os

arr = os.listdir('transactions')

spisok =[]
for i in arr:
    with open(f"transactions/{i}","r") as file:
        spisok.append(json.loads(file.read()))

spisok = sorted(spisok, key = lambda x:x['index'])   # сортировка

# 0 => {
#  'index': 0, 
#  'pre_hash': '0x0', 
#  'timestamp': 1649168214, 
#  'transactions': [{'from': 'SYSTEM', 'to': 'Alice', 'value': 400}, 
#     {'from': 'SYSTEM', 'to': 'Bob', 'value': 400}, 
#     {'from': 'SYSTEM', 'to': 'Sam', 'value': 400}, 
#     {'from': 'SYSTEM', 'to': 'Tina', 'value': 400}, 
#     {'from': 'SYSTEM', 'to': 'Uwe', 'value': 400}],
#  'secret_info': '', 
#  'nonce': 7209, 
#  'hash': '00013fe63b19af3dc8ac14bcdbfdc5f78159c638bfa841f64abaa234b4a0fa1767e971a1902df139844493b397b0d6322fd1ecc7e04202caa912e22143fa6be4'}

#  forks = (17, 19) (29, 32) (35, 45) (79, 80)

# поиск форков 
forks =[]
startFork = 0
endFoerk = 0
for i in range(len(spisok)-3):

    if startFork == 0:
        if spisok[i]['index'] == spisok[i+1]['index']:
            startFork = spisok[i]['index']

    else:
        if spisok[i-1]['index'] != spisok[i]['index'] and spisok[i+1]['index'] != spisok[i]['index']:
            endFoerk = spisok[i]['index'] - 1

            fork = (startFork,endFoerk)

            startFork = 0
            forks.append(fork)

print("Все форки в системе, их начало и конец  - ",*forks)
print()



# Вопрос 13.
# Полученное ранее значение является шестнадцатеричной формой представления ключевой строки. Строка имеет следующий формат: WSflag{_____}


sborSecretInfo = ''
for i in spisok:
    if i['secret_info'] != '':
            sborSecretInfo += i['secret_info']



print(sborSecretInfo)
            
keyString = bytearray.fromhex(sborSecretInfo).decode()

print(keyString)
            
# ss = sborSecretInfo.encode()
# print(ss)

# dd = bytearray(ss)

# print(dd)

# string = ss.decode()

# print(string)


# dd = 'king'
# ll  = list(dd)
# st = bytearray(map(int,ll)).encode('hex')
# print(st)
# ss = dd.encode()
# rt = bytearray.from(dd)
# rt = bin(rt)
# dd = dd.decode()
# print(rt)







