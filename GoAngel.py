import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui

class FenPrincipale(QMainWindow):
    def __init__(self):
        super(FenPrincipale, self).__init__()
        self.setWindowIcon(QtGui.QIcon('epic_browser.ico'))
        self.navigateur=QWebEngineView()
        self.navigateur.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.navigateur)
        self.showMaximized()

        #naxbar
        navbar=QToolBar()
        self.addToolBar(navbar)

        retour_btn=QAction('Retour',self)
        retour_btn.triggered.connect(
            self.navigateur.back)
        navbar.addAction(retour_btn)

        refresh_btn = QAction('Rafraichir', self)
        refresh_btn.triggered.connect(
            lambda:
            self.navigateur.reload())
        navbar.addAction(refresh_btn)

        next_btn = QAction('Avancer', self)
        next_btn.triggered.connect(
            lambda:
            self.navigateur.forward())
        navbar.addAction(next_btn)

        accueil_btn = QAction('Accueil', self)
        accueil_btn.triggered.connect(
            self.url_accueil)
        navbar.addAction(accueil_btn)

        self.urlbar=QLineEdit()
        self.urlbar.returnPressed.connect(self.navigation)
        navbar.addWidget(self.urlbar)

        self.navigateur.urlChanged.connect(self.update_url)

    def url_accueil(self):
        self.navigateur.setUrl(QUrl('http://google.com'))

    def navigation(self):
        url=self.urlbar.text()
        self.navigateur.setUrl(QUrl(url))

    def update_url(self, url):
        self.urlbar.setText(url.toString())


app=QApplication(sys.argv)
QApplication.setApplicationName('Go Devil')
fenetre=FenPrincipale()
app.exec_()
