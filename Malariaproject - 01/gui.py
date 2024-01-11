from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os

class Ui_MainWindow(object):
    def __init__(self, model):
        self.model = model
        self.correct_predictions = 0
        self.total_predictions = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(426, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(30, 10, 361, 30))
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setText("Malaria Identification App")

        self.graphicsScene = QtWidgets.QGraphicsScene()

        self.graphicsView = QtWidgets.QGraphicsView(self.graphicsScene, self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 50, 361, 231))
        self.graphicsView.setObjectName("graphicsView")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(113, 10, 200, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonEvent)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 300, 200, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(163, 340, 200, 20))
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 18))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Malaria Identification"))
        self.pushButton.setText(_translate("MainWindow", "Upload Image"))

    def load_image(self, img_path):
        img = image.load_img(img_path, target_size=(100, 100))
        img_tensor = image.img_to_array(img)
        img_tensor = np.expand_dims(img_tensor, axis=0)
        img_tensor /= 255.
        return img_tensor

    def activation(self, number):
        return "Uninfected" if number >= 0.5 else "Parasitized"

    def buttonEvent(self):
        filename, _ = QFileDialog.getOpenFileName(None, "Open Image File", "", "Image files (*.jpg *.png)")
        if filename:
            self.getImage(filename)

    def predict(self, path):
        return self.activation(self.model.predict(self.load_image(path))[0][0])

    def getImage(self, filename):
        self.graphicsScene.clear()
        self.pixMap = QtGui.QPixmap(filename)
        self.pixMapItem = QtWidgets.QGraphicsPixmapItem(self.pixMap)
        self.graphicsScene.addItem(self.pixMapItem)
        self.graphicsView.show()

        prediction = self.predict(filename)

        self.label.setText("Predicted: " + prediction)
        isCorrect = "Yes" if ("Uninfected" in filename and prediction == "Uninfected") or ("Parasitized" in filename and prediction == "Parasitized") else "No"
        self.label_2.setText("Correct: " + isCorrect)

        self.correct_predictions += 1 if isCorrect == "Yes" else 0
        self.total_predictions += 1

        accuracy = (self.correct_predictions / self.total_predictions) * 100 if self.total_predictions > 0 else 0
        self.label_2.setText(f"{self.label_2.text()}, Accuracy: {accuracy:.2f}%")

        # Show accuracy message box
        QMessageBox.information(None, "Accuracy", f"Accuracy: {accuracy:.2f}%")

model = load_model("model.h5")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(model)
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())
