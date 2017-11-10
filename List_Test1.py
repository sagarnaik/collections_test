def common(list1):
    new_d =list1[0]
    for i in list1:
        #print(i)
        for k, v in i.items():
            if k in new_d.keys():
                new_d[k] = v
    return new_d

list1 = [{'a':1,'b':2},{'a':1,'b':2,'c':3},{'a':1,'b':2,'d':4, 'c':3}]
a = common(list1)
print (a)

