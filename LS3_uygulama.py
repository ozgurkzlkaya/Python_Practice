a = 14
a = 4.2 
a = 7

print(a)
print(type(a))
  #EN SON YAZILAN DEĞER 'A' DEĞERİ İÇİN KABUL GÖRÜR



#SONUCU BULALIM (21)
print((8 - 4) * 5 + (5 % 2))


#ALAN VE ÇEVREYİ 2 ONDALIKLI OLARAK HESAPLAYIN (İMPORT MATH)
r = 5 
pi = 3.14159

print(2 * pi * r)
print(pi * r ** 2) #pi*r*r ve pi*(pow(r, 2)) ile eşittir
import math
print(2* math.pi*r) #TOPLAM ÇEVREYİ MATH KÜTÜPHANESİYLE BULDUK


#X SAYISININ TEK Mİ ÇİFT Mİ OLDUĞUNU BULALIM 
x = 21
if(x % 2 == 0):
    print('X bir çift sayıdır')
    
else: 
    print('X bir tek sayıdır')


#|4 - 7| * (4 + 7) = ?   YAZDIR
print(abs(4 - 7) * (4 + 7))


#TEXT'İ YAZDIR TİPİNİ VER 
text = 'Welcome to python code'
print(text)
print(type(text))


#İSİM YAZDIRMA
name = 'Özgür'
print('My name is ' + name)
print('My name is {}'.format(name))
print(f'My name is {name}')
 

#BOOLEAN
names = 'Özgür'
ages = 20
married = True
print(name, ages, married)


#KULLANICIDAN İSMİNİ AL BÜYÜK VE KÜÇÜK HARFLE YAZDIR
my_name  = input('İsminiz nedir? ')
print(my_name.upper())
print(my_name.lower())