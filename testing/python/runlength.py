def printRLE(st):
    n = len(st)
    i = 0
    tx = ''

    while i < n - 1:

        # Count occurrences of
        # current character
        count = 1

        while (i < n - 1 and
               st[i] == st[i + 1]):

            count += 1
            i += 1
        i += 1

        # Print character and its count
        print(st[i - 1] +
              str(count),end="")
        wd =(st[i - 1] + str(count))
        tx = tx + wd

    return tx


# Driver code
if __name__ == "__main__":
    st = "helloworldaaa"
    word = printRLE(st)
    print(word)