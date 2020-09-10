
def bounce(n):
    if n >= 0:
        print(n,)
        bounce(n - 1)

        if n != 0:
            print(n)



def bounce2(n):
    x = n

    if n < 0:
        print("Ange ett naturligt tal")
    else: 
        while n > 0:
            print(n)
            n -= 1
        while n <= x:
            print(n)
            n += 1

bounce(4)