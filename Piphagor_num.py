a1 = 0
b1 = 0
c1 = 0
for c in range(1, 1000):
    for b in range(1, 1000):
        for a in range(1, 1000):
            if a < b < c:
                if c ** 2 == a ** 2 + b ** 2:
                    a1 = a
                    b1 = b
                    c1 = c
                    k = a1 + b1 + c1

                    if k == 1000:
                        print(a1, b1, c1)
                        print(a1 * b1 * c1)

