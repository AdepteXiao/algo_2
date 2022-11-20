import json
from back.playlist import Playlist, make_list_of_all, create_node_sequence
from back.composition import get_comp


class Interaction:

    def __init__(self) -> None:
        self.json_file = r"C:\Education\algo2\tracks\songs"
        with open(self.json_file, 'r', encoding="utf-8") as file:
            tmp = json.load(file)
            tmp[0] = make_list_of_all().get_dict()
        with open(self.json_file, 'w', encoding="utf-8") as file:
            json.dump(tmp, file, indent=4, ensure_ascii=False)

    def save(self, list_of_playlists: list[Playlist]) -> None:
        with open(self.json_file, 'w', encoding='utf-8') as file:
            res = []
            for pllst in list_of_playlists:
                res.append(pllst.get_dict())
            json.dump(res, file, indent=4, ensure_ascii=False)

    def load(self) -> list:
        with open(self.json_file, 'r', encoding='utf-8') as file:
            return json.load(file)

    def load_playlists(self) -> list:
        list_of_playlists = self.load()
        res = []
        for playlist_data in list_of_playlists:
            res.append(Playlist(name=playlist_data['name'],
                                head=create_node_sequence(
                                    get_comp(playlist_data['tracks']))))
        return res
