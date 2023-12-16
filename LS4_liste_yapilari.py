cities = ['barcelona', 'floransa', 'istanbul', 'belgrad', 'tahran']

print(cities[0])  #N'inci indisi yazdırır
print(len(cities)) #İndis sayısını yazdırır
print(cities[0:2]) #0' dan 2. indise kadar yazdırır

cities[0] = 'tiflis' #0. indisi değiştirdik
print(cities)

cities.append('roma') #listenin sonuna 'roma' ekledik
print(cities)

cities.insert(2, 'warsaw') #2. indise 'warsaw' ekledik
print(cities)

del cities[0]    #0. indisteki elemanı sildik
print(cities)

cities.pop()     #sondaki elemanı sildik
print(cities)

cities2 = cities.pop() #SİLDİĞİMİZ ELEMANA YALNIZCA POP METODUYLA ULAŞABİLİRİZ
print(cities2)         #SİLDİĞİMİZ ELEMANI YAZDIRDIK

cities.remove('belgrad') #DEĞERİNİ BİLDİĞİMİZ ELEMANI SİLDİK
print(cities) 

cities.sort    #Listeyi alfabetik sıraya çevirir
print(cities)

cities.sort(reverse=True)  #Listeyi alfabetik sıranın tersine çevirir 
print(cities) 

print(sorted(cities))  #Listeyi geçiçi olarak alfabetik sıraya çevirir

