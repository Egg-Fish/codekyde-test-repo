def quadratic():
    a = int(input("Enter an integer: "))
    b = int(input("Enter an integer: "))
    c = int(input("Enter an integer: "))
    roots = []
    if (b**2-4*a*c)>=0:
        r1 = (-b+(b**2-4*a*c)**1/2)/(2*a)
        r2 = (-b-(b**2-4*a*c)**1/2)/(2*a)
    if r1 == r2:
        roots.append(r1)
    else:
        roots.append(r2)
    return (roots)

if __name__ == '__main__':
    # put tests here and run this file
    print(quadratic(1, 2, 3)) # idk what this returns