"""
练习 写一个函数 该函数需要一个列表喝我们正在搜索的项作为参数
并返回一个是否存在的布尔值， fonund=Flask
"""


def sequentialSearch(alist, item):
    fount = False
    pos = 0
    while pos < len(alist) and not fount:
        if alist[pos] == item:
            fount = True
        else:
            pos = pos + 1
    return fount


# testList = [1, 2, 3, 7, 23, 33, 40]
# print(sequentialSearch(testList, 40))
'''
升序[17,20,26,30,44,54,55,65,77,93]
假设寻找的项在列表中
假设寻找的项布置列表中，50
'''

#
# def orderredSequentialSearch(alist, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(alist) and not found and not stop:
#         if alist[pos] == item:
#             found = True
#         else:
#             if alist[pos] > item:
#                 stop = True
#             else:
#                 pos = pos + 1
#     return found
# testList=[17,20,26,30,44,54,55,65,77,93]
# print(orderredSequentialSearch(testList,50))
#
# def binarySearch(alist,item):
#     found=False
#     first=0
#     last=len(alist)-1
#     while first<=last and not found :
#         midpoint=(first+last)//2
#
#         if alist[midpoint]==item:
#             found=True
#         else:
#             if item<alist[midpoint]:
#                 last=midpoint-1
#             else:
#                 first=midpoint+1
#     return found
def binarySearch(alist,item):
    if len(alist)==0:
        return False
    midpoint=len(alist)//2
    if alist[midpoint]==item:
        return True
    else:
        if alist[midpoint]>item:
            return binarySearch(alist[:midpoint],item)

        else:
            return  binarySearch(alist[midpoint+1:],item)
a=[0,1,2,8,13,17,19,32,42]
print(binarySearch(a,13))