import math


class ListNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def remove_by_id(self, item_id):
        current_id = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next

            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1

    def search(self, x, y):
        current_node = self.head
        node_id = 1

        while current_node is not None:
            if current_node.x == x and current_node.y == y:
                print(f"({current_node.x},{current_node.y}) - id of element = {node_id}")
            current_node = current_node.next
            node_id = node_id + 1

    def distance_between_first_and_last(self):
            a = (self.head.x - self.tail.x) ** 2
            b = (self.head.y - self.tail.y) ** 2
            return math.sqrt(a + b)

    def get_all(self):
        current_node = self.head

        while current_node is not None:
            print(f"({current_node.x},{current_node.y})")

            current_node = current_node.next

    def length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count = count + 1
            current_node = current_node.next

        return count
