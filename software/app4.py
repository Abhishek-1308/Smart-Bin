import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from pandas import Timestamp 


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.cred = credentials.Certificate("key.json")
        self.obj = firebase_admin.initialize_app(self.cred, { 'databaseURL': "https://loggbwv-default-rtdb.firebaseio.com/"})
        self.ui.h1status.setText("STATUS1")

        print("Firebase Logged in") 
        
        db.reference('/House1').listen(self.updatehouse1)
        db.reference('/House2').listen(self.updatehouse2)
        self.ui.pushButton.clicked.connect(self.Refresh)

    def Refresh(self):
        print("Clicked Refreshed")
        self.updatehouse1(None)
        self.updatehouse2(None)

    def updatehouse1(self,event):
        house1 = db.reference('/House1').get()
        self.h1garbage_weight = house1['GarbageWeight']
        self.h1garbage_volume = house1['GarbageVolume']
        self.ui.lcdNumber.display("HOUSE 1")
        currtime = Timestamp.now()
        self.ui.pushButton.setText(f"Refreshed at :{currtime}")
        self.ui.lcdNumber_2.display(self.h1garbage_weight)
        self.ui.lcdNumber_3.display(self.h1garbage_volume)
        if self.h1garbage_volume > 45000:
            self.ui.h1status.setText("OVERLOADED")
            self.ui.h1status.setStyleSheet("color:red")

        else:
            self.status_h1 = 'OK'
            self.ui.h1status.setText("GOOD")
            self.ui.h1status.setStyleSheet("color:green")

    def updatehouse2(self,event):
        house2 = db.reference('/House2').get()
        self.h2garbage_weight = house2['GarbageWeight']
        self.h2garbage_volume = house2['GarbageVolume']
        self.ui.lcdNumber_5.display("HOUSE 2")
        currtime = Timestamp.now()
        self.ui.pushButton.setText(f"Refreshed at :{currtime}")
        self.ui.lcdNumber_6.display(self.h2garbage_weight)
        self.ui.lcdNumber_7.display(self.h2garbage_volume)
        if self.h2garbage_volume > 25000:
            self.ui.h2status.setText("OVERLOADED")
            self.ui.h2status.setStyleSheet("color:red")

        else:
            self.status_h2 = 'OK'
            self.ui.h2status.setText("GOOD")
            self.ui.h2status.setStyleSheet("color:green")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle("REALTIME GARBAGE MONITOR")
    widget.show()
    sys.exit(app.exec())
 