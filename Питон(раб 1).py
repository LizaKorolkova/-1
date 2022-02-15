d = " Liza"
x = "19 лет"
l = (d + " ") * 5
print("я", d, "мне", x)
print(l)
print("Как вас зовут? Сколько вам лет?")
a = input()
b =int(input())
print("Привет", a ,)
if b>= 14 and b<=17 : print("ты очень молод")
if b>=18 and b<=25 : print("Скоро на пенсию")
c = a [::-1]
print(c)

print(a[2:-1])
print(a[-3:])
print(a[1:6])
y = len(a)
print(y)

suma = 0
mult = 1

while b > 0:
    digit = b % 10
    suma = suma + digit
    mult = mult * digit
    b = b//10
print(suma)
print(mult)


print(a.lower())
print(a.upper())

print(a.replace('',''))
if b<0 and b>150 : print("Ошибка")

print("Сколько будет 3+3*3?")
z = int(input())
if z == 12 :
    print("верно")
else :
    print("не верно")




