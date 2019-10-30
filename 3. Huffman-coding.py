import sys
from collections import Counter, namedtuple

Pair = namedtuple('Pair', 'frequency char')


class Node:
    def __init__(self, value, char=None):
        self.value = value
        self.char = char
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


class HuffmanTree:
    def __init__(self, pair=None, node=None):
        self.root = Node(None)
        self.root.left = node if node else Node(pair.frequency, pair.char)

    def append(self, pair):
        if self.root.left and self.root.right:
            new_tree = HuffmanTree(node=self.root)
            new_tree.append(pair)
            self.re_assign_root(new_tree)
        else:
            self.root.right = Node(pair.frequency, pair.char)
            self.root.value = self.root.left.value + self.root.right.value

    def re_assign_root(self, sub_tree):
        self.root = sub_tree.root

    def __repr__(self):
        return str(self.root.left) + ' - \'' + str(self.root.value) + '\' - ' + str(self.root.right)


def huffman_encoding(data):
    frequencies = [Pair(freq, char) for char, freq in Counter(sorted(data)).items()]
    trees = []
    while len(frequencies) > 0:
        lower_freq = min(frequencies, key=lambda x: x.frequency).frequency

        lower_freq_pairs = [pair for pair in frequencies if pair.frequency == lower_freq]
        frequencies = [pair for pair in frequencies if pair.frequency != lower_freq]
        if len(trees) == 0:
            for i in range(1, len(lower_freq_pairs), 2):
                sub_tree = HuffmanTree(lower_freq_pairs[i - 1])
                sub_tree.append(lower_freq_pairs[i])
                trees.append(sub_tree)

            if len(lower_freq_pairs) % 2 == 1:
                trees[0].append(lower_freq_pairs[-1])
        else:
            for i, tree in enumerate(trees):
                if i + 1 <= len(lower_freq_pairs):
                    tree.append(lower_freq_pairs[i])
                else:
                    break

            if len(lower_freq_pairs) > len(trees):
                lower_freq_pairs = lower_freq_pairs[len(trees):]
                for i in range(1, len(lower_freq_pairs), 2):
                    sub_tree = HuffmanTree(lower_freq_pairs[i - 1])
                    sub_tree.append(lower_freq_pairs[i])
                    trees.append(sub_tree)

                if len(lower_freq_pairs) % 2 == 1:
                    trees[0].append(lower_freq_pairs[-1])

    print(trees)
    trees = sorted(trees, key=lambda x: x.root.value)
    print(trees)
    while len(trees) > 1:
        trees[0].append(Pair(frequency=trees[1].root.value, char=trees[1].root.char))
        del trees[1]

    print(trees)

    return None, None


def huffman_decoding(data, t):
    return None, None


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, t = huffman_encoding(a_great_sentence)
    #
    # print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print("The content of the encoded data is: {}\n".format(encoded_data))
    #
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print("The content of the encoded data is: {}\n".format(decoded_data))
