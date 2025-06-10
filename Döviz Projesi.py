import sys
import  requests
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout


class Pencere (QWidget) :

    def __init__(self):

        super().__init__()

        self.init_ui ()

    def init_ui (self) :

        self.yazi_alanı = QLabel(" ")
        self.kuru_getir = QPushButton ("Getir")
        self.temizle = QPushButton ("Temizle")

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazi_alanı)
        v_box.addStretch()
        v_box.addWidget(self.kuru_getir)
        v_box.addWidget(self.temizle)


        h_box = QHBoxLayout()

        h_box.addLayout(v_box)

        self.setLayout(h_box)

        self.setWindowTitle("Döviz Programı")

        self.temizle.clicked.connect (self.yaziyi_temizle)
        self.kuru_getir.clicked.connect (self.kur_getir)

        self.show()

    def yaziyi_temizle(self):

        self.yazi_alanı.clear()

    def kur_getir(self):

        try :

            response = requests.get ("https://api.exchangerate-api.com/v4/latest/USD")

            data = response.json()

            kur = data["rates"]["TRY"]

            self.yazi_alanı.setText (f"Güncel USD/TRY Kuru : {kur} ")

        except :

            self.yazi_alanı.setText("Kur bilgisi alınamadı.")


app =QApplication (sys.argv)

pencere = Pencere ()

sys.exit(app.exec_())

