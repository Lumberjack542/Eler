
list1 = []
#list12 = [[] for _ in range(10)]
c = 0

for i in range(1, 1000000 + 1):
    c += i
print(c)
y = 1
while y <= c:
    if c % y == 0:
        list1.append(y)
    y += 1
print(len(list1))


#print(list12)

# for i in list12:
#     if len(i) >= 500:
#         print(i)
#         print(sum(i))
#         break

