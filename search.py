# # # def monday():
# # #     return "monday"
# # # def tuesday():
# # #     return "tuesday"
# # # def wednesday():
# # #     return "wednesday"
# # # def thursday():
# # #     return "thursday"
# # # def friday():
# # #     return "friday"
# # # def saturday():
# # #     return "saturday"
# # # def sunday():
# # #     return "sunday"
# # # def default():
# # #     return "Invalid day"
# # # switcher = {
# # #     1: monday,
# # #     2: tuesday,
# # #     3: wednesday,
# # #     4: thursday,
# # #     5: friday,
# # #     6: saturday,
# # #     7: sunday
# # # }
# # # def switch(dayOfWeek):
# # #     return switcher.get(dayOfWeek, default)()
# # # print(switch(1))
# # # print(switch(0))
# # def calc(len1) :
# #     list1 = []
# #     for i in range(0, len1, 1):
# #         a = int(input("Enter Number"))
# #         list1.append(a)
# #     odd = []
# #     even = []
# #     for i in range(0, len(list1), 1):
# #         if list1[i] % 2 == 0:
# #             even.append(list1[i])
# #         else:
# #             odd.append(list1[i])
# #     # print(odd)
# #     # print(even)
# #
# #     ans1 = sorted(odd)
# #     ans2 = []
# #     for i in range(len(ans1) -1, -1, -1): # This line cant able to understand . It is used to print the values in array in rev order
# #         ans2.append(ans1[i])
# #     print(ans2)
# #     print(sorted(even))
# #
# #
# # len1 = int(input("enter length"))
# # ans = calc(len1)
# #
# # #Go through the code plsss. Each line by line ok da. Go through the parameter pass da
# # # plss check y i used print instead of return
#
#
#
# #i will explain with example. Ok
# # ok done
# ans1 = [1,2,3,4]
# ans2 = []
# for i in range(0, len(ans1) , 1):
#     ans2.append(ans1[i])
# print(ans2)
# # # plsss check the process this -1,-1,-1 y we are using. is it understandable hmm da
# # Pls print this forward then backward
#
# # The output should be
# # Naveen
# # Kumar
# # Sabari
# # Nath
# # ok done
# # list1 = ["Naveen", "Kumar", "Sabari", "Nath"]
# # for i in range (0, len(list1), 1):
# #     # list2.append(list1[i])
# #     print(list1[i])
# #     # Dinner poitu varan ok va okok

# 1 Print elements one by one present in a list
# a = [1,2,3,4,5]
# for i in range(0, len(a), 1):
#     print(a[i])
# 2 Print a range with given a and b
# a = int(input("Enter number"))
# b = int(input("enter number"))
# for i in range(a+3 ,b-2 ,1) :
#     print(i)

# # 3 Print 13 table with 10
# a = int(input("Enter a number"))
# b = int(input("Enter a range"))
# for i in range(1, b+1, 1) :
#     print(i,"*",a,"=",i*a)
# # 4 append empty list with given range with getting input
# ans1 = int(input("Enter a range"))
# ans2 = ["nav",1]
# for i in range(0, ans1 , 1):
#     a = input("Enter name")
#     ans2.append(a)
# print(ans2)
# print(len(ans2))
# print(type(ans2[0]))
# 5.break and continue(create a list with fruits, if "" == list in fruit break, continue
# list1=["banana","apple","orange","grap"]
# for i in list1:
#     if i == "orange":
#         continue
#     print(i)
# list1=["banana","apple","orange","grap"]
# for i in list1:
#     if i == "orange":
#         break
#     print(i)
# def sab(n) :
#     x = int(input("Enter a range "))
#     b =  [ ]
#     for i in range(0, x, 1):
#         a = input("Enter name")
#         b.append(a)
#     for i in range (0, len(b), 1):
#         if n == b[i]:
#             return i
#     else:
#         return "not found"
#
# n = input("enter string")
# ans=sab(n)
# print(ans)
#
def lenier(a,b) :
    c = []
    c1 = []
    for i in range(0, b, 1):
        d = input("Enter a input")
        c.append(d)
    print(c)
    for i in range(1, 8, 1):
        print(c[i])
        c1.append(c[i])
    print(c1)

    for i in range(0, len(c1), 1):
        if c1[i] == a:
            print(i)
            break
    else:
        if len(c) > 0:
            for i in range(0, len(c), 1):
                if c[i] == a:
                    print(i)
                    break
            else:
                print("Not found")
a = input("Enter a string")
b = int(input("enter a range"))
lenier(a,b)