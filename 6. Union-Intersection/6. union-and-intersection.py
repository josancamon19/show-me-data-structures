class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        if cur_head is None:
            return "-- Empty --"
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(list1, list2):
    # Your Solution Here

    if list1 is None or type(list1) is not LinkedList or list2 is None or type(list2) is not LinkedList:
        print("Invalid Arguments, lists cannot be None")
        return LinkedList()

    if list1.head is None:
        return list2

    new_linked_list = LinkedList()

    current_l1 = list1.head
    while current_l1:
        new_linked_list.append(current_l1.value)
        current_l1 = current_l1.next

    current_l2 = list2.head
    while current_l2:
        new_linked_list.append(current_l2.value)
        current_l2 = current_l2.next

    return new_linked_list


def intersection(list1, list2):
    # Your Solution Here

    if list1 is None or type(list1) is not LinkedList or list2 is None or type(list2) is not LinkedList:
        print("Invalid Arguments, lists cannot be None")
        return LinkedList()

    intersected_linked_list = LinkedList()
    s = set()

    current_l1 = list1.head
    while current_l1:
        s.add(current_l1.value)
        current_l1 = current_l1.next

    current_l2 = list2.head
    while current_l2:
        if current_l2.value in s:
            intersected_linked_list.append(current_l2.value)
            s.remove(current_l2.value)

        current_l2 = current_l2.next

    return intersected_linked_list


# def intersection2(list1, list2):
#     # Your Solution Here
#
#     if list1 is None or type(list1) is not LinkedList or list2 is None or type(list2) is not LinkedList:
#         print("Invalid Arguments, lists cannot be None")
#         return LinkedList()
#
#     intersected_linked_list = LinkedList()
#     s = set()
#
#     current_l1 = list1.head
#     while current_l1:
#
#         current_l2 = list2.head
#         while current_l2:
#
#             if current_l2.value == current_l1.value:
#                 # print(current_l1, current_l2)
#
#                 already_intersected = False
#                 current_intersected = intersected_linked_list.head
#
#                 while current_intersected:
#                     if current_intersected.value == current_l1.value:
#                         already_intersected = True
#                         break
#                     current_intersected = current_intersected.next
#
#                 if not already_intersected:
#                     intersected_linked_list.append(current_l1.value)
#
#             current_l2 = current_l2.next
#
#         current_l1 = current_l1.next
#
#     return intersected_linked_list

if __name__ == '__main__':
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    # Union operation returns element_1 + element_2
    print('\nUnion operation: ', union(linked_list_1, linked_list_2))
    # Intersection operation returns set(element_1).intersection(set(element_2))
    print('Intersection operation: ', intersection(linked_list_1, linked_list_2))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    # Union operation returns element_1 + element_2
    print('\nUnion operation: ', union(linked_list_3, linked_list_4))
    # element_1 and element_2 are all different  --> 0 intersections
    print('Intersection operation: ', intersection(linked_list_3, linked_list_4))

    # Test case 3

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = []
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    # Union operation element_1 is empty so return element_2 [1, 7, 8, 9, 11, 21, 1]
    print('\nUnion operation: ', union(linked_list_5, linked_list_6))
    # Intersection operation element_1 is empty so 0 intersections
    print('Intersection operation: ', intersection(linked_list_5, linked_list_6))

    print('\n\n--- Invalid Operations ---')

    # all will return empty LinkedList() and print a message Invalid Arguments, lists cannot be None
    print('\nUnion operation: ', union(linked_list_5, None))
    print('Intersection operation: ', intersection(linked_list_5, None))

    print('\nUnion operation: ', union(None, linked_list_6))
    print('Intersection operation: ', intersection(None, linked_list_6))

    print('\nUnion operation: ', union(None, None))
    print('Intersection operation: ', intersection(None, None))
