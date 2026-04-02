from  math import sqrt
x1 = int(input("введите х начала: "))
x2 = int(input("введите х ИЗМЕНЕНИЕ: "))
h = int(input("ведите шаг: "))

for x in range(x1, x2+1, h):
    if x>=1:
        print("при х =", x, ", y =", x/sqrt(x))
    else:
        a = 0
        for k in range(1, 13):
            if x+k*k!=0:
                a += (2*k*x)/(x+k*k)

        if (sqrt(abs(x+a))) != 0:
            y = (a*x)/(sqrt(abs(x+a)))
            print("при х =", x, ", y =", y)
