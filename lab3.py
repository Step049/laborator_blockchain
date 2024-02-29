import re 
import json
import os

print("Практическая работа №1")

arr = os.listdir('transactions')

spisok =[]
for i in arr:
    with open(f"transactions/{i}","r") as file:
        spisok.append(json.loads(file.read()))

spisok = sorted(spisok, key = lambda x:x['index'])   #сортировка

print("Вопрос 1")

# Укажите автора и номер блока, хэш которого имеет вид 0х000.......000 

pattern = '000.*000$' # шаблон для проверки хэша

for i in spisok:
    ex = str(i['hash'])
    match = re.search(pattern,ex)
    if match != None:
        print(f"Сам хэш  -  {i['hash']} \nНомер, он же индекс  -  {i['index']} \nАвтор  -  {i['transactions'][-1]['to']}")
print()


print("Вопрос 2")

# Укажите длину наименьшего форка в системе.

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
# мин длина форка в системе
minLongFork = forks[0][1] - forks[0][0] + 1

# номер первого блока в мин форке
blok_1_MinFork = forks[0][0]

# поиск мин длины форка и его певого блока
for i in forks:
    if (i[1] - i[0] + 1) < minLongFork:
        minLongFork = (i[1] - i[0] + 1)
        blok_1_MinFork = i[0]

print("Длина наименьшего форка в системе: ",minLongFork)
print()


print("Вопрос 3")

# Укажите номер первого блока в форке наименьшей длины.

print("Номер первого блока в форке наименьшей длины:  ",blok_1_MinFork)
print()


print("Вопрос 4")

# Укажите длину наибольшего форка.

# мax длина форка в системе
maxLongFork = forks[0][1] - forks[0][0] + 1


# поиск max длины форка 
for i in forks:
    if (i[1] - i[0] + 1) > maxLongFork:
        maxLongFork = (i[1] - i[0] + 1)
        numbLastBlok = i[1]

print("Длина наибольшего форка в системе:  ",maxLongFork)
print()


print("Вопрос 5")

# Укажите хэш последнего блока в отброшенной ветке форка наибольшей длины.
# проверка по timestamp у отброшенного форка он больше

# Первый способ через цикл - нахождения блоков с индексом последнего отброшенного форка макс длины 

lastBloks = []

# for i in range(numbLastBlok, len(spisok) - 1):

#     if len(lastBloks) == 2:
#         break

#     if spisok[i]['index'] == numbLastBlok:
#         lastBloks.append(spisok[i])

# Второй способ через filter - нахождения блоков с индексом последнего отброшенного форка макс длины 

lastBloks = list(
    filter(
        lambda block: block['index'] == numbLastBlok,
        spisok
    )
)

if lastBloks[0]['timestamp'] > lastBloks[1]['timestamp']:
    print("Последний блок в отброшенной ветке форка наибольшей длины:\n")
    print(lastBloks[0])
else:
    print("Последний блок в отброшенной ветке форка наибольшей длины:\n")
    print(lastBloks[1])

print()        


print("Вопрос 6")

print("Количество форков в системе:  ", len(forks))
print() 


print("Вопрос 7")

# Укажите размер вознаграждения за создание блока #71.

block71 = list(
    filter(
        lambda block: block['index'] == 71,
        spisok
    )
)

print("Размер вознаграждения за создание блока #71:   ", block71[0]['transactions'][-1]['value'])
print()


print("Вопрос 8")

# Определите период сокращения размера вознаграждения за создание блока (каждые n блоков).

unicValue = spisok[1]['transactions'][-1]['value']

countValue = 1

kValue = 0

for i in range(1,len(spisok)-1):
    if spisok[i]['index'] != spisok[i+1]['index']:
        if spisok[i]['transactions'][-1]['value'] == unicValue:
            countValue += 1
        else:
            kValue = spisok[i]['transactions'][-1]['value']/unicValue # k сокращения
            break
# округление до сотых 
kValue = round(kValue,2)

print("Период сокращения размера вознаграждения за создание блока (каждые n блоков) =  ", countValue)
print()

print("Вопрос 9")

# Определите коэффициент сокращения вознаграждения за выработку блока.
# (Округлить до сотых)

print("Коэффициент(округленный до сотых) сокращения вознаграждения за выработку блока:  ", kValue)
print()


print("Вопрос 10")

# Определите # блока, в котором в будущем размер вознаграждения впервые окажется равен 0,09

poiskValue = spisok[1]['transactions'][-1]['value'] #100

number009 = 0
flagKV = 0

while round(poiskValue,2) != 0.09:
    number009 += 1
    flagKV += 1

    if flagKV == 17:
        poiskValue = (poiskValue * kValue)
        flagKV = 0

print("Номер блока, в котором в будущем размер вознаграждения впервые окажется равен 0,09:  ",number009)
print()


print("Вопрос 11")

# Укажите блоки, в которых в поле secret_info встречается дополнительная информация, блоки откинутых форков не учитываются.

blocksNotEmpySecret =[]

sborSecretInfo = ''
for i in spisok:
    if i['secret_info'] != '':
        blocksNotEmpySecret.append(i['index'])
        sborSecretInfo += i['secret_info'] # 12 вопрос

print("Блоки, в которых в поле secret_info встречается дополнительная информация:  ",*blocksNotEmpySecret)
print()

print("Вопрос 12")

# Соберите полученную информацию в порядке ее появления в цепочке, укажите полученное значение.

# второй спсоб
# sborSecretInfo = ''.join([elem['secret_info'] for elem in spisok if elem['secret_info'] != ''])

print("Вся секретная информацияв порядке ее появления в цепочке: ", sborSecretInfo)
print()

print("Вопрос 13")

# Полученное ранее значение является шестнадцатеричной формой представления ключевой строки. Строка имеет следующий формат: WSflag{_____}


# keyString = bytearray.fromhex(sborSecretInfo).decode

# print(keyString)

