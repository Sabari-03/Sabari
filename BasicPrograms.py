# print("Hello world")
# sabari = "Hai my name is sabari"
# sabari = "im naveen"
# sabari = 22
# print(type(sabari),sabari)
# sabari = "22"
# naveen = "44"
# print(sabari+naveen)
# print(int(sabari)+float(naveen))
# sab = "Naveen"
# nav = "kumar"
# print(sab + " " + nav)
# sabari = int(input("Enter your name"))
# print(int(sabari))
# print(type(sabari))
# sabari = int(input("Enter the number pls"))
# sabari1 = input("Enter the String")
# print(str(sabari)+" "+sabari1)
# a = 10
# b = 20
# print(a+b)
# print((a-b)*-1)
# print(a*b)
# print(b%a)
# print(b/a)
# print(b//a)
# a = 20
# b = 10
# if a == b :
#     print("They are equal")
# # elif a > b :
# #     print("A is Greater than B")
# elif b > a :
#     print("B is Greater than A")
# else :
#     print("Out of Bound")
# a = input("Enter the string")
# b = input("Enter the string")
# c = type(a)
# print(c)
# if type(a) == int and type(b) == int :
#     print("both are int")
# elif type(a) == int or type(b) == int :
#     print("a or b is int")
# else :
#     print(" are not int")
# def findOddOrEven(n) :
#     if n % 2 != 0:
#         return "wierd"
#     else:
#         if n >= 2 and n <= 5:
#             return "Not Weird"
#         elif n >= 6 and n <= 20:
#             return "Weird"
#         else:
#             return "Not Weird"
# n = int(input("enter the number :"))
# ans = findOddOrEven(n)
# print(ans)
# name = 10
# ss = findOddOrEven(name)
# print(ss)

def calculator(a,b,c):
    if c == "+":
        d = int(a) + int(b)
        return "d = {0}".format(d)
    elif c == "-":
        d = int(a) - int(b)
        if d < 0:
            d = d * -1
            print("d = {0}".format(d))
        elif d > 0:
            print("d = {0}".format(d))
        else:
            print("d = 0")
    elif c == "*":
        print(int(a) * int(b))
    else:
        print("Unidentified Symbol")

a = input("Enter Value")
b = input("Enter Value")
c = input("Enter Symbol")
print(calculator(a,b,c))
# print(ans)