import sys
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon
def vid_player(vid_dir):
    app = QtGui.QApplication(sys.argv)
    vp = Phonon.VideoPlayer()
    media = Phonon.MediaSource('F:\\video.mp4')
    vp.load(media)
    vp.play()
    videoWidget = vp.videoWidget()
    if videoWidget.isFullScreen():
        videoWidget.exitFullScreen()
    else:
        videoWidget.enterFullScreen()
    vp.show()
    sys.exit(app.exec_())