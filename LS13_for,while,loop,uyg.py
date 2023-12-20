"""
friends = ['ahmet','mehmet','ebru','mahmut','ayşe'] listesindeki mahmut hariç diğer elemanları while ve for loop kullanarak yaz
"""

friends = ['ahmet','mehmet','ebru','mahmut','ayşe']
x = 0
while (x < len(friends)):
    friend = friends[x]
    x = x+1
    if friend == 'mahmut':
        continue
    print(friend)

#For'lu hali
for friend in friends:
    if friend == 'mahmut':
        continue
    print(friend)

"""
Kullanıcı tarafından girilen 2 rakam arasındaki çift sayıların çıktısını alın
"""
minNum = int(input('Lütfen minimum sayıyı giriniz: '))
maxNum = int(input('Lütfen maksimum sayıyı giriniz: '))

for evenNum in range(minNum, maxNum):
    if evenNum % 2 != 0:
        continue
    else:
        print(evenNum)
        
"""
While döngüsünü kullanarak 1 ile 100 arasında sayı tahminlerini yapabileceğiniz bir program yazın

import random
xnum = random.randint(1,100)
print(xnum)

"""

import random
xnum = random.randint(1,100)

num = int(input('Lütfen 1 ile 100 arası bir sayı giriniz: '))
while num != xnum:
    if num < xnum:
        print(f'{num} daha büyük bir sayı girin')
        num = int(input())
    else:
        print(f'{num} daha küçük bir sayı girin')
        num = int(input())

print(f' Tebrikler {num} yakaladınız!') 

"""
celciuses = [20, 25, 30, 35] derecelerini kelvin ve fahrenheit olarak iki ayrı liste halinde gösterin
K = C + 273
F = C * 9 / 5 + 32
"""
celciuses = [20, 25, 30, 35]
kelvin = []
fahrenheit = []

for c in celciuses:
    k = c + 273
    kelvin.append(k)
    f = c * 9 / 5 + 32
    fahrenheit.append(f)

print(kelvin)
print(fahrenheit)

"""
Kullanıcıdan bir sayı girişi isteyelim ve o sayı ve öncekilerin toplamını yaz
"""

num1 = int(input('Lütfen bir sayı giriniz: '))
if num1 < 0:
    print('Negatif bir sayı girdiniz')
else:
    sum = 0
    while num > 0:
        sum += num1
        num-= 1
        print('Toplam sayı: ', sum)