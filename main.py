from PyQt5 import uic, QtWidgets
import sqlite3, random

def gerar():
    conn = sqlite3.connect('db/data.db')
    c = conn.cursor()

    tela.resul.clear()

    tabela = tela.input_nom_tabela.text()
    
    sql_nomes = c.execute("SELECT * FROM NOMES;").fetchall()
    sql_sobrenomes = c.execute("SELECT * FROM SOBRENOMES;").fetchall()
    sql_uf = c.execute("SELECT * FROM UF;").fetchall()

    r = ''
    for i_nomes,i_sobrenomes,i_ufs in zip(sql_nomes,sql_sobrenomes,sql_uf):
        if tela.cb_nome.isChecked() and tela.cb_sobrenome.isChecked():
            print(i_nomes,i_sobrenomes)            
            r += f"INSERT INTO {tabela}(NOME,SOBRENOME) VALUES ('{random.choice(i_nomes)}','{random.choice(i_sobrenomes)}');\n"
        elif tela.cb_nome.isChecked():            
            r += f"INSERT INTO {tabela}(NOME) VALUES ('{i_nomes[1]}');\n"        
        elif tela.cb_sobrenome.isChecked():            
            r += f"INSERT INTO {tabela}(SOBRENOME) VALUES ('{i_sobrenomes[1]}');\n"
        else:
            pass

    tela.resul.append(r)

app = QtWidgets.QApplication([])
tela = uic.loadUi('gui/tela.ui')

tela.bt_gerar.clicked.connect(gerar)

tela.show()
app.exec()

