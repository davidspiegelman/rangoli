def print_rangoli(size, d="-", p="abcdefghijklmnopqrstuvwxyz"):    
    p = (p * (((size - 1) // len(p)) + 1))[::-1][-size:]
    f = lambda y: (y - abs(x) for x in range(y , -y - 1, -1))
    for i in f(s := size - 1):
        print(d.join((b := [d] * (s - i)) + [p[x] for x in f(i)] + b))
