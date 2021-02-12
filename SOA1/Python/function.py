import time
import struct

def main_function():
    number = ["0", "1", "b", "p", "4", "s", "6", "v", "8", "x", "a", "2", "c", "d", "y", "f", "g", "h", "i", "j", "k", "l"
              "m", "n", "o", "3", "q", "5", "t", "u", "7", "w", "9", "e", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I"
              "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "J", "K", "L", "M", "N",
              "O", "0", "1", "b", "p", "4", "s", "6", "v", "8", "x", "a", "q", "5", "t", "u", "7", "w", "9", "e", "z", "A",
              "B", "C", "D", "Q", "R", "S", "T", "U", "V", "W"]

    def rand_val(x,y):
        sub=y-x
        random=int(time.time()*1000)
        random %=sub
        random+=x
        return random

    x = int(3)
    y = int(10)
    res = rand_val(x,y)
    num = ""

    while res > 0:
        # print (res)
        a = res * 2
        b = a + 5
        val = rand_val(a,b)
        subval = res * val
        getval = rand_val(res,subval)
        num += number[getval]
        res = res - 1
    return(num)

def figure_to_word(main, sub) :
    # Program to input a number upto 5 digits and print it in words
    number = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    nty = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]
    tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
            "Nineteen"]

    p = sub
    p = int(p * 100)
    n = int(main)

    if p > 99:
        print("Cant solve for more than 2 digits")
    else:
        f = [0, 0]
        j = 0
        while p > 0:
            f[j] = p % 10
            j += 1
            p = p // 10
        paisa = ""

        if f[1] != 0:
            if (f[1] == 1):
                paisa += tens[f[0]]
            else:
                paisa += nty[f[1]] + " " + number[f[0]]
        else:
            if f[0] != 0:
                paisa += number[f[0]]

    if n > 999999999:
        return ("Cant solve for more than 8 digits")
    else:
        d = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        i = 0
        while n > 0:
            d[i] = n % 10
            i += 1
            n = n // 10
        num = ""
        if d[8] != 0:
            if (d[8] == 1):
                num += tens[d[7]] + " Crore "
            else:
                num += nty[d[8]] + " " + number[d[7]] + " Crore "
        else:
            if d[7] != 0:
                num += number[d[7]] + " Crore "
        if d[6] != 0:
            if (d[6] == 1):
                num += tens[d[5]] + " Lakhs "
            else:
                num += nty[d[6]] + " " + number[d[5]] + " Lakhs "
        else:
            if d[5] != 0:
                num += number[d[5]] + " Lakhs "
        if d[4] != 0:
            if (d[4] == 1):
                num += tens[d[3]] + " Thousand "
            else:
                num += nty[d[4]] + " " + number[d[3]] + " Thousand "
        else:
            if d[3] != 0:
                num += number[d[3]] + " Thousand "
        if d[2] != 0:
            num += number[d[2]] + " Hundred "
        if d[1] != 0:
            if (d[1] == 1):
                num += tens[d[0]]
            else:
                num += nty[d[1]] + " " + number[d[0]]
        else:
            if d[0] != 0:
                num += number[d[0]]
    resp = num
    res = paisa * 0

    result = " " + resp +" "+ res + "INR only"
    return (result)

