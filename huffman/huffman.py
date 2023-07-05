from heapq import heappush, heappop
from collections import defaultdict
import os

class HuffmanCoding:
    class Node:
        def __init__(self, freq, char=None, left=None, right=None): #each node of huffman tree:
            self.freq = freq
            self.char = char
            self.left = left
            self.right = right

        def __lt__(self, other): #overloads '<' operator:
            return self.freq < other.freq

    def __init__(self):
        self.codes = {}
        self.encoded_string = ""
        self.decoded_string = ""

    def build_frequency_table(self, string): #gets frequency of each charachter and makes a dictonary:
        freq_table = defaultdict(int)
        for char in string:
            freq_table[char] += 1
        return freq_table

    def build_huffman_tree(self, freq_table): #builds the huffman tree using a heap. adds characters as instances of node class.
        priority_queue = []
        for char, freq in freq_table.items():
            heappush(priority_queue, self.Node(freq, char))

        while len(priority_queue) > 1:
            node1 = heappop(priority_queue)
            node2 = heappop(priority_queue)
            merged = self.Node(node1.freq + node2.freq, left=node1, right=node2)
            heappush(priority_queue, merged)

        return priority_queue[0]

    def build_codes(self, root, current_code=""): #builds the code for each character from the huffman tree.
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            return

        self.build_codes(root.left, current_code + "0")
        self.build_codes(root.right, current_code + "1")

    def encode(self, string): #encodes the given string
        freq_table = self.build_frequency_table(string)
        huffman_tree = self.build_huffman_tree(freq_table)
        self.build_codes(huffman_tree)

        for char in string:
            self.encoded_string += self.codes[char]

        return self.encoded_string

    def decode(self, encoded_string, root): #decodes the sring based on the huffman tree.
        current_node = root
        for bit in encoded_string:
            if bit == "0":
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.char is not None:
                self.decoded_string += current_node.char
                current_node = root

        return self.decoded_string
    

def read_file(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, file_path)
    with open(full_path, 'r') as file:
        content = file.read()
        return content

def wrtie_file(result, path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, path + '.compressed')
    with open(full_path, 'w') as file:
        file.write(result)


do = HuffmanCoding()

string = read_file("/home/benyamin/codes/algorithems/huffman/test.txt")

wrtie_file (
    do.encode(string)
    ,'result')

print(
'decoded string is: '+
do.decode(do.encoded_string,do.build_huffman_tree(do.build_frequency_table(string)))
)
