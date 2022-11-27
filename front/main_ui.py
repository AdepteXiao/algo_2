from sys import argv, exit

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QRect, pyqtSignal, QSize
from PyQt5.QtGui import QPixmap

from back.composition import Composition
from back.database_interaction import Relator
from back.playlist import Playlist, PlaylistItem, make_list_of_all, make_random_playlist
from front.designer_maked.des_ui import Ui_MainWindow

from PyQt5.QtWidgets import (QScrollArea, QApplication, QWidget,
                             QMainWindow, QHBoxLayout, QVBoxLayout,
                             QLabel, QSpacerItem, QSizePolicy,
                             QPushButton, QSlider,
                             QGroupBox, QDialog, QCheckBox, QLineEdit)


def make_pixmap(img: bytes, size_x: int, size_y: int) -> QPixmap:
    pix = QPixmap()
    pix.loadFromData(img)
    pix = pix.scaled(size_x, size_y, Qt.AspectRatioMode.KeepAspectRatio,
                     Qt.TransformationMode.SmoothTransformation)
    return pix


class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.relator = Relator()
        self.playlists = self.relator.load_playlists()

        self.playlistsLayout = QHBoxLayout(self)

        self.playLine = PlayLineGroupBox(make_list_of_all())

        self.all_playlists = AllPlaylistsGroupbox(self.playlists)
        self.all_playlists.to_be_cur.connect(self.cur)
        self.all_playlists.add_new_list.connect(self.add)

        self.playlistsLayout.addWidget(self.all_playlists)

        self.playlist_boxes = dict()
        self.cur_plist = None
        for plist in self.playlists:
            new_box = CurPlaylistGroupbox(plist)
            new_box.updated.connect(self.update_handler)
            if plist.name != "Все треки":
                new_box.hide()
            else:
                self.cur_plist = new_box
            self.playlistsLayout.addWidget(new_box)
            self.playlist_boxes[plist.name] = new_box

        self.verticalLayout.addLayout(self.playlistsLayout)
        self.verticalLayout.addWidget(self.playLine)

    def update_handler(self):
        print(f"\033[0;32m[ MAIN]\033[0;0m {self.sender().name} обновился(типа)")

    def cur(self, name):
        print(f"\033[0;32m[ MAIN]\033[0;0m делает {name} текущим")
        self.cur_plist.hide()
        self.cur_plist = self.playlist_boxes[name]
        self.cur_plist.show()

    def add(self):
        print(f"\033[0;32m[ MAIN]\033[0;0m генерит новый плейлист")
        new_list = make_random_playlist(len(self.playlist_boxes))

        new_box = CurPlaylistGroupbox(new_list)
        new_box.updated.connect(self.update_handler)
        new_box.hide()

        self.playlistsLayout.addWidget(new_box)
        self.playlist_boxes[new_list.name] = new_box

        self.all_playlists.add_playlist(new_list)




class AllPlaylistsGroupbox(QGroupBox):
    to_be_cur = pyqtSignal(str)
    add_new_list = pyqtSignal()

    def __init__(self, playlists: list):
        super().__init__()
        self.setTitle('Плейлисты')

        self.layout = QVBoxLayout(self)

        self.scrollArea = QScrollArea()
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidgetLayout = QVBoxLayout(self.scrollAreaWidget)
        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.playlist_boxes = []
        for playlist in playlists:
            new_playlist = PlaylistGroupbox(playlist, self)
            new_playlist.want_to_be_cur.connect(self.pll_to_be_cur)

            self.playlist_boxes.append(new_playlist)
            self.scrollAreaWidgetLayout.addWidget(new_playlist)
        self.addNewListBox = AddNewListGroupbox(self)
        self.addNewListBox.want_to_add_list.connect(self.pll_to_be_added)

        self.scrollAreaWidgetLayout.addWidget(self.addNewListBox)

        self.scrollAreaWidgetLayout.addItem(
            QtWidgets.QSpacerItem(0, 40,
                                  QtWidgets.QSizePolicy.Minimum,
                                  QtWidgets.QSizePolicy.Expanding))
        self.layout.addWidget(self.scrollArea)

        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 350, 344))
        self.scrollArea.setMinimumSize(QSize(300, 0))

    def add_playlist(self, playlist: Playlist):
        new_playlist = PlaylistGroupbox(playlist, self)
        new_playlist.want_to_be_cur.connect(self.pll_to_be_cur)

        self.playlist_boxes.append(new_playlist)
        widgets_count = self.scrollAreaWidgetLayout.count()
        self.scrollAreaWidgetLayout.insertWidget(widgets_count - 2, new_playlist)

    def pll_to_be_cur(self, name):
        print(f"\033[0;39m[ALLPL]\033[0;0m понял, что {name} хочет стать текущим")
        self.to_be_cur.emit(name)

    def pll_to_be_added(self):
        print(f"\033[0;39m[ALLPL]\033[0;0m хочет добавить новый плейлист")
        self.add_new_list.emit()


