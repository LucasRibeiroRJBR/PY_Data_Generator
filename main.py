from PyQt5 import uic, QtWidgets, QtGui
import sqlite3

def sair():
    tela.close()

def conectar():
    pass


app = QtWidgets.QApplication([])
tela = uic.loadUi('ui/tela.ui')
tela_pessoa = uic.loadUi('ui/pessoa.ui')

# Definição stylesheet
estilo = open('qss/estilo.qss').read()
app.setStyleSheet(estilo)
tela.setStyleSheet(estilo)

tela_pessoa.lb_status_conexao.setPixmap(QtGui.QPixmap('img/db_off.png'))
tela_pessoa.bt_desconectar.clicked.connect(desconectar)
tela_pessoa.bt_conectar.clicked.connect(conectar)
tela.bt_pessoa.clicked.connect(tela_pessoa.show)
tela.bt_sair.clicked.connect(sair)

tela.show()
app.exec()
