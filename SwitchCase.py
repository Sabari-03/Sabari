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

1 Print elements one by one present in a list
a = [1,2,3,4,5]
for i in range(0, len(a), 1):
    print(a[i])
# 2 Print a range with given a and b

# 3 Print 13 table with 10
a = int(input("Enter a number"))
b = int(input("Enter a range"))
for i in range(1, b+1, 1) :
    print(i,"*",a,"=",i*a)
# 4 append empty list with given range with getting input
ans1 = int(input("Enter a number"))
ans2 = []
for i in range(0, len(ans1) , 1):
    ans2.append(ans1[i])
print(ans2)
5.break and continue(create a list with fruits, if "" == list in fruit break, continue
list1=["banana","apple","orange","grap"]
for i in list1:
    if i == "orange":
        continue
    print(i)
list1=["banana","apple","orange","grap"]
for i in list1:
    if i == "orange":
        break
    print(i)