class PlaylistGroupbox(QGroupBox):
    want_to_be_cur = pyqtSignal(str)

    def __init__(self, playlist: Playlist, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.name = playlist.name
        self.meta = QLabel(playlist.meta())
        self.layout.addWidget(self.meta)
        self.layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

    def mousePressEvent(self, event) -> None:
        print(f"\033[0;34m[PLLST]\033[0;0m {self.name} хочет стать текущим")
        self.want_to_be_cur.emit(self.name)


class AddNewListGroupbox(QGroupBox):
    want_to_add_list = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.add_new_box_layout = QHBoxLayout(self)
        self.label = QLabel("Добавить плейлист\n")
        self.add_new_box_layout.addWidget(self.label)
        # self.add_new_box_layout.addItem(
        #     QtWidgets.QSpacerItem(0, 40,
        #                           QtWidgets.QSizePolicy.Minimum,
        #                           QtWidgets.QSizePolicy.Expanding))

    def mousePressEvent(self, event) -> None:
        print(f"\033[0;34m[ADDER]\033[0;0m хочет добавить плейлист")
        self.want_to_add_list.emit()


class TrackGroupbox(QGroupBox):
    want_play = pyqtSignal()
    swap_dir = pyqtSignal(str)

    def __init__(self, composition: Composition, parent=None):
        super().__init__(parent)

        self.upDownLayout = QHBoxLayout()
        self.up = QPushButton("↑")
        self.down = QPushButton("↓")
        self.up.setMaximumSize(QSize(15, 30))
        self.down.setMaximumSize(QSize(15, 30))
        self.up.clicked.connect(self.swap_direction)
        self.down.clicked.connect(self.swap_direction)

        self.layout = QHBoxLayout(self)
        self.pic = QLabel()
        self.pic.setPixmap(make_pixmap(composition.image, 32, 32))
        self.name = composition.name
        self.author = composition.author
        self.meta = QLabel(repr(composition))
        self.meta_dur = QLabel(composition.dur())
        self.composition = composition
        self.layout.addLayout(self.upDownLayout)
        self.upDownLayout.addWidget(self.up)
        self.upDownLayout.addWidget(self.down)
        self.layout.addWidget(self.pic)
        self.layout.addWidget(self.meta)
        spacerItem = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.layout.addItem(spacerItem)
        self.layout.addWidget(self.meta_dur)

    def mousePressEvent(self, event) -> None:
        print(f"\033[0;35m[TRACK]\033[0;0m {self.name} хочет играть")
        self.want_play.emit()

    def swap_direction(self):
        direction = self.sender().text()
        print(f"\033[0;35m[TRACK]\033[0;0m {self.name} хочет меняться {direction}")
        self.swap_dir.emit(direction)

    # def swap_up(self):
    #     print(f"\033[0;35m[TRACK]\033[0;0m {self.name} хочет меняться вверх")
    #     self.swap_tracks.emit("up")

    # def swap_down(self):
    #     print(f"\033[0;35m[TRACK]\033[0;0m {self.name} хочет меняться вниз")
    #     self.swap_tracks.emit("down")


class CurPlaylistGroupbox(QGroupBox):
    updated = pyqtSignal()
    list_updated = pyqtSignal(int)

    def __init__(self, playlist: Playlist):
        super().__init__()
        self.playlist = playlist
        self.setTitle(playlist.name)

        self.layout = QVBoxLayout(self)

        self.scrollArea = QScrollArea()
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidgetLayout = QVBoxLayout(self.scrollAreaWidget)
        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.track_boxes = []
        for song in playlist:
            new_track = TrackGroupbox(song.data, self)
            new_track.want_play.connect(self.play_slot)
            new_track.swap_dir.connect(self.swap_tracks)
            self.track_boxes.append(new_track)
            self.scrollAreaWidgetLayout.addWidget(new_track)

        if self.track_boxes:
            self.cur_track = self.track_boxes[0]
        else:
            self.cur_track = None

        spacerItem = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.scrollAreaWidgetLayout.addItem(spacerItem)

        self.playlist_meta = QLabel(repr(playlist))

        self.layout.addWidget(self.playlist_meta)
        self.layout.addWidget(self.scrollArea)

        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumSize(QSize(500, 0))
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 350, 344))

    @property
    def name(self):
        return self.playlist.name

    def play_slot(self):
        print(
            f"\033[0;36m[CURPL]\033[0;0m Плейлист {self.playlist.name} "
            f"понял что {self.sender().name} хочет играть")
        # self.playlist.current_track = self.sender().composition
        self.updated.emit()

    def swap_tracks(self, direction):
        print(
            f"\033[0;36m[CURPL]\033[0;0m Плейлист {self.playlist.name} понял что {self.sender().name} "
            f"хочет поменяться местами {direction}")
        track = self.sender().composition
        self.playlist.swap(track, direction)
        self.upd()

    def upd(self, index=-1):
        print(f"\033[0;36m[CURPL]\033[0;0m Плейлист {self.playlist.name} обновился")
        is_filled = False
        if self.track_boxes:
            self.track_boxes.clear()
            is_filled = True
        count = self.scrollAreaWidgetLayout.count()
        for i in range(0, count):
            item = self.scrollAreaWidgetLayout.itemAt(i)
            if i == count - 1:
                self.scrollAreaWidgetLayout.removeItem(item)
            else:
                item.widget().deleteLater()
        for song in self.playlist:
            track = TrackGroupbox(song.data)
            track.swap_dir.connect(self.swap_tracks)
            track.clicked.connect(self.play_slot)
            self.scrollAreaWidgetLayout.addWidget(track)
            self.track_boxes.append(track)

        spacerItem = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.scrollAreaWidgetLayout.addItem(spacerItem)

        if not is_filled:
            self.cur_track = self.track_boxes[0]

        self.update_meta()
        self.list_updated.emit(index)

    def update_meta(self):
        self.playlist_meta.setText(str(self.playlist))


