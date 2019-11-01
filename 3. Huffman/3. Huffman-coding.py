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
        # return '\n'.join(self.traverse_dfs())
        return str(self.root.left) + ' - \'' + str(self.root.value) + '\' - ' + str(self.root.right)


def lowest_frequencies(frequencies):
    """
    1. O(n)
    frequencies: Named tuple 'Pair' built based on repetition of each character in data

    we are getting the lowest frequency in a letter in a string and getting all the letters with the
    same frequency, then deleting those for the original frequencies array
    """
    lowest_freq = min(frequencies, key=lambda x: x.frequency).frequency
    lowest_freq_pairs = [pair for pair in frequencies if pair.frequency == lowest_freq]
    new_frequencies = [pair for pair in frequencies if pair.frequency != lowest_freq]
    return lowest_freq_pairs, new_frequencies


def create_subtrees_in_pairs(trees, lowest_freq_pairs):
    """
    2. O(n)
    iterating over lowest_freq_pairs each 2 -> getting i and i - 1
    using those to build an independent tree and add it to our original list of trees.

    if the len of lowest_freq_pairs is an odd number --> append last frequency Pair and append it to trees[0]
    """
    if len(lowest_freq_pairs) == 1 and len(trees) == 0:
        sub_tree = HuffmanTree(lowest_freq_pairs[0])
        trees.append(sub_tree)
        return

    for i in range(1, len(lowest_freq_pairs), 2):
        sub_tree = HuffmanTree(lowest_freq_pairs[i - 1])
        sub_tree.append(lowest_freq_pairs[i])
        trees.append(sub_tree)

    if len(lowest_freq_pairs) % 2 == 1:
        trees[0].append(lowest_freq_pairs[-1])


def add_one_freq_to_each_tree(trees, lowest_freq_pairs):
    """
    if trees is not empty we cannot create a bunch of leaf nodes all in the same level, instead we need to
    append to each tree in trees a new lowest_frequency --> meaning appending to a full binary tree a new node

    --> how to address that? -> the current_tree.root becomes a new_tree.left and new_tree.right is the new node

    Finally if the len of lowest_freq_pairs is greater than the number of trees -> we create_subtrees_in_pairs with the
    residual ones
    """
    for i, tree in enumerate(trees):
        if i + 1 <= len(lowest_freq_pairs):
            tree.append(lowest_freq_pairs[i])

    # if trees added just 3 and there are 5 letters in this frequency -> 2 letters not added
    # so need to be added as new trees created in pairs
    if len(lowest_freq_pairs) > len(trees):
        lowest_freq_pairs = lowest_freq_pairs[len(trees):]
        create_subtrees_in_pairs(trees, lowest_freq_pairs)


def build_final_tree_from_trees(trees):
    """ O(nlogn)
    with a sorted array of different trees, add to trees[0]  trees[1] .. trees[n] one by one
    """
    trees = sorted(trees, key=lambda x: x.root.value)
    while len(trees) > 1:
        trees[0].mix_with_tree(trees[1])
        del trees[1]

    return trees[0]


def find_path_to_char(char, node, previous_path_found=""):
    if node:
        if node.get_pair().char == char:
            return previous_path_found

        found_left = find_path_to_char(char, node.left, previous_path_found + "0")
        if found_left:
            return found_left

        found_right = find_path_to_char(char, node.right, previous_path_found + "1")
        if found_right:
            return found_right


def get_encoded_data(root_node, data):
    return ' '.join([find_path_to_char(c, root_node) for c in data])


def huffman_encoding(data):
    trees = []

    # sort -> logn -> Counter ( Space O(n), Time O(n)) ---> build frequencies arr costs O(nlogn)
    frequencies = [Pair(freq, char) for char, freq in Counter(sorted(data)).items()]

    # O(f) -> f set of different amounts of frequencies
    # Worst case all different so forget O(f) exists ---> Just O(n)
    while len(frequencies) > 0:

        # O(2n) -> O(n) n = chars in data
        lowest_freq_pairs, frequencies = lowest_frequencies(frequencies)

        if len(trees) == 0:
            # All different frequencies, so here there is only 1 frequency O(1)
            create_subtrees_in_pairs(trees, lowest_freq_pairs)
        else:
            # only 1 frequency  in lowest_freq_pairs, and trees always len 1 --> O(1)
            add_one_freq_to_each_tree(trees, lowest_freq_pairs)

    # trees here len = 1 so cost is O(1)
    final_tree = build_final_tree_from_trees(trees)
    # O(n) iterate over each char -> and get char encoded recursively takes O(n) --> O(n^2)
    data_encoded = get_encoded_data(final_tree.root, data)

    return data_encoded, final_tree


def find_char_from_path(path, node):
    # This recursive function also takes O(n)
    if node:
        if node.get_pair().char is not None:
            return node.get_pair().char

        if len(path) > 0:
            direction = path[0]
            char = None
            if direction == "0":
                char = find_char_from_path(path[1:], node.left)
            elif direction == "1":
                char = find_char_from_path(path[1:], node.right)

            return char


def huffman_decoding(data, codified_tree):
    # Iterate over each "char" in data O(n)
    return ''.join([find_char_from_path(path, codified_tree.root) for path in data.split()])


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, t = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data.replace(' ', ''), base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, t)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