def diff_date(d1, d2, m1, m2, y1, y2, s1, s2):
    year1 = y1
    year2 = y2
    day1 = d1
    day2 = d2
    mon1 = m1
    mon2 = m2
    time1 = list(s1.split(":"))
    time2 = list(s2.split(":"))
    # time calculation
    r = ['0', '0', '0']

    for i in range(0, len(time1)):
        time1[i] = int(time1[i])
        # print (time1[i]);

    for i in range(0, len(time2)):
        time2[i] = int(time2[i])

    if (time2[2] >= time1[2]):
        r[2] = time2[2] - time1[2]
    else:
        r[2] = (time2[2] + 60) - time1[2]
        time2[1] -= 1

    if (time2[1] >= time1[1]):
        r[1] = time2[1] - time1[1]
    else:
        r[1] = (time2[1] + 60) - time1[1]
        time2[0] -= 1

    if (time2[0] >= time1[0]):
        r[0] = time2[0] - time1[0]
    else:
        r[0] = (time2[0] + 24) - time1[0]
        day2 -= 1

    # dayscalculartion

    if day2 < day1:
        if mon2 == 3:
            if ((year2 % 4 == 0 and year2 % 100 != 0) or (year2 % 400 == 0)):
                day2 += 29
            else:
                day2 += 28
        else:
            if (mon2 == 5 or mon2 == 7 or mon2 == 10 or mon2 == 12):
                day2 += 30
            else:
                day2 += 31
                mon2 = mon2 - 1

    if mon2 < mon1:
        mon2+= 12
        year2-= 1

    day_diff = day2 - day1
    mon_diff = mon2 - mon1
    year_diff = year2 - year1

    if year_diff < 0:
        year_diff = year_diff * -1

    res = (" Years : " + str(year_diff) + "  Months : " + str(mon_diff) + " Days : " + str(day_diff) + " Hours : "+ str(r[0]) + " Minutes : " + str(r[1]) + " Seconds : " + str(r[2]))
    return(res)

def union_op(a, b):
    for i in b:
        if i in a:
            continue
        else:
            a.append(i)
    return a


def diff_op(a, b):
    c = a[:]
    for i in c:
        print(i)
        if i in b:
            print(str(i) + " is in b")
            a.remove(i)
    print(a)
    return a


def intersect_op(a, b):
    c = []
    for i in a:
        if i in b:
            c.append(i)

    return c

def lowerDiagonal(matrixA, row, col):
    RMT = []
    LMT = []
    LM = []
    RM = []

    for i in range(0, row):
        for j in range(0, col):
            if (j < i):
                LMT.append(matrixA[i][j])
            else:
                LMT.append(" ")

            if (j >= 1) and (i + j > col - 1):
                RMT.append(matrixA[i][j])
            else:
                RMT.append(" ")
        RM.append(RMT)
        LM.append(LMT)
        RMT = []
        LMT = []

    print(LM)
    print(RM)

    return {'Lower Right': RM, 'Lower Left': LM}


def upperDiagonal(matrixA, row, col):
    RMT = []
    LMT = []
    LM = []
    RM = []
    if row == col:
        for i in range(0, row):
            for j in range(0, col):
                if (j > i):
                    RMT.append(matrixA[i][j])
                else:
                    RMT.append(" ")
                if (j <= 1) and (i + j < col - 1):
                    LMT.append(matrixA[i][j])
                else:
                    LMT.append(" ")
            RM.append(RMT)
            LM.append(LMT)
            RMT = []
            LMT = []

    return { 'Upper Right': RM, 'Upper Left': LM}


def transpose(matrixA, row, col):
    RM = [[matrixA[j][i] for j in range(len(matrixA))] for i in range(len(matrixA[0]))]

    return RM

import random
import math
from random import randrange

def rabinMiller(n, k=10):
    if n == 2:
            return True
    if not n & 1:
            return False

    def check(a, s, d, n):
            x = pow(a, d, n)
            if x == 1:
                    return True
            for i in range(1, s - 1):
                    if x == n - 1:
                            return True
                    x = pow(x, 2, n)
            return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
            d >>= 1
            s += 1

    for i in range(1, k):
            a = randrange(2, n - 1)
            if not check(a, s, d, n):
                    return False
    return True

