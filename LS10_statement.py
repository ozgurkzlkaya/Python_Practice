#Kullanıcıdan gelen herhangi bir sayının tek mi çift mi olduğunu göster
num1 = int(input('Lütfen bir sayı giriniz: '))

if num1 % 2 == 0:
    print(f'{num1} çift sayıdır')
else:
    print(f'{num1} tek sayıdır')

"""
_________________________________________________________________________________________
"""

#Kullanıcıdan gelen bir sayının pozitif, negatif veya 0'mı olduğunu kontrol edin

num2 = int(input('Lütfen bir sayı giriniz '))

if num2 == 0:
    print(f'{num} sayısı 0 dır')
elif num2 > 0:
    print(f'{num2} sayısı pozitiftir')
else:
    print(f'{num2} sayısı negatiftir')

"""
_________________________________________________________________________________________
"""


"""
x = 10, y = 5
if x > y: 
      print(f'{x} sayısı {y}/'den büyüktür')
      
      ifadesinin tek satır formunu yazın, else yapısıyla yine tek satırda yazın
    
"""
      
if x > y: print(f'{x} sayısı {y}\'den büyüktür') #TEK SATIRDA YAZILABİLİR

"""
_________________________________________________________________________________________
"""

#Kullanıcının girdiği herhangi bir sayının faktöriyelini bulun

numberssss = int(input('Lütfen bir sayı giriniz: '))
faktöriyel = 1
if numberssss < 0: print(f'{number} negatiftir')
elif numberssss == 0:
    print(f'{numberssss} sayısının faktöriyeli {faktöriyel}')
else:
    for x in range(1, numberssss+1):
        faktöriyel = faktöriyel * x
    print(f'{numberssss} sayısının faktöriyeli {faktöriyel}')
    
"""
_________________________________________________________________________________________
"""
# notes = {'ahmet': 58, 'mehmet': 76, 'ebru': 44, 'pınar': 90}
# 50 ve üzeri notu olan öğrenci için geçti diğerleri için kaldı çıktısını alın.

notes = {'ahmet': 58, 'mehmet': 76, 'ebru': 44, 'pınar': 90}

for key, value in notes.items():
    if value >= 50:
        print(f'{key} aldığı not {value} : GEÇTİ')
    else:
        print(f'{key} aldığı not {value} : KALDI')
