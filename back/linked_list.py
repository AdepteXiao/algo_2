class LinkedListItem:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append_to_emptylist(self, item):
        new_node = LinkedListItem(item)
        self.head = new_node
        self.tail = new_node
        new_node.prev = self.head
        new_node.next = self.tail
        self.size += 1

    def append_left(self, item):
        if self.head is None:
            self.append_to_emptylist(item)
            return
        new_node = LinkedListItem(item)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def append_right(self, item):
        self.append(item)

    def append(self, item):
        if self.head is None:
            self.append_to_emptylist(item)
            return
        node = self.tail
        new_node = LinkedListItem(item)
        node.next = new_node
        new_node.prev = node
        self.tail = new_node
        self.size += 1

    def insert_after_item(self, previous, item):
        if self.head is None:
            print("List is empty")
            return
        else:
            node = self.head
            while node is not self.tail:
                if node.item == previous:
                    break
                node = node.next
            if node is self.tail:
                print("item not in the list")
            else:
                new_node = LinkedListItem(item)
                node.next.prev = new_node
                new_node.prev = node
                new_node.next = node.next
                node.next = new_node
                self.size += 1

    def remove(self, item):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head is self.tail:
            if self.head.item == item:
                self.head = None
            else:
                print("Item not found")
            return

        if self.tail.item == item:
            self.tail = self.tail.prev
            return

        if self.head.item == item:
            self.head = self.head.next
            return

        node = self.head
        while node.next is not self.tail:
            if node.item == item:
                break
            node = node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def swap(self, item1, item2):
        if item1 == self.head:
            self.head = item2
        elif item2 == self.head:
            self.head = item1
        if item1 == self.tail:
            self.tail = item2
        elif item2 == self.tail:
            self.tail = item1

        item2.prev = item1.prev
        item1.next = item2.next
        item2.next = item1
        item1.prev = item2
        item1.next.prev = item1
        item2.prev.next = item2

    def __len__(self) -> int:
        return self.size

    def __contains__(self, item: object) -> bool:
        node = self.head
        while node is not self.tail:
            if node.item == item:
                return True
        if self.tail.item == item:
            return True
        return False


