import math

def BiqEq(a):
    if (a[0] == 0 and a[1] == 0 and a[2] == 0):
        print("х ∈ R")
        return 0
    elif (a[0] == 0 and a[1] == 0 and a[2] != 0):
        print("х ∈ Ø")
        return 0
    elif (a[0] == 0 and a[1] != 0 and a[2] == 0):
        print("x=0")
        return 0
    elif (a[1] != 0 and a[1] == 0 and a[2] == 0):
        print("x=0")
        return 0
    elif (a[0] == 0 and a[1] != 0 and a[2] != 0):

        if (-a[2] / a[1] > 0):
            print("x = {}".format(math.sqrt(-1.0 * a[2] / a[1])))
            print("x = {}".format(-math.sqrt(-1.0 * a[2] / a[1])))
            return 0
        else:
            print("х ∈ Ø")
            return 0
    elif (a[0] != 0 and a[1] == 0 and a[2] != 0):

        if (-a[2] / a[0] < 0):
            print("х ∈ Ø")
            return 0
        else:
            if (-math.sqrt(-a[2] / a[0]) > 0):
                print(" x = {}".format(math.sqrt(-math.sqrt(-a[2] / a[0]))))
                print("x = {}".format(-math.sqrt(-math.sqrt(-a[2] / a[0]))))
                return 0

    else:
        d = a[1] * a[1] - 4 * a[0] * a[2]
        if (d == 0):
            if ((-a[1] / (2 * a[0])) == 0):
                print("x = 0")
                return 0
            elif ((-a[1] / (2 * a[0])) < 0):
                print("х ∈ Ø")
                return 0
            else:
                print("x = {}".format(math.sqrt(-a[1] / (2 * a[0]))))
                print("x = {}".format(-math.sqrt(-a[1] / (2 * a[0]))))
                return 0

        elif (d < 0):
            print("х ∈ Ø")
            return 0
        else:
            x1 = (-a[1] + math.sqrt(d)) / (2 * a[0])
            x2 = (-a[1] - math.sqrt(d)) / (2 * a[0])
            if (x1 > 0):
                print("x = {}".format(math.sqrt(x1)))
                print("x = {}".format(-math.sqrt(x1)))
            if (x2 > 0):
                print("x = {}".format(math.sqrt(x2)))
                print("x = {}".format(-math.sqrt(x2)))
            if (x1 == 0):
                print("x = 0")
            if (x2 == 0):
                print("x = 0")
                
print("Введите коэффициенты биквадратного уравнения")
while True:
    a = input().split()
    for i in range(3):
        try:
            a[i] = float(a[i])
        except:
            print("Введите коэффициенты заново")
            break
        if i == 2:
            BiqEq(a)
            exit()
