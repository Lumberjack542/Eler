list1 = []
for i in range(2, 101):
    for j in range(2, 101):
        list1.append(i ** j)
#list1 = sorted(list1)
print(len(list(sorted(set(list1)))))

