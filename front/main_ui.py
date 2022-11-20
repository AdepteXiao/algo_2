from sys import argv, exit

from PyQt5 import QtWidgets

from back.composition import Composition
from back.playlist import Playlist, PlaylistItem
from front.designer_maked.des_ui import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QApplication, QGroupBox


class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class TrackGroupbox(QGroupBox):
    def __init__(self, composition: Composition):
        super().__init__()
        self.composition = composition


class CurPlaylistGroupbox(QGroupBox):
    def __init__(self, playlist: Playlist):
        super().__init__()
        self.playlist = playlist
        self.track = TrackGroupbox


if __name__ == '__main__':
    app = QApplication(argv)
    ex = MainUI()
    ex.show()
    app.exec_()
    exit()
