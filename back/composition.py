from tinytag import TinyTag
from back.utils import duration_from_seconds


class Composition:
    def __init__(self, path):
        self.__path = path
        self.tag = TinyTag.get(path, image=True)

    @property
    def duration(self):
        return self.tag.duration

    @property
    def path(self):
        return self.__path

    @property
    def name(self):
        return self.tag.title

    @property
    def author(self):
        return self.tag.artist

    @property
    def image(self):
        return self.tag.get_image()

    def __repr__(self):
        return f"{self.author} - {self.name}"

    def dur(self):
        return f'{duration_from_seconds(self.duration)}'


def get_comp(paths):
    return [Composition(t_path) for t_path in paths]
