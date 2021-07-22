def triangle(a,b,c):
    if a+b < c or a+c < b or b+c < a:
        return -1
    else:
        s = (a + b + c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        return area