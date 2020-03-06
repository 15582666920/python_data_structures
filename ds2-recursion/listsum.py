"""
[1,3,5,7,9]
"""


#
# def listSum(numList):
#     sum = 0
#     for i in numList:
#         sum = sum + i
#     return sum
#
#
# print(listSum([1, 3, 5, 7, 9, ]))
#
#
# # 不能使用while for
# def listSum2(numlist):
#     sum=0
#     if len(numlist) ==1:
#         return numlist[0]
#     else:
#         return numlist[0]+listSum2(numlist[1:])
#
#
# print(listSum2([1, 3, 5, 7, 9 ]))

def tostr(n, base):
    str1 = '0123456789ABCDEF'
    if n < base:
        return str1[n]
    else:
        return tostr(n // base, base) + str1[n % base]


print(tostr(7, 2))
