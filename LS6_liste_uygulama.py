# 1 - Verilen listenin ikinci ve son liste elemanının çıktısını büyük harfle al
dersler = ['matematik', 'fizik','ingilizce','türkçe'] 
print(dersler[1].upper())
print(dersler[3].upper())
print(dersler[-1].upper())   #-1. indiste 4. indiste LİSTENİN SON ELEMANINI VERİR
"""
----------------------------------------------------------------------------
"""
# 2 - Fizik ve Kimya elemanlarının çıktısını al 
# 3 - İlk iki elemanın çıktısını al 
# 4 - Son iki elemanın çıktısını al
dersler2 = ['matematik', 'fizik', 'kimya','ingilizce','türkçe']
print(dersler2[1:3])

print(dersler2[:2])

print(dersler2[-2:])
"""
-----------------------------------------------------------------------------
"""
#LİSTE İÇİNDE LİSTE KULLANIMINA (İÇ İÇE LİSTE) 'NESTED LİST' DENİR.

# 5 - Fizik ve Kimya birlikte varsa ayrı ayrı çıktısını al
# 6 - Son elemanın çıktısını 'LEN' yardımı ile al

dersler3 = ['matematik', ['fizik','kimya'],'ingilizce','türkçe']
print(dersler3[1][0])
print(dersler3[1][1])

print(dersler3[len(dersler3)-1])

"""
------------------------------------------------------------------------------
"""
# 7 - Listenin uzunluğunu göster
# 8 - Tarih dersini listeye ekle
# 9 - Coğrafya dersini listeye ekle 2. yol

dersler4 = ['matematik','fizik','kimya','ingilizce','türkçe']

print(len(dersler4))

print(dersler4.append('tarih'))
print(dersler4)

dersler4[len(dersler4):] = ['cografya']
print(dersler4)

"""
-------------------------------------------------------------------------------
"""
# 10 - Tarih dersini liste başına 'insert' ile ekle
# 11 - Coğrafya dersini 'insert' ile liste sonuna ekle

dersler5 = ['matematik','fizik','kimya','ingilizce','türkçe']

dersler5.insert(0, 'tarih')
print(dersler5)

dersler5.insert(len(dersler5), 'coğrafya')
print(dersler5)
"""
--------------------------------------------------------------------------------
"""
# 12 - Kimya dersini 'DEL' ile kaldır
# 13 - Türkçe dersini 'REMOVE' ile kaldır

dersler6 = ['matematik','fizik','kimya','ingilizce','türkçe']

del dersler6[2]
print(dersler6)

dersler.remove('türkçe')
print(dersler6)
"""
----------------------------------------------------------------------------------
"""
# 14 - Listeyi artacak ve azalacak şekilde sırala 

numbers = [8,4,5,1,6,9,2,7,3,10]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
"""
------------------------------------------------------------------------------------
"""
# 15 - İçteki listelerin son elemanlarıyla yeni bir liste oluşturalım

dersler7 = [['matematik','fizik'],['kimya','ingilizce'],['türkçe','tarih']]

dersleryedek = []
for ders in dersler7:
    dersleryedek.append(ders[-1])

print(dersleryedek)

"""
-------------------------------------------------------------------------------------
"""
# 16 - 1'den 10' a kadar olan sayıların karelerinden bir liste oluşturalım
# 17 - Aynı işlemi list comprehension ile yapalım

squares = [num**2 for num in range (1,11)]
print(squares)

"""
 BÖYLE DE YAZILABİLİR
   squares = []
for num in range (1,11):
    squares.append(num**2)

print(squares)
"""


