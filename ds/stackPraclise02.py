# from pythonds.basic.stack import Stack
#
#
# def divide2(desNimber):
#     s = Stack()
#
#     while desNimber > 0:
#         rem = desNimber % 2
#         s.push(rem)
#         desNimber = desNimber // 2
#
#         binString = ''
#         while not s.isEmpty():
#             binString = binString + str(s.pop())
#         return binString
#
#
# print(divide2(7))
from pythonds.basic.stack import Stack


def dividebase(desNumber, base):
    digits='0123456789ABCDEF'
    s = Stack()

    while desNumber > 0:
        rem = desNumber % base
        s.push(rem)
        desNumber = desNumber // base
    binString = ''
    while not s.isEmpty():
        binString = binString + digits[s.pop()]
    return binString
print(dividebase(233,16))
