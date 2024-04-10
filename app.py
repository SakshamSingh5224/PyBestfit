from PyQt5 import QtWidgets, QtGui


if __name__ == "__main__":
    app = QtWidgets.QApplication(['BestFit Algorithm'])  # Use QtWidgets for modern PyQt5 applications
    window = BestfitApp()
    window.show()
    sys.exit(app.exec_())  # Use sys.exit for cleaner exit handling
