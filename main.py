from PyQt5 import uic, QtWidgets
import sqlite3

def sair():
    tela.close()


def conectar():
    try:
        conn = sqlite3.connect('db/data.db')
        c = conn.cursor()
        print('Conectado com sucesso!')
    except:
        print('Banco inacessível!')


app = QtWidgets.QApplication([])
tela = uic.loadUi('ui/tela.ui')
tela_pessoa = uic.loadUi('ui/pessoa.ui')

tela.bt_pessoa.clicked.connect(tela_pessoa.show)
tela.bt_sair.clicked.connect(sair)

tela.show()
app.exec()
