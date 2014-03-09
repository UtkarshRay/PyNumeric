import math

# trapezint1: approximates the result of
# integrating f from a to b
# f is the function to integrate
# a is lower limit, b is upper limit
# intervals taken is 1000000 as best tradeoff between accuracy and speed
def trapezint1(f, a, b):
    step = (b - a)/1000000.0
    val = 0
    while (a < b):
        val += 0.5 *  step * (f(a) + f(a + step))
        a += step
    return val
    
def main():
    print('trapezint1(math.cos, 0, math.pi)')
    print(trapezint1(math.cos, 0, math.pi))
    print('trapezint1(math.exp, 0, math.log(3))')
    print(trapezint1(math.exp, 0, math.log(3)))
    print('trapezint1(math.sin, 0, math.pi)')
    print(trapezint1(math.sin, 0, math.pi))
    print('trapezint1(math.sin, 0, 0.5 * math.pi)')
    print(trapezint1(math.sin, 0, 0.5 * math.pi))
    
if __name__ == '__main__':
    main()
    input('Press enter to exit...')


# Output obtained by running this program
# trapezint1(math.cos, 0, math.pi)
# -3.14158110876e-06
# trapezint1(math.exp, 0, math.log(3))
# 2.0
# trapezint1(math.sin, 0, math.pi)
# 2.0
# trapezint1(math.sin, 0, 0.5 * math.pi)
# 1.00000157079
