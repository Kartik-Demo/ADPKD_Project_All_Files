def polygon(L,n):
    angle=int(360/n)
    for i in range(n):
        fd(L)
        lt(angle)
    return
polygon(100,4)
polygon(100,6)
polygon(100,8)
speed(10)
for i in range(50):
    polygon(100,4)
    lt(10)
