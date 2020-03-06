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

# def tostr(n, base):
#     str1 = '0123456789ABCDEF'
#     if n < base:
#         return str1[n]
#     else:
#         return tostr(n // base, base) + str1[n % base]
#
#
# print(tostr(7, 2))
from pythonds.basic.stack import Stack

rStack = Stack()


def toStr(n, base):
    converString = '0123456789ABCDEF'

    while n > 0:
        if n < base:
            rStack.push(converString[n])
        else:
            rStack.push(converString[n % base])
        n = n // base
    res = ''
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res


print(toStr(7, 2))
