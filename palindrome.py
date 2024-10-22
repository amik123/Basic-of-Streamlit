# a=[1,1,1,1,22,2,2,2,2,3,3,3,3]
# b=a.count(1)
# print(b)
# c={x:a.count(x) for x in a }
# print(c)


# #check if the string is palindrome or not
# temp=list(input("Enter your string"))
# if temp==temp[::-1]:
#     print('Palindrome')
#     print(temp)
# else:
#     print('Not palindrome')

temp=input("Enter your string\t")
x=len(temp)
y=[]
while x!=0:
    y.append(temp[x-1])
    x-=1
print(y)




