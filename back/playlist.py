from typing import Union

from back.linked_list import LinkedListItem, LinkedList
from back.composition import Composition
from back.utils import duration_from_seconds

import os

path = r"C:\Education\algo2\tracks\songs"
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

    @property
    def current_track(self) -> Composition:
        return self.__current_track.data

    @current_track.setter
    def current_track(self, value: Composition) -> None:
        self.__current_track = self.find_node(value)

    def next_track(self) -> None:
        self.__current_track = self.__current_track.next_item

    def previous_track(self):
        self.__current_track = self.__current_track.previous_item

    def __str__(self) -> str:
        return f'{self.name} - {self.size} треков, длительностью {self.duration}'

    def __repr__(self):
        return f'{self.name} - {self.size} треков, длительностью {self.duration}'

    def meta(self):
        return f'{self.name} - {self.size} треков'

    def get_dict(self) -> dict:
        res = {
            'name': self.name,
            'tracks': []
        }
        for node in self:
            res['tracks'].append(node.data.path)
        return res

    def swap(self, item, direction) -> None:
        first_item = self.find_node(item)
        second_item = first_item.previous_item
        if direction == "down":
            second_item = first_item.next_item
        super().swap(first_item, second_item)

    def append(self, item: Composition) -> None:
        super().append(item)
        self.duration = duration_from_seconds(sum(map(lambda x: x.data.duration, self)))


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


def make_empty_playlist():
    return Playlist(head=None, name=None)


def make_playlist(data: list[Composition], name: str) -> Playlist:
    seq = create_node_sequence(data)
    return Playlist(seq, name=name)


if __name__ == '__main__':
    print(make_list_of_all())
