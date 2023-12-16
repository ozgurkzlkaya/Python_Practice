monster_1 = {'name': 'guru', 'power': 10, 'color': 'red'}
my_friend = {'name': 'deniz', 'age': 40, 'gender': 'woman'}
print(monster_1)
print(monster_1['name'])
print(monster_1['power'])
print(type(monster_1))

#Eleman ekleme
monster_1['position'] = 100
print(monster_1)

print(monster_1.get('boy'))   #Listede olmayan bir değer 'None' olur çıktısı

monster_1.update({'name': 'GURU', 'power': 20 })
print(monster_1)

del monster_1['color']   #Silme
print(monster_1)

poplan = monster_1.pop('power')  #'Pop' yöntemi ile silip, sildiğimiz elemanı geri çağırma
print(monster_1)
print(poplan)

print(len(monster_1))   #Uzunluk

print(monster_1.keys())  #Key değerleri

print(monster_1.values())  #Value değerleri

print(monster_1.items())  #Key ve Value değerleri

for key in monster_1:  #Key'ler döner
    print(key)

"""
-----------------------------------------------------------------------------
"""
my_friends = [
    {'name': 'deniz', 'age': 40},
    {'name': 'ahmet', 'age': 41}
]

print(my_friends[0]['age'])