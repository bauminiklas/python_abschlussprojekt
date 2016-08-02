from PyQt4 import QtGui, QtCore, uic

from ReferenceSurvey import ReferenceSurvey
from Survey import Survey

import sys
import os



Ui_MainWindow, WindowBaseClass = uic.loadUiType("main_window.ui")

class UIEvaluationHelper(WindowBaseClass, Ui_MainWindow):
    def __init__(self, parent=None):
        WindowBaseClass.__init__(self, parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
#        self.labelReferencePicture.setMouseTracking(True)
        


if __name__ == "__main__":
#Ab hier richtiges Programm

    referenceSurvey = ReferenceSurvey()
    list_of_surveys = [Survey(f, referenceSurvey) for f in os.listdir('boegen')]



#Erstmal egal!    
    app = QtGui.QApplication(sys.argv)
    dialog = UIEvaluationHelper()
#    dialog.show()
    sys.exit(app.exec_())
    
    
    