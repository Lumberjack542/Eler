
list = []
for i in range(1, 1000):
    for k in range(1, 1000):
        c = i * k
        #print(c)
        c_rev = "".join(reversed(str(c)))
        if str(c) == c_rev:
            list.append(c)
print(max(list))
