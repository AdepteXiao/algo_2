from sys import argv, exit

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QRect, pyqtSignal
from PyQt5.QtGui import QPixmap

from back.composition import Composition
from back.database_interaction import Interaction
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
        self.cur_playlist = CurPlaylistGroupbox(make_list_of_all())
        self.cur_playlist.updated.connect(self.update_handler)
        self.playlistsLayout.addWidget(self.cur_playlist)
        self.curPlaylistGroupBox.hide()

    def update_handler(self):
        print(f"{self.sender().name} обновился")


class AllPlaylists(QGroupBox):
    def __init__(self, interaction: Interaction):
        super().__init__()
        self.scrollArea = QScrollArea()
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidgetLayout = QVBoxLayout(self.scrollAreaWidget)
        self.scrollArea.setWidget(self.scrollAreaWidget)
        self.playlist_boxes = []
        for playlist in interaction.load():
            new_playlist = TrackGroupbox(playlist.data, self)
            # new_playlist.want_play.connect(self.play_slot)
            self.playlist_boxes.append(new_playlist)
            self.scrollAreaWidgetLayout.addWidget(new_playlist)


class PlaylistGroupbox(QGroupBox):
    def __init__(self, playlist: Playlist, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.playlist = playlist
        self.name = playlist.name
        self.duration = playlist.duration
        self.cur_track = playlist.current_track
        self.meta = playlist.meta()
        self.layout.addWidget(self.meta)


class TrackGroupbox(QGroupBox):
    want_play = pyqtSignal()

    def __init__(self, composition: Composition, parent=None):
        super().__init__(parent)

        self.layout = QHBoxLayout(self)
        self.pic = QLabel()
        self.pic.setPixmap(make_pixmap(composition.image, 32, 32))
        self.name = composition.name
        self.author = composition.author
        self.meta = QLabel(repr(composition))
        self.meta_dur = QLabel(composition.dur())
        self.composition = composition
        self.layout.addWidget(self.pic)
        self.layout.addWidget(self.meta)
        self.layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.layout.addWidget(self.meta_dur)
        self.layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

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

        self.layout.addWidget(QLabel("Пип"))
        self.layout.addWidget(self.scrollArea)

        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidget.setGeometry(QRect(0, 0, 350, 344))

    @property
    def name(self):
        return self.playlist.name

    def play_slot(self):
        print(f"Плейлист {self.playlist.name} понял что {self.sender().name} хочет играть")
        # self.playlist.current_track = self.sender().composition
        self.updated.emit()


if __name__ == '__main__':
    app = QApplication(argv)
    ex = MainUI()
    ex.show()
    app.exec_()
    exit()