def isPrime(n):
     #lowPrimes is all primes (sans 2, which is covered by the bitwise and operator)
     #under 1000. taking n modulo each lowPrime allows us to remove a huge chunk
     #of composite numbers from our potential pool without resorting to Rabin-Miller
     lowPrimes =   [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                   ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
     if (n >= 3):
         if (n&1 != 0):
             for p in lowPrimes:
                 if (n == p):
                    return True
                 if (n % p == 0):
                     return False
             return rabinMiller(n)
     return False

def generateLargePrime(k):
     #k is the desired bit length
     r = 100*(math.log(k,2)+1) #number of attempts max
     r_ = r
     while r>0:
        #randrange is mersenne twister and is completely deterministic
        #unusable for serious crypto purposes
         n = random.randrange(2**(k-1),2**(k))
         r -= 1
         if isPrime(n) == True:
             return n

     str_failure = "Failure after" + str(r_) + "tries."
     return str_failure


def gcd(a, b):
    '''
    Euclid's algorithm for determining the greatest common divisor
    Use iteration to make it faster for larger integers
    '''
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(a, b):
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oa  # If neg wrap modulo orignal a
    # return a , lx, ly  # Return only positive values
    return lx

def rwh_primes2(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in range(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n/3-correction) if sieve[i]]

def multiply(x, y):
    _CUTOFF = 1536
    if x.bit_length() <= _CUTOFF or y.bit_length() <= _CUTOFF:  # Base case
        return x * y
    else:
        n = max(x.bit_length(), y.bit_length())
        half = (n + 32) // 64 * 32
        mask = (1 << half) - 1
        xlow = x & mask
        ylow = y & mask
        xhigh = x >> half
        yhigh = y >> half

        a = multiply(xhigh, yhigh)
        b = multiply(xlow + xhigh, ylow + yhigh)
        c = multiply(xlow, ylow)
        d = b - a - c
        return (((a << half) + d) << half) + c


def generate_keypair(keySize=10):
    p = generateLargePrime(keySize)
    # print(p)
    q = generateLargePrime(keySize)
    # print(q)

    if p == q:
        raise ValueError('p and q cannot be equal')

    #n = pq
    n = multiply(p, q)

    #Phi is the totient of n
    phi = multiply((p-1),(q-1))

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    #return ''.join(plain)
    return plain

def edfuncntion(mes):
    '''
    Detect if the script is being run directly by the user
    '''
    #print("RSA Encrypter/ Decrypter")

    #print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair()
    #print("Your public key is ", public ," and your private key is ", private)

    message = mes

    encrypted_msg = encrypt(private, message)

    #print("Your encrypted message is: ")
    # print(''.join(map(lambda x: str(x), encrypted_msg)))
    # print("Decrypting message with public key ", public ,"...")
    # print("Your message is:")
    # print(decrypt(public, encrypted_msg))
    enc = (''.join(map(lambda x: str(x), encrypted_msg)))
    dec = (''.join(decrypt(public, encrypted_msg)))
    return (enc,dec)


def generate(message):
    paddingSize = (64 - 1 - 8 - len(message) % 64) % 64
    lengthInBits = (len(message) * 8) % 2 ** 64
    return message + b"\x80" + paddingSize * b"\x00" + struct.pack("<Q", lengthInBits)


def rotate_left(n, amount):
    return ((n << amount) & 0xffff_ffff) | (n >> (32 - amount))


def hash_chunk(state, chunk):
    (a, b, c, d) = state

    for i in range(64):
        if i < 16:
            bits = (b & c) | (~b & d)
            index = i
            shift = (7, 12, 17, 22)[i % 4]
        elif i < 32:
            bits = (d & b) | (c & ~d)
            index = (5 * i + 1) % 16
            shift = (5, 9, 14, 20)[i % 4]
        elif i < 48:
            bits = b ^ c ^ d
            index = (3 * i + 5) % 16
            shift = (4, 11, 16, 23)[i % 4]
        else:
            bits = c ^ (b | ~d)
            index = 7 * i % 16
            shift = (6, 10, 15, 21)[i % 4]

        const = math.floor(abs(math.sin(i + 1)) * 2 ** 32)
        bAdd = (const + a + bits + chunk[index]) & 0xffff_ffff
        bAdd = rotate_left(bAdd, shift)

        (a, b, c, d) = (d, (b + bAdd) & 0xffff_ffff, b, c)

    return (a, b, c, d)


def md5(message):
    state = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

    ctr = 0
    for chunk in struct.iter_unpack("<16I", generate(message)):
        print('chunk  ', chunk, 'ctr', ctr)
        ctr += 1
        print('prep-msg  ', generate(message))
        print('iter-unpack  ', struct.iter_unpack("<16I", generate(message)))

        hash_ = hash_chunk(state, chunk)
        state = [(s + h) & 0xffff_ffff for (s, h) in zip(state, hash_)]

    return b"".join(struct.pack("<I", number) for number in state)