class PlayLineGroupBox(QGroupBox):
    def __init__(self, playlist: Playlist):
        super().__init__()
        self.cur_playlist = playlist
        self.cur_track = self.cur_playlist.current_track
        self.setTitle(playlist.name)

        self.layout = QVBoxLayout(self)

        self.metaLayout = QHBoxLayout(self)
        self.pic = QLabel()
        self.pic.setPixmap(make_pixmap(self.cur_track.image, 32, 32))
        self.name = QLabel(self.cur_track.name)
        self.metaLayout.addWidget(self.pic)
        self.metaLayout.addWidget(self.name)
        spacerItem = QtWidgets.QSpacerItem(1000, 0, QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.metaLayout.addItem(spacerItem)

        self.trackProgressLayout = QHBoxLayout(self)
        self.cur_dur = QLabel('00:00')
        self.bar = QSlider()
        self.bar.setOrientation(Qt.Horizontal)
        self.dur = QLabel(self.cur_track.dur())
        self.trackProgressLayout.addWidget(self.cur_dur)
        self.trackProgressLayout.addWidget(self.bar)
        self.trackProgressLayout.addWidget(self.dur)

        self.controlsLayout = QHBoxLayout(self)
        self.prev = QPushButton("<-")
        self.pause = QPushButton("||")
        self.play = QPushButton("|>")
        self.next = QPushButton("->")
        self.controlsLayout.addWidget(self.prev)
        self.controlsLayout.addWidget(self.pause)
        self.controlsLayout.addWidget(self.play)
        self.controlsLayout.addWidget(self.next)

        self.layout.addLayout(self.metaLayout)
        self.layout.addLayout(self.trackProgressLayout)
        self.layout.addLayout(self.controlsLayout)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = MainUI()
    ex.show()
    app.exec_()
    exit()
