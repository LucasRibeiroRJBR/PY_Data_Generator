from PyQt5 import uic, QtWidgets
import sqlite3

def gerar():
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    tabela = tela.input_nom_tabela.text()
    
    sql = c.execute("SELECT * FROM NOMES;").fetchall()
    r = ''
    for i in sql:
        if tela.cb_nome.isChecked():            
            r += f"INSERT INTO {tabela}(ID,NOME) VALUES (0,'{i[1]}');\n"

    tela.resul.append(r)

app = QtWidgets.QApplication([])
tela = uic.loadUi('gui/tela.ui')

tela.bt_gerar.clicked.connect(gerar)

tela.show()
app.exec()

