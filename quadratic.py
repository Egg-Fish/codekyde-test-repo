def quadratic(a,b,c):
    roots = []
    if (b**2-4*a*c)>=0:
        r1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
        r2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)
        if r1 == r2:
            roots.append(r1)
        else:
            roots = [r1,r2]
    return (roots)

if __name__ == '__main__':
    # put tests here and run this file
    print(quadratic(1, 5, 6)) # idk what this returns
    print(quadratic(1, 6, 8))
    print(quadratic(2, -8, -24))