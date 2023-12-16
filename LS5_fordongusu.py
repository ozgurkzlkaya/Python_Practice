cities = ['tokyo', 'madrid', 'londra', 'kiev']
print(cities.index('madrid'))   #Madrid'in indeks numarasını verir
print(cities.index('ankara'))   #İs not in list hatası alırız
print('ankara'in cities)  #Ankara'nın liste yapısı içerisinde olup olmadığını kontrol eder

for city in cities:  #For döngüsü için CİTY adlı değişken ürettik
    print(city)      #For döngü kullanımı

for cc in cities:
    print(f'Gezilen şehir: {cc}')    #For döngüsü kullanımı


str_cities = 'İstanbul, Hongkong, Rias'
my_list = str_cities.split(', ')
print(my_list)             #Liste şeklinde yazdırma

for number in range(1,10):  #1'den 10'a kadar yazdır
     print(number)
     

for numb in range (2,21,2):  #21'e kadar olan çift sayıları yazdır
    print(numb)

numbs = list(range(1,11))    #Liste şeklinde yazdırma
print (numbs)

numbss = [numbe for numbe in range(1,11)]  #Liste şeklinde yazdırma
print (numbss)

cityy = ['izmir', 'ankara', 'istanbul']  #Liste kopyalama
print(cityy)
cityy2 = cityy
print(cityy2)
cityy.append('artvin')            #Listeye eleman ekleme
print(cityy)
print(cityy2)

