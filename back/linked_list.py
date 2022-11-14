from typing import Union, Iterator, Generator


class LinkedListItem:
    def __init__(self, item = None):
        self.__next = None
        self.__prev = None
        self.item = item

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value
        value.__prev = self

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value
        value.__next = self


class LinkedList:
    def __init__(self, head: Union[LinkedListItem, None] = None) -> None:
        self.__head = head

        if head is None:
            self.__tail = None
            self.size = 0
        else:
            self.size = 1
            ptr = head
            while ptr.next_item is not None and ptr.next_item != self.head:
                ptr = ptr.next_item
                self.size += 1
            self.tail = ptr

    @property
    def head(self) -> Union[LinkedListItem, None]:
        return self.__head

    @property
    def tail(self) -> Union[LinkedListItem, None]:
        return self.__tail

    @tail.setter
    def tail(self, value: Union[LinkedListItem, None]) -> None:
        self.__tail = value

    @head.setter
    def head(self, value: Union[LinkedListItem, None]) -> None:
        self.__head = value

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

    def swap(self, first_item: LinkedListItem, second_item: LinkedListItem) -> None:
        """
        Метод обмена двух любых нод списка между собой
        :param first_item: первая нода
        :param second_item: вторая нода
        """

        if first_item == self.head:
            self.head = second_item
        elif second_item == self.head:
            self.head = first_item
        if first_item == self.tail:
            self.tail = second_item
        elif second_item == self.tail:
            self.tail = first_item

        temp = first_item.next
        first_item.next = second_item.next
        second_item.next = temp

        if first_item.next is not None:
            first_item.next.prev = first_item
        if second_item.next is not None:
            second_item.next.prev = second_item

        temp = first_item.prev
        first_item.prev = second_item.prev
        second_item.prev = temp

        if first_item.prev is not None:
            first_item.prev.next = first_item
        if second_item.prev is not None:
            second_item.prev.next = second_item

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator:
        pointer = self.head
        for i in range(self.size):
            yield pointer
            pointer = pointer.next

    def __contains__(self, item: object) -> bool:
        node = self.head
        while node is not self.tail:
            if node.item == item:
                return True
            node = node.next
        if self.tail.item == item:
            return True
        return False

    def __reversed__(self) -> Generator:
        node = self.tail
        for i in range(self.size):
            yield node
            node = node.prev

    def __getitem__(self, index: int) -> object:
        if index >= self.size or abs(index) > self.size:
            raise IndexError("index out of range")
        if index >= 0:
            node = self.head
            for i in range(index):
                node = node.next
        else:
            node = self.tail
            for i in range(-1, index, -1):
                node = node.prev
        return node.item

