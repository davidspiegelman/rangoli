def print_rangoli(size, d="-", p="abcdefghijklmnopqrstuvwxyz"):    
    p = (p * (((size - 1) // len(p)) + 1))[::-1][-size:]
    f = lambda y: list(range(0, y)) + list(range(y - 2, -1, -1))
    for i in f(size):
        b = [d] * (size - 1 - i)
        print(d.join(b + list(map(lambda x: p[x], f(i + 1))) + b))
        
