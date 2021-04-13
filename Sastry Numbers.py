import math
def is_sastry(n):
    x = len(str(n))
    a = 10**x
    c = n + 1
    b = n * a + c
    if n > 0:
        sr = int(math.sqrt(b))
    return sr*sr == b