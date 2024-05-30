import heapq

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node (char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        node = Node(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, node)
    return heap[0]

def generate_huffman_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node.char is not None:
        codebook[node.char] = prefix
    if node.left is not None:
        generate_huffman_codes(node.left, prefix + "0", codebook)
    if node.right is not None:
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encoding(frequencies):
    root = build_huffman_tree(frequencies)
    codebook = generate_huffman_codes(root)
    return codebook

frequencies = {'a': 5, 'c': 1, 't': 2, 's': 1}
huffman_codes = huffman_encoding(frequencies)

print(huffman_codes)

def encode_string(s, huffman_codes):
    return ''.join(huffman_codes[char] for char in s)

encoded_string = encode_string("cats", huffman_codes)
print(encoded_string)