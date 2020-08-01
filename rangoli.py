def print_rangoli(size, d="-", p=lambda q, r: chr(97 + (q - r) % 26)):
    f, s = lambda y: (y - abs(x) for x in range(y , -y - 1, -1)), size - 1
    _ = [print(d.join((b := [d] * (s - i)) + [p(s, x) for x in f(i)] + b)) for i in f(s)]
