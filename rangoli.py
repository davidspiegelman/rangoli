def print_rangoli(size, d="-", p="abcdefghijklmnopqrstuvwxyz"):    
    p = (p * (((s := size - 1) // len(p)) + 1))[::-1][-size:]
    f = lambda y: (y - abs(x) for x in range(y , -y - 1, -1))
    _ = [print(d.join((b := [d] * (s - i)) + [p[x] for x in f(i)] + b)) for i in f(s)]
