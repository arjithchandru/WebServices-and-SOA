import random
def standard_calculus(li):
    # observation = [1, 5, 4, 2, 0]
    observation = li
    # print (len(observation))
    sum = 0
    for i in range(len(observation)):
        # print(observation[i])
        sum += int(observation[i])
    # print(sum)
    mean_of_observations = float(sum / len(observation))
    # print(mean_of_observations)
    sum_of_squared_deviation = 0
    for i in range(len(observation)):
        # print(sum_of_squared_deviation)
        sum_of_squared_deviation += ((observation[i] - mean_of_observations) ** 2)
        print(sum_of_squared_deviation)
    Standard_Deviation = (((sum_of_squared_deviation) / len(observation)) ** 0.5)
    # print("Standard Deviation of sample is ", Standard_Deviation)
    return Standard_Deviation

def variance(data):
    # Number of observations
    n = len(data)
    # Mean of the data
    mean = sum(data) / n
    # Square deviations
    deviations = [(x - mean) ** 2 for x in data]
    # Variance
    variance = sum(deviations) / n
    return variance

# mathlog2-calculator

def gcd_function(a,b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
        print(a)
    return a

def lcm_function(arr):
        ans = arr[0]
        i = 1
    
        for i in range(len(arr)):
            ans = (
                    ((arr[i] * ans)) / (gcd(arr[i], ans))
            )
        return ans

def gcd(a, b):
    if (b == 0):
        return a
    else:
        a = int(a % b)
        return gcd(b, a)

# def find_sqroot(sq):
#     # sqnum = float(sq**())
#     # sq = float(sq)
#     sqnum = float(sq**0.5)
#     return sqnum

def Square(n, i, j):
    mid = (i + j) / 2
    mul = mid * mid
    if ((mul == n) or (abs(mul - n) < 0.00001)):
        return mid

    elif (mul < n):
        return Square(n, mid, j)
    else:
        return Square(n, i, mid)


def find_sqroot(n):
    n = int(n)
    i = 1;

    # While the square root is not found
    found = False;
    while (found == False):

        # If n is a perfect square
        if (i * i == n):
            # print(i);
            return i
            found = True;

        elif ((i * i) > n):

            # Square root will lie in the
            # interval i-1 and i
            res = Square(n, i - 1, i);
            # print("{0:.5f}".format(res))
            result = ("{0:.5f}".format(res))
            return result
            found = True
        i += 1;


def find_nsqroot(A, N):
    A = float(A)
    N = float(N)
    xPre = random.randint(1, 101) % 10
    eps = 0.001
    delX = 2147483647
    xK = 0.0

    while (delX > eps):
        Si = (((N - 1.0) * xPre) + A / pow(xPre, N - 1))
        xK = Si / N
        delX = abs(xK - xPre)
        xPre = xK

    return xK

def factorial_function(x):
    y = x
    # print (x,y)
    if x == 0:
        return 1
    else:
        for i in range(1,x):
            y = i * y
            # print (y)
    return y

def pi():
    pi = float(3.1415)
    return pi

def my_sin(theta):
    # print(pi())
    # degree = ()
    # theta = float(theta)

    theta = theta * (pi() / 180)
    # theta = math.fmod(theta + math.pi, 2 * math.pi) - math.pi
    d_theta = (theta+pi())%(2*pi())
    # print(d_theta)
    theta = d_theta - pi()
    # print(theta)
    result = 0
    termsign = 1
    power = 1

    for i in range(10):
        # print(i)
        # result += (math.pow(theta, power) / factorial_function(power)) * termsign
        result += ((theta**power) / factorial_function(power)) * termsign
        # dummypower = factorial_function(power)
        # print(dummypower)
        # dummy = (theta**power) /dummypower
        # print(dummy)
        # result += dummy * termsign
        # print(result)
        # print(power)
        termsign *= -1
        # print(termsign)
        power += 2
    return result

def my_cos(theta):
    theta = theta * (pi() / 180)
    # print(theta)
    # theta = math.fmod(theta + math.pi, 2 * math.pi) - math.pi
    d_theta = (theta + pi()) % (2 * pi())
    theta = d_theta - pi()
    result = 0
    termsign = 1
    power = 0
    # print(theta)
    for i in range(10):
        # result += (math.pow(theta, power) / math.factorial(power)) * termsign
        result += ((theta**power) / factorial_function(power)) * termsign
        termsign *= -1
        power += 2
    return result

def my_tan(theta):
    return my_sin(theta) / my_cos(theta)

def my_sec(theta):
    return  1 / my_cos(theta)

def my_cosec(theta):
    return  1 / my_sin(theta)

def my_cot(theta):
    return  1 / my_tan(theta)

def nLog(x) :
    n = 99999999
    return n * ((x ** (1 / n)) - 1)


def log(x, base) :
    try:
        result = nLog(x) / nLog(base)
    except:
        result = 'Infinity'
    return result


def antiLog(a, b) :

    c = 1
    for i in range(1,b+1):
        c = c * a
    return c