input = open('day3.in').read().split()
g = ''.join(['1' if c.count('1') > len(input) / 2 else '0' for c in zip(*input)])
e = int(''.join('1' if x == '0' else '0' for x in g), 2)

print(int(g, 2) * e)
