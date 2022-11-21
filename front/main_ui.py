from sys import argv, exit

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QRect, pyqtSignal, QSize
from PyQt5.QtGui import QPixmap

from back.composition import Composition
from back.database_interaction import Relator
from back.playlist import Playlist, PlaylistItem, make_list_of_all
from front.designer_maked.des_ui import Ui_MainWindow

from PyQt5.QtWidgets import (QScrollArea, QApplication, QWidget,
                             QMainWindow, QHBoxLayout, QVBoxLayout,
                             QLabel, QSpacerItem, QSizePolicy,
                             QPushButton, QTabWidget, QSlider,
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
        self.playLine = PlayLineGroupBox(make_list_of_all())
        self.all_playlists = AllPlaylistsGroupbox(self.relator)
        self.cur_playlist = CurPlaylistGroupbox(make_list_of_all())
        self.cur_playlist.updated.connect(self.update_handler)
        self.playlistsLayout.addWidget(self.all_playlists)
        self.allPlaylistsGroupBox.hide()
        self.playlistsLayout.addWidget(self.cur_playlist)
        self.curPlaylistGroupBox.hide()
        self.verticalLayout.addWidget(self.playLine)
        self.playLineGroupBox.hide()

    def update_handler(self):
        print(f"{self.sender().name} обновился")


class AllPlaylistsGroupbox(QGroupBox):
    def __init__(self, relator: Relator):
        super().__init__()
        self.setTitle('Плейлисты')
        self.layout = QVBoxLayout(self)
        self.scrollArea = QScrollArea()
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidgetLayout = QVBoxLayout(self.scrollAreaWidget)
        self.scrollArea.setWidget(self.scrollAreaWidget)
        self.playlist_boxes = []
        for playlist in relator.load_playlists():
            new_playlist = PlaylistGroupbox(playlist, self)
            # new_playlist.want_to_be_cur.connect(self.)
            self.playlist_boxes.append(new_playlist)
            self.scrollAreaWidgetLayout.addWidget(new_playlist)
        spacerItem = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scrollAreaWidgetLayout.addItem(spacerItem)
        self.layout.addWidget(self.scrollArea)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 350, 344))
        self.scrollArea.setMinimumSize(QSize(300, 0))


class PlaylistGroupbox(QGroupBox):
    want_to_be_cur = pyqtSignal()

    def __init__(self, playlist: Playlist, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.playlist = playlist
        self.name = playlist.name
        self.duration = playlist.duration
        self.cur_track = playlist.current_track
        self.meta = QLabel(playlist.meta())
        self.layout.addWidget(self.meta)
        self.layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

    def mousePressEvent(self, event) -> None:
        print(f"{self.name} хочет стать настоящим")
        self.want_to_be_cur.emit()


class TrackGroupbox(QGroupBox):
    want_play = pyqtSignal()

    def __init__(self, composition: Composition, parent=None):
        super().__init__(parent)

        self.upDownLayout = QHBoxLayout()
        self.up = QPushButton("↑")
        self.down = QPushButton("↓")
        self.up.setMaximumSize(QSize(15, 30))
        self.down.setMaximumSize(QSize(15, 30))

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
        spacerItem = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout.addItem(spacerItem)
        self.layout.addWidget(self.meta_dur)

    def mousePressEvent(self, event) -> None:
        print(f"{self.name} хочет играть")
        self.want_play.emit()


class CurPlaylistGroupbox(QGroupBox):
    updated = pyqtSignal()

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
            self.track_boxes.append(new_track)
            self.scrollAreaWidgetLayout.addWidget(new_track)

        if self.track_boxes:
            self.cur_track = self.track_boxes[0]
        else:
            self.cur_track = None

        spacerItem = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
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
        print(f"Плейлист {self.playlist.name} понял что {self.sender().name} хочет играть")
        # self.playlist.current_track = self.sender().composition
        self.updated.emit()


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
        spacerItem = QtWidgets.QSpacerItem(1000, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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