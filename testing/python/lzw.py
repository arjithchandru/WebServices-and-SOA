def lzw(input_str):
    keys_dict = {}

    ind = 0
    inc = 1
    while True:
        if not (len(input_str) >= ind + inc):
            break
        sub_str = input_str[ind:ind + inc]
        print (sub_str, ind, inc)
        if sub_str in keys_dict:
            inc += 1
        else:
            keys_dict[sub_str] = 0
            ind += inc
            inc = 1
            # print 'Adding %s' %sub_str

    return list(keys_dict)

# second test

def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    # in Python 3: dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
            # print(w)
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            # print (w)
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO

    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    # in Python 3: dictionary = {i: chr(i) for i in range(dict_size)}

    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
            # print(entry)
        elif k == dict_size:
            entry = w + w[0]
            # print(entry)
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()


# How to use:


# Driver code
if __name__ == "__main__":
    st = "AAAABBCDEABCDABCAAABCDEEEEEECBBBBBBDDAAE"
    word = lzw(st)
    compressed = compress(st)
    print(compressed)
    # decompressed = decompress(compressed)
    # print(decompressed)
    print(word)