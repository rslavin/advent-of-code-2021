input = list(map(lambda l: (l, int(l.strip()[-1])), open('day2.in')))

y = [sum(x) for x in zip(*map(lambda i: (0, i[1]) if i[0][0] == 'f' else ((0 - i[1] if i[0] > 'f' else i[1]), 0), input))]
print(y[0] * y[1])

a = d = h = 0
for i, j in input:
    if i[0] == 'd':
        a += j
    elif i[0] == 'u':
        a -= j
    else:
        h += j
        d += (a * j)

print(d * h)
