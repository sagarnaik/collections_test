d=[{"a":1,"b":2,"c":3},{"a":1,"s":55,"b":10},{"a":1,"s":55},{"b":10,"s":55},{"x":10,"s":55},{"x":10,"s":55}]
newDict={}
for index in range(len(d)):
   # print(index)
    for index1 in range(index+1,len(d)):
        #print(index1)
        for key,val in d[index].items():
            for key1,val1 in d[index1].items():
                if key == key1 and val == val1:
                    newDict[key]=val

print(newDict)







