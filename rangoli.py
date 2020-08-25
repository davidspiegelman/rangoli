def print_rangoli(size, d="-"):
    s = size - 1
    f = lambda y: (y - abs(x) for x in range(y , -y - 1, -1))
    p = lambda r: chr(97 + (s - r) % 26)
    _ = [print(d.join((b := [d] * (s - i)) + [p(x) for x in f(i)] + b)) for i in f(s)]
    
