#Boş liste, tuple set ve dictionary oluştur
list1 = []
list2 = list ()
print(type(list1))
print(type(list2))

tuple1 = ()
tuple2 = tuple()
print(type(tuple1))
print(type(tuple2))

set2 = set()
print(type(set2))

dict1 = {}
dict2 = dict()
print(type(dict1))
print(type(dict2))

"""
___________________________________________________________________________________________________________________________________________
"""

#Değeri sayı olan 3 elemanlı bir dictionary oluştur, 2. sayıyı ve sayıların ortalamasını çıkar
friends = {'mahmut': 38, 'deniz': 29, 'ebru': 21}
print(friends['deniz'])

print(sum(friends.values()) / len(friends) )

"""
___________________________________________________________________________________________________________________________________________
"""

# 2 Okul arkadaşı ve numaralardan oluşan bir dict oluştur, başka bir arkadaşı ekle, ekli olan arkadaşı sil,
# 'UPDATE' ile bir arkadaşın numarasını değiştir ve yeni bir arkadaş ekle

friendss = {'mahmut': 345, 'ebru': 127,}
friendss['eren'] = 76  #ELEMAN EKLEME
print(friendss)

del friendss['mahmut']  #ELEMAN SİLME
print(friendss)

friendss.update( {'mahmut': 666, 'eren': 676} ) #ELEMANIN VALUESİNİ DEĞİŞTİRDİK, VE ELEMAN EKLEMESİ YAPTIK
print(friendss)

"""
___________________________________________________________________________________________________________________________________________
"""

#my_dict = {'odd_numbers': [1,2,3]}
#yukardaki dictionary yapısında bulunan tüm elemanların karesini alalım aynı dictionary yapısını update edelim

my_dict = {'odd _numbers': [1,2,3]}
my_dict['odd _numbers'] = [my_dict['odd _numbers'][0] ** 2, my_dict['odd _numbers'][1] ** 2, my_dict['odd _numbers'][2] ** 2]
#ELEMANLARIN KARESİNİ ALDIK

print(my_dict)

"""
___________________________________________________________________________________________________________________________________________
"""
#my_dict2 = {'even_numbers': [2,4,6,8,10,12,14,16]}
#yukardaki dictionary yapısında bulunan tüm elemanların karesini alalım aynı dictionary yapısını update edelim,
#bu sefer for döngüsüyle yapalım

my_dict2 = {'even_numbers': [2,4,6,8,10,12,14,16]}

for v in my_dict2.values():
    my_list = [] 
    for y in v:
         my_list.append(y**2)


my_dict2['even_numbers'] = my_list
print(my_dict2)

"""
___________________________________________________________________________________________________________________________________________
"""
#my_friendsss = {'ali' : 28, 'mahmut': 46, 'ebru': 34}

#keylerden bir liste oluştur, valuelardan bir liste oluştur ve valueler toplamını yaz

my_friendsss = {'ali' : 28, 'mahmut': 46, 'ebru': 34}
my_key_list = []
my_value_list = []

for k , v in my_friendsss.items():  #KEY VE VALUE MYF_FRİENDSSS LİSTESİNDEN DEĞERLERİNİ ALDIK
     my_key_list.append(k)
     my_value_list.append(v)

print(my_key_list)
print(my_value_list)
print(sum(my_value_list))

"""
___________________________________________________________________________________________________________________________________________
"""

#Dictionary comprehension ile 1'den 10'a kadar olan sayılar, sayıları key, kareleri value olacak şekilde tek satırda oluştur

numbersss = { x: x**2  for x in range(1, 11)}
print(numbersss)

"""
___________________________________________________________________________________________________________________________________________
"""