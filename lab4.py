


import json
import os

# подключение файла с функциями поиска
import poisk
# подключение файла с функциями сортировки
import sort


arr = os.listdir('transactions')

spisok =[]
for i in arr:
    with open(f"transactions/{i}","r") as file:
        spisok.append(json.loads(file.read()))


spisok = sorted(spisok, key = lambda x:x['index'])   #сортировка

# number = int(input())
# print(poisk.linPoisk(number, spisok))

# for i in spisok:
#     print(i['index'])

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

# print("Все форки в системе, их начало и конец  - ",*forks)


{'index': 99, 
 'pre_hash': '000e0ef49a7bc2750fb1eaa7739a050232e300d92e242bb442226aa7251c6bf1cea0228084fc704e27ae42ddbf40fae31a228281cd6674ad661d23d6d273ce35', 
 'timestamp': 1649168284, 
 'transactions': [{'from': 'Jon', 'to': 'Ivan', 'value': 417.398}, 
{'from': 'Ivan', 'to': 'Tina', 'value': 232.146}, 
{'from': 'Harry', 'to': 'Victor', 'value': 65.423}, 
{'from': 'SYSTEM', 'to': 'Oliver', 'value': 0.69}],
'secret_info': '', 'nonce': 4243,
'hash': '000db7795a1ec51217e24246e264cb7b6227d3ec0f87fdd4dc165418f82ac2930108f5182e31c36df7394d5776cab559320a0bd10808b19d21303b42edc8767f'}

# средний перевод блока в транзакциях
midlSumValue = []
for i in range(1,len(spisok)):
    ss = 0
    for j in range(len(spisok[i]['transactions']) - 1):
        ss += spisok[i]['transactions'][j]['value']
    ss = ss/(len(spisok[i]['transactions']) - 1)
    midlSumValue.append([spisok[i]['index'], ss])

# вывод средней суммы и номера блока

# for i in midlSumValue:
#     print(f"№{i[0]} среднее: {i[1]}")








countTransactions = []
sumCountTransactions = 0
for index in range(len(spisok)):
    countTransactions.append([spisok[index]['index'], len(spisok[index]['transactions'])])
    sumCountTransactions += len(spisok[index]['transactions'])

# for i in countTransactions:
#     print(f"№{i[0]} - кол-во транзакций: {i[1]} ")

# print('Всего транзакций во всех блоках -', sumCountTransactions)

namesSumValues = {}

for index in range(1,len(spisok)):
    if spisok[index]['transactions'][-1]['to'] in namesSumValues:
        namesSumValues[spisok[index]['transactions'][-1]['to']] += spisok[index]['transactions'][-1]['value']
    else:
        namesSumValues[spisok[index]['transactions'][-1]['to']] = spisok[index]['transactions'][-1]['value']

# вывод мейнера и суммы его награждений
for key in namesSumValues:
    print(key, namesSumValues[key])

# макс вознаграждение
maxSumValue = list(namesSumValues.items())[0][1]
for key in namesSumValues:
    if namesSumValues[key] > maxSumValue:
        maxSumValue = namesSumValues[key]

print("Макс вознаграждение",maxSumValue)


# мин вознаграждение
minSumValue = list(namesSumValues.items())[0][1]
for key in namesSumValues:
    if namesSumValues[key] < minSumValue:
        minSumValue = namesSumValues[key]

print("Мин вознаграждение",minSumValue)


# for i in spisok[0]['transactions']:
#     print(i)


# Сгруппировать блоки по часам и минутам,  и вывести количество элементов в каждой группе 


