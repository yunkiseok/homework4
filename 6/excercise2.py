def gugudan(n):
    if n % 2 == 0:
        return gugudan_even()
    else:
        return gugudan_odd()

def gugudan_even():
    for i in range(2, 10, 2):
        for p in range(1, 10):
            print("%d x %d = %d" % (i, p, i*p))
def gugudan_odd():
    for i in range(1, 10, 2):
        for p in range(1, 10):
            print("%d x %d = %d" % (i, p, i*p))

gugudan(2)
gugudan(5)


