def ispower(num):
    """ispower
    """
    s = num**(1 / 2)

    return s == int(s)


for x in range(2020, 9999):
    if ispower(2 * x**2 - 2019**2):
        print((2 * x**2 - 2019**2, x**2, 2019**2, x,
               (2 * x**2 - 2019**2)**(1 / 2)))
