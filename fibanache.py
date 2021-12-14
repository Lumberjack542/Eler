a = 0
b = 1
i = 0
list = []
while i >= 0:
    c = a + b
    a = b
    b = c
    c = a + b
    i += 1
    #print(c)
    if c >= 4000000:
        break
    elif c % 2 == 0:
        list.append(c)
#print(list)
print(sum(list))
