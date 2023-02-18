li = [i for i in range(10)]
splitted = (li[i:i+4] for i in range(0,len(li),4))
for _ in splitted:
    print(_)


