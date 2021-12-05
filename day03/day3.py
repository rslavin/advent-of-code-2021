input = open('day3.in').read().split()
g = ''.join(['1' if c.count('1') > len(input) / 2 else '0' for c in zip(*input)])
e = int(''.join('1' if x == '0' else '0' for x in g), 2)

print(int(g, 2) * e)

def o(b, l, p=0):
    c = 0
    if len(l) != 1:
        for j in l:
            if j[b] == '1':
                c += 1
        if p:
            search = '1' if c < len(l) / 2 else '0'
        else:
            search = '1' if c >= len(l) / 2 else '0'
        return o(b+1, list(filter(lambda x: x[b] == search, l)), p)
    return l[0]

print(int(o(0, input),2) * int(o(0, input, 1), 2))
