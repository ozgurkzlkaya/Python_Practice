def func():             #FONKSİYON OLUŞTURURKEN 'DEF' KULLANIRIZ
    print(func)

def my_func(username):   #'USERNAME' PARAMETRE
    print(f'Hello {username}')

my_func('Arin')  #'ARİN' ARGÜMAN
#Fonksiyona argüman vermediğimiz takdirde parametreye varsayılan bir değer vermemiz gerekiyor
"""
____________________________________
"""
def function(username, age=25):
    print(f'Merhaba {username}, {age} yaşındasınız')

function('Arin')

"""
____________________________________
"""
def func1():
    return 8 + 10

def func2():
    print(4 + 10)

func1()
func2()
#'Func1' fonksiyonunu döndürdük fakat yazdırmadık herhangi bir işlem gerçekleşmez
"""
_____________________________________
"""
def funcc1():
    return 8 + 10

def funcc2():
    print(4 + 10)

result1 = funcc1()
result2 = funcc2()

print(f'Result 1 , {result1}')
print(f'Result 2, {result2}')

#RETURN'LADIĞIMIZ DEĞERİ RESULT'A ATADIĞIMIZ İÇİN DAHA SONRASINDA YAZDIRABİLDİK
#FAKAT FUNC2'DEKİ DEĞERİ YAZDIRDIĞIMIZ İÇİN RESULT 2'YE HERHANGİ BİR DEĞER ATAYAMADIK
"""
_____________________________________
"""
def funcc3():
    pass

funcc3() 
#FONKSİYONUN İŞLEM YAPMAMASINI İSTEDİĞİMİZ ZAMAN PASS KEYWORDUNU KULLANIRIZ