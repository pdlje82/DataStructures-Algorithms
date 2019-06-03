import sys
from collections import Counter
from heapq import heappop, heappush
from time import sleep


def huffman_encoding(data):
    if len(data) is 0:
        return None, None
    # create dict with frequencies for each character
    character_freqs = Counter(data)
    if len(character_freqs) < 2:
        return None, None

    # create and fill priority queue
    h = []  # create heap (priority queue)
    encode_dict = {}  # dict to store codes for each character
    decode_dict = {}  # dict to decode (reverse mapping from encode dict)

    # create node for each character and push to heap
    for key in character_freqs:
        node = Node(char=key, freq=character_freqs[key])
        heappush(h, node)

    # build tree
    while len(h) > 1:
        l_node = heappop(h)
        # print('left node :', l_node.char, l_node.freq)
        r_node = heappop(h)
        # print('right node: ', r_node.char, r_node.freq)
        merged = Node(None, l_node.freq + r_node.freq)
        # print('merged node: ', merged.char, merged.freq)
        merged.left = l_node
        merged.right = r_node
        heappush(h, merged)

    root = heappop(h)
    # print('root note left char.: {} - freq.: {}; '
    #      'right char.: {} - freq.: {}'.format(root.left.char, root.left.freq,
    #                                           root.right.char, root.right.freq))
    current_code = ""

    # traverse tree recursively, building the codes
    def traverse(curr_node, curr_code):
        if curr_node:
            # visit
            if curr_node.char is not None:
                encode_dict[curr_node.char] = curr_code
                decode_dict[curr_code] = curr_node.char
                return
            # traverse left
            traverse(curr_node.left, curr_code + '0')
            # traverse right
            traverse(curr_node.right, curr_code + '1')

    traverse(root, current_code)

    # create encoded text
    encoded_text = ''
    for char in data:
        encoded_text += encode_dict[char]

    sleep(0.5)
    return encoded_text, decode_dict


def huffman_decoding(data, decode_dict):
    code = ''
    char_string = ''
    for bit in data:
        code += bit
        if code in decode_dict:
            char = decode_dict[code]
            char_string += char
            code = ''
    return char_string


class Node(object):
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __gt__(self, other):
        return self.freq > other.freq


if __name__ == "__main__":
    codes = {}

# Test Case 1
    print('Test Case1______________________________________________________________________________')
    # a_great_sentence = "abccddd"
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, decode_dict = huffman_encoding(a_great_sentence)
    if (encoded_data and decode_dict) is not None:
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, decode_dict)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))
    else:
        print('No data available')

    # Test Case 2
    print('Test Case2______________________________________________________________________________')
    a_great_sentence = "AAAAAAAAAAAAAAA"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, decode_dict = huffman_encoding(a_great_sentence)
    if (encoded_data and decode_dict) is not None:
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, decode_dict)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))
    else:
        print('No data available')

    # Test Case 3
    print('Test Case3______________________________________________________________________________')
    a_great_sentence = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, decode_dict = huffman_encoding(a_great_sentence)
    if (encoded_data and decode_dict) is not None:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, decode_dict)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
    else:
        print('No data available')

