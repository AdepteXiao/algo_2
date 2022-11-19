from typing import Union

from back.linked_list import LinkedListItem, LinkedList
from back.composition import Composition
from back.utils import duration_from_seconds

import os

path = "C:\\Education\\algo2\\tracks\\songs"
list_of_all = [f"{path}\\{track}" for track in os.listdir(path)]


class PlaylistItem(LinkedListItem):
    def __init__(self, composition: Composition):
        super().__init__(composition)


class Playlist(LinkedList):
    def __init__(self, head: Union[PlaylistItem, None], name: Union[str, None]):
        super().__init__(head)
        if name is None:
            self.name = 'Неизвестный'
        else:
            self.name = name

        if head is None:
            self.duration = '0:0'
        else:
            self.duration = duration_from_seconds(sum(map(lambda x: x.data.duration, self)))

        self.__current_track = head


def create_node_sequence(data):

    if not data:
        return None
    head = LinkedListItem(data[0])
    ptr = head
    for val in data[1:]:
        new_node = LinkedListItem(val)
        ptr.next_item = new_node
        new_node.previous_item = ptr
        ptr = ptr.next_item

    head.previous_item = ptr
    ptr.next_item = head

    return head


def make_list_of_all():
    return Playlist(create_node_sequence([Composition(paths) for paths in list_of_all]), "Все треки")


if __name__ == '__main__':
    print(make_list_of_all())


