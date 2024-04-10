from PyQt5 import QtCore, QtWidgets


class Ui_BestFit(object):
    def setupUi(self, BestFit):
        BestFit.setObjectName("BestFit")
        BestFit.resize(800, 500)
        BestFit.setMinimumSize(QtCore.QSize(800, 500))
        BestFit.setMaximumSize(QtCore.QSize(800, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BestFit.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(BestFit)
        self.centralwidget.setObjectName("centralwidget")

        self.memoryAlloc = QtWidgets.QPushButton(self.centralwidget)
        self.memoryAlloc.setGeometry(QtCore.QRect(637, 420, 131, 41))
        self.memoryAlloc.setObjectName("memoryAlloc")

        self.randomCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.randomCheck.setGeometry(QtCore.QRect(350, 420, 141, 41))
        self.randomCheck.setObjectName("randomCheck")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 751, 391))
        self.tabWidget.setObjectName("tabWidget")

        self.processTab = QtWidgets.QWidget()
        self.processTab.setObjectName("processTab")

        self.tableMemory = QtWidgets.QTableView(self.processTab)
        self.tableMemory.setGeometry(QtCore.QRect(0, 0, 749, 355))
        self.tableMemory.setObjectName("tableMemory")

        self.tabWidget.addTab(self.processTab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.processTab), "Memory")

        self.memoryTab = QtWidgets.QWidget()
        self.memoryTab.setAccessibleName("")
        self.memoryTab.setObjectName("memoryTab")

        self.tableProcess = QtWidgets.QTableView(self.memoryTab)
        self.tableProcess.setGeometry(QtCore.QRect(0, 0, 749, 355))
        self.tableProcess.setObjectName("tableProcess")

        self.tabWidget.addTab(self.memoryTab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(memoryTab), "Processes")

        self.logTab = QtWidgets.QWidget()
        self.logTab.setObjectName("logTab")

        self.logView = QtWidgets.QTextEdit(self.logTab)
        self.logView.setEnabled(True)
        self.logView.setGeometry(QtCore.QRect(0, 0, 761, 361))
        self.logView.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.logView.setReadOnly(True)
        self.logView.setTabStopWidth(20)
        self.logView.setObjectName("logView")

        self.tabWidget.addTab(self.logTab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logTab), "Logs")

        self.updateInfo = QtWidgets.QPushButton(self.centralwidget)
        self.updateInfo.setGeometry(QtCore.QRect(497, 420, 131, 41))
        self.updateInfo.setObjectName("updateInfo")

        BestFit.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(BestFit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")

        self.menuAjudar = QtWidgets.QMenu(self.menubar)
        self.menuAjudar.setSeparatorsCollapsible(True)
        self.menuAjudar.setObjectName("menuAjudar")
        BestFit.setMenuBar(self.menubar)

        self.actionGithub = QtWidgets.QAction(BestFit)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/github.png"),


