'''
乱序字符串是指一个字符串只是另一个字符串的重新排列
前提：字符串由26个小写字母集合组成，长度相同
比如：python typhon head deah
目的： 写一个布尔函数（返回值是布尔值的函数）
        solutions1（'abcd','dbcd;）
'''


# 穷举法：排除 原因：如果字符串过长，

# 检查第一个字符串是否出现在第二个字符串中  O(n^2)
def solutions1(s1, s2):
    alist = list(s2)
    pos1 = 0
    flag = True

    while flag and pos1 < len(s1):
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
            pos1 = pos1 + 1
        else:
            flag = False
    return flag


# print(solutions1('abcd', 'abcd'))


# 计数和比较法
# 计算每个字符出现的次数
def solutions2(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        print(pos)
        c1[pos] += 1

    count = 0
    flag = True
    while count < 26:
        if s1[count] == c2[count]:
            count = count + 1
        else:
            flag = False
    return flag


# print(solutions2('abcd', 'bacd'))

#  排序和比较：即使s1 s2 不同，他们都是有完全相同的字符组成
# 我们可以按照a-z排列每一个字符串，如果两个字符串相同，那这两个字符串就是乱序字符串
def solutions3(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    # 排序
    alist1.sort()
    alist2.sort()
    flag = True

    pos = 0

    while pos < len(s1) and flag:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            flag = False

    return flag
print(solutions3('abcd', 'bacd'))
