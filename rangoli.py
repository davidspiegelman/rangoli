def print_rangoli(size, d="-", p="abcdefghijklmnopqrstuvwxyz"):    
    p = (p * (((size - 1) // len(p)) + 1))[::-1][-size:]
    f = lambda y: (y - 1 - abs(x) for x in range(y - 1, -y, -1))
    for i in f(size):
        b = [d] * (size - 1 - i)
        print(d.join(b + [ p[x] for x in f(i + 1) ] + b))
        
