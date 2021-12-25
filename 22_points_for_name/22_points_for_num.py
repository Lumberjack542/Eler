
with open('names.txt', 'r', encoding='utf-8') as f:
    list1 = [[] for _ in range(5163)]
    index_1 = 0
    for i in f.read().split(','):
        i = i.replace('"', "").lower()
        list1[index_1].append(i)
        index_1 += 1
    list1.sort()
    c = 0
    index_2 = 0
    for word in list1:
        for j in word[0]:
            c += ord(j) - 96
        list1[index_2].append(c)
        index_2 += 1
        c = 0
    index_3 = 0
    for i in enumerate(list1):
        list1[index_3].append(i[0])
        index_3 += 1
    sum_points = 0
    for i in list1:
        print(i[1], i[2])
        sum_points += int(i[1]) * int(i[2])
    print(sum_points)




