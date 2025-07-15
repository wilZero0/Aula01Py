
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


app = QApplication([])
janela = QWidget()
janela.setWindowTitle("minha primeira janela!")
rotulo = QLabel("Olá, mundo!", parent=janela)

janela.resize(1920,1080)

janela.show()

app.exec_()