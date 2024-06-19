from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas
from datetime import datetime

# conectando o banco
banco = mysql.connector.connect(
        host= "localhost",
        user= "root",
        password= "vip123",
        database= "bancoLed"
)

def main ():
    print("Cadastrado")

def ledCadastro():
    campoNome = led.txtnome.text()
    
    if led.ledred.isChecked():
        corLed = "vermelho"
    elif led.ledyellow.isChecked():
        corLed = "Amarelo"
    elif led.ledgreen.isChecked():
        corLed = "Verde"
    else:
        corLed = "Cor não informada"

    dataAtual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Formata a data atual

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO tbl_led (nome, colorLed, dataLigado) VALUES (%s, %s, %s )"
    dados = (str(campoNome),corLed, dataAtual)
    cursor.execute(comando_SQL, dados)
    banco.commit()

    led.txtnome.setText("")
   

    print("led cadastrado com sucesso!")

app = QtWidgets.QApplication([])
led = uic.loadUi("led.ui")
led.btnEnviar.clicked.connect(ledCadastro)
led.btnEnviar.clicked.connect(main)

led.show()
app.exec()