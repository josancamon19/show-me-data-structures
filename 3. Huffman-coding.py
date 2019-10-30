import sys
from collections import Counter, namedtuple

Pair = namedtuple('Pair', 'frequency char')


class Node:
    def __init__(self, value, char=None):
        self.value = value
        self.char = char
        self.left = None
        self.right = None

    def get_pair(self):
        return Pair(frequency=self.value, char=self.char)

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

    def mix_with_tree(self, tree):
        mixed_tree = HuffmanTree(node=self.root)
        mixed_tree.root.right = tree.root
        mixed_tree.root.value = mixed_tree.root.left.value + mixed_tree.root.right.value
        self.re_assign_root(mixed_tree)

    def re_assign_root(self, sub_tree):
        self.root = sub_tree.root

    def traverse_dfs(self):
        visit_order = list()
        root = self.root

        def traverse(node):
            if node:
                if node.get_pair().char is not None:
                    visit_order.append(node.get_pair())

                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return visit_order

    def __repr__(self):
        return str(self.root.left) + ' - \'' + str(self.root.value) + '\' - ' + str(self.root.right)


def create_subtrees_in_pairs(trees, lower_freq_pairs):
    for i in range(1, len(lower_freq_pairs), 2):
        sub_tree = HuffmanTree(lower_freq_pairs[i - 1])
        sub_tree.append(lower_freq_pairs[i])
        trees.append(sub_tree)

    if len(lower_freq_pairs) % 2 == 1:
        trees[0].append(lower_freq_pairs[-1])

    return trees


def lowest_frequencies(frequencies):
    lower_freq = min(frequencies, key=lambda x: x.frequency).frequency
    lower_freq_pairs = [pair for pair in frequencies if pair.frequency == lower_freq]
    new_frequencies = [pair for pair in frequencies if pair.frequency != lower_freq]
    return lower_freq_pairs, new_frequencies


def add_one_freq_to_each_tree(trees, lower_freq_pairs):
    for i, tree in enumerate(trees):
        if i + 1 <= len(lower_freq_pairs):
            tree.append(lower_freq_pairs[i])

    # if trees added just 3 and there are 5 letters in this frequency -> 2 letters not added
    # so need to be added as new trees created in pairs
    if len(lower_freq_pairs) > len(trees):
        lower_freq_pairs = lower_freq_pairs[len(trees):]
        trees = create_subtrees_in_pairs(trees, lower_freq_pairs)
    return trees, lower_freq_pairs


def build_final_tree_from_trees(trees):
    trees = sorted(trees, key=lambda x: x.root.value)
    while len(trees) > 1:
        trees[0].mix_with_tree(trees[1])
        del trees[1]

    return trees[0]


def huffman_encoding(data):
    trees = []
    frequencies = [Pair(freq, char) for char, freq in Counter(sorted(data)).items()]

    while len(frequencies) > 0:
        lower_freq_pairs, frequencies = lowest_frequencies(frequencies)

        if len(trees) == 0:
            trees = create_subtrees_in_pairs(trees, lower_freq_pairs)
        else:
            trees, lower_freq_pairs = add_one_freq_to_each_tree(trees, lower_freq_pairs)

    final_tree = build_final_tree_from_trees(trees)

    print(sorted(final_tree.traverse_dfs(), key=lambda x: x.frequency, reverse=True))

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
