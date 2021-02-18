import heapq
from heapq import heappop, heappush


def isLeaf(root):
	return root.left is None and root.right is None


# A Tree node
class Node:
	def __init__(self, ch, freq, left=None, right=None):
		self.ch = ch
		self.freq = freq
		self.left = left
		self.right = right


	def __lt__(self, other):
		return self.freq < other.freq


def encode(root, str, huffman_code):

	if root is None:
		return

	# found a leaf node
	if isLeaf(root):
		huffman_code[root.ch] = str if len(str) > 0 else '1'

	encode(root.left, str + '0', huffman_code)
	encode(root.right, str + '1', huffman_code)



def decode(root, index, str):

	if root is None:
		return index

	# found a leaf node
	if isLeaf(root):
		print(root.ch, end='')
		word = root.ch
		return index,word

	index = index + 1
	root = root.left if str[index] == '0' else root.right
	return decode(root, index, str)


def buildHuffmanTree(text):

	if len(text) == 0:
		return


	freq = {i: text.count(i) for i in set(text)}


	pq = [Node(k, v) for k, v in freq.items()]
	heapq.heapify(pq)

	# do till there is more than one node in the queue
	while len(pq) != 1:


		left = heappop(pq)
		right = heappop(pq)


		total = left.freq + right.freq
		heappush(pq, Node(None, total, left, right))

	root = pq[0]


	huffmanCode = {}
	encode(root, "", huffmanCode)



	str = ""
	for c in text:
		str += huffmanCode.get(c)


	encd = str
	decd=""

	if isLeaf(root):
		while root.freq > 0:
			word = root.ch
			decd = word
			root.freq = root.freq - 1
	else:

		index = -1
		while index < len(str) - 1:
			index,word = decode(root, index, str)
			decd = decd + word

	return encd,decd,huffmanCode

# runlengthcode

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

# lwz code

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
            

    return list(keys_dict)

# second test

def compress(uncompressed):

    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))


    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
            # print(w)
        else:
            result.append(dictionary[w])

            dictionary[wc] = dict_size
            dict_size += 1
            # print (w)
            w = c


    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):

    from io import StringIO

    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))

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


        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()
