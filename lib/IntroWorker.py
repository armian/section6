from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtMultimedia import QSound

class IntroWorker(QObject):
    startMsg = pyqtSignal(str, str)
    @pyqtSlot()
    def playBgm(self):
        self.intro = QSound("/Users/armian/Inflearn/workspace/section6/resource/intro.wav")
        self.intro.play()
        self.startMsg.emit("Anonymous",self.intro.fileName())
