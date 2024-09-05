

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def beginning (self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def between (self, prev_node, new_data):
        # if prev_node is None:
        #     print("The given previous node must inLinkedList.")
        #     return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def End(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def delete(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def getList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()
    llist.End(1)
    llist.beginning(2)
    llist.beginning(3)
    llist.End(4)
    llist.between(llist.head.next, 5)


    llist.getList()