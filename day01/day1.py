i = list(map(int, open('day1.in')))
print(sum(b > a for a, b in zip(i, i[1:])))
j = list(sum(k) for k in zip(i, i[1:], i[2:]))
print(sum(b > a for a, b in zip(j, j[1:])))