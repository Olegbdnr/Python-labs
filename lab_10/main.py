from LinkedList import ListNode
from LinkedList import LinkedList


def main():
    node1 = ListNode(4, 2)
    node2 = ListNode(5, 2)
    node3 = ListNode(9, 2)
    node4 = ListNode(8, 2)
    list = LinkedList()
    list.add(node1)
    list.add(node2)
    list.add(node3)
    list.add(node4)
    list.get_all()
    print("Length =", list.length())
    list.search(8, 2)
    list.remove_by_id(1)
    list.get_all()
    print("Distance between first and last =", list.distance_between_first_and_last())


if __name__ == '__main__':
    main()

