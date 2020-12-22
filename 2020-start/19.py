# coding:utf-8
'''
面试题 17.07. 婴儿名字
每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。
在结果列表中，选择字典序最小的名字作为真实名字。
示例：
输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
输出：["John(27)","Chris(36)"]
'''

import collections


def trulyMostPopular(names, synonyms):
    list1 = []
    for each in synonyms:
        a, b = each[1:-1].split(',')
        if list1 == []:
            list1.append([a, b])
        else:
            tag = 0
            for i in range(len(list1)):
                if a in list1[i]:
                    list1[i].append(b)
                    tag = 1
                    break
                elif b in list1[i]:
                    list1[i].append(a)
                    tag = 1
                    break
            if tag == 0:
                list1.append([a, b])
    dict1 = collections.OrderedDict()
    dict_res = collections.OrderedDict()
    for elem in names:
        str1, num1 = elem.split('(')[0], int(elem.split('(')[-1].split(')')[0])
        dict1[str1] = num1
    for each in list1:
        tag = ''
        for i in range(len(each)):
            if not dict_res:
                if each[i] in dict1:
                    dict_res[each[i]] = dict1[each[i]]
                    tag = each[i]
            else:
                if tag != '':
                    if each[i] in dict1:
                        dict_res[tag] += dict1[each[i]]
                else:
                    if each[i] in dict1:
                        dict_res[each[i]] = dict1[each[i]]
                        tag = each[i]
    list_res = []
    for key in dict_res.keys():
        list_res.append(key + '(' + str(dict_res[key]) + ')')
    return list_res

names = ["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"]
synonyms = ["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]
trulyMostPopular(names, synonyms)
