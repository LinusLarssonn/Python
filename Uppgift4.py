
def tvarsumman(n):
    if n == 0:
        return 0
    return n % 10 + tvarsumman(n//10)

print(tvarsumman(55))


def tvarsumman2(n):
    x = 0

    while n > 0:
        x = x + n % 10
        n = n//10
    print(x)
