
'''
MIT License

Copyright (c) 2023 Stefan Unković

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sys
import re
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_Calculator(object):
	def setupUi(self, Calculator):
		if Calculator.objectName():
			Calculator.setObjectName(u"Calculator")

		Calculator.resize(301, 408)
		Calculator.setMinimumSize(QSize(301, 408))
		Calculator.setMaximumSize(QSize(301, 408))
		icon = QIcon("calc.png")
		Calculator.setWindowIcon(icon)
		palette = QPalette()
		brush = QBrush(QColor(35, 35, 35, 255))
		brush.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.Base, brush)
		brush1 = QBrush(QColor(54, 54, 54, 255))
		brush1.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.Window, brush1)
		palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
		palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
		palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
		palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
		Calculator.setPalette(palette)
		self.listView = QListView(Calculator)
		self.listView.setObjectName(u"listView")
		self.listView.setEnabled(True)
		self.listView.setGeometry(QRect(10, 10, 281, 73))
		palette1 = QPalette()
		brush2 = QBrush(QColor(255, 255, 255, 255))
		brush2.setStyle(Qt.SolidPattern)
		palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
		brush3 = QBrush(QColor(99, 99, 99, 255))
		brush3.setStyle(Qt.SolidPattern)
		palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
		brush4 = QBrush(QColor(149, 149, 149, 255))
		brush4.setStyle(Qt.SolidPattern)
		palette1.setBrush(QPalette.Active, QPalette.Light, brush4)
		brush5 = QBrush(QColor(124, 124, 124, 255))
		brush5.setStyle(Qt.SolidPattern)
		palette1.setBrush(QPalette.Active, QPalette.Midlight, brush5)
		brush6 = QBrush(QColor(49, 49, 49, 255))
		brush6.setStyle(Qt.SolidPattern)
		palette1.setBrush(QPalette.Active, QPalette.Dark, brush6)
		brush7 = QBrush(QColor(66, 66, 66, 255))
		brush7.setStyle(Qt.SolidPattern)
		palette1.setBrush(QPalette.Active, QPalette.Mid, brush7)
		palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
		palette1.setBrush(QPalette.Active, QPalette.BrightText, brush2)
		palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
		brush8 = QBrush(QColor(80, 80, 80, 255))
		brush8.setStyle(Qt.SolidPattern)
		palette1.setBrush(QPalette.Active, QPalette.Base, brush8)
		palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
		brush9 = QBrush(QColor(0, 0, 0, 255))
		brush9.setStyle(Qt.SolidPattern)
		palette1.setBrush(QPalette.Active, QPalette.Shadow, brush9)
		palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
		brush10 = QBrush(QColor(255, 255, 220, 255))
		brush10.setStyle(Qt.SolidPattern)
		palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
		palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush9)
		brush11 = QBrush(QColor(255, 255, 255, 128))
		brush11.setStyle(Qt.SolidPattern)
		#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
		#endif
		palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
		palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
		palette1.setBrush(QPalette.Inactive, QPalette.Light, brush4)
		palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
		palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
		palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
		palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
		palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
		palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
		palette1.setBrush(QPalette.Inactive, QPalette.Base, brush8)
		palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
		palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush9)
		palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
		palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
		palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush9)
		#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
		#endif
		palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
		palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
		palette1.setBrush(QPalette.Disabled, QPalette.Light, brush4)
		palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush5)
		palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush6)
		palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
		palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
		palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
		palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
		palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
		palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
		palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush9)
		palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
		palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
		palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush9)
		#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
		#endif
		self.listView.setPalette(palette1)
		self.listView.setMouseTracking(True)
		self.listView.setSelectionRectVisible(False)
		self.button_num9 = QPushButton(Calculator)
		self.button_num9.setObjectName(u"button_num9")
		self.button_num9.setGeometry(QRect(150, 100, 61, 81))
		palette2 = QPalette()
		palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
		brush12 = QBrush(QColor(97, 97, 97, 255))
		brush12.setStyle(Qt.SolidPattern)
		palette2.setBrush(QPalette.Active, QPalette.Button, brush12)
		palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
		palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
		palette2.setBrush(QPalette.Active, QPalette.Base, brush12)
		palette2.setBrush(QPalette.Active, QPalette.Window, brush12)
		brush13 = QBrush(QColor(255, 255, 255, 128))
		brush13.setStyle(Qt.NoBrush)
		#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
		#endif
		palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
		palette2.setBrush(QPalette.Inactive, QPalette.Button, brush12)
		palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
		palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
		palette2.setBrush(QPalette.Inactive, QPalette.Base, brush12)
		palette2.setBrush(QPalette.Inactive, QPalette.Window, brush12)
		brush14 = QBrush(QColor(255, 255, 255, 128))
		brush14.setStyle(Qt.NoBrush)
		#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
		#endif
		palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
		palette2.setBrush(QPalette.Disabled, QPalette.Button, brush12)
		palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
		palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
		palette2.setBrush(QPalette.Disabled, QPalette.Base, brush12)
		palette2.setBrush(QPalette.Disabled, QPalette.Window, brush12)
		brush15 = QBrush(QColor(255, 255, 255, 128))
		brush15.setStyle(Qt.NoBrush)
		#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
		#endif
		self.button_num9.setPalette(palette2)
		self.button_num9.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_num8 = QPushButton(Calculator)
		self.button_num8.setObjectName(u"button_num8")
		self.button_num8.setGeometry(QRect(80, 100, 61, 81))
		self.button_num8.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_num7 = QPushButton(Calculator)
		self.button_num7.setObjectName(u"button_num7")
		self.button_num7.setGeometry(QRect(10, 100, 61, 81))
		self.button_num7.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_plus = QPushButton(Calculator)
		self.button_plus.setObjectName(u"button_plus")
		self.button_plus.setGeometry(QRect(230, 100, 61, 51))
		palette3 = QPalette()
		palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
		palette3.setBrush(QPalette.Active, QPalette.Button, brush12)
		palette3.setBrush(QPalette.Active, QPalette.Text, brush2)
		palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
		palette3.setBrush(QPalette.Active, QPalette.Base, brush12)
		palette3.setBrush(QPalette.Active, QPalette.Window, brush12)
		brush16 = QBrush(QColor(255, 255, 255, 128))
		brush16.setStyle(Qt.NoBrush)
		#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
		#endif
		palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
		palette3.setBrush(QPalette.Inactive, QPalette.Button, brush12)
		palette3.setBrush(QPalette.Inactive, QPalette.Text, brush2)
		palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
		palette3.setBrush(QPalette.Inactive, QPalette.Base, brush12)
		palette3.setBrush(QPalette.Inactive, QPalette.Window, brush12)
		brush17 = QBrush(QColor(255, 255, 255, 128))
		brush17.setStyle(Qt.NoBrush)
		#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
		#endif
		palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
		palette3.setBrush(QPalette.Disabled, QPalette.Button, brush12)
		palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
		palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
		palette3.setBrush(QPalette.Disabled, QPalette.Base, brush12)
		palette3.setBrush(QPalette.Disabled, QPalette.Window, brush12)
		brush18 = QBrush(QColor(255, 255, 255, 128))
		brush18.setStyle(Qt.NoBrush)
		#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
		#endif
		self.button_plus.setPalette(palette3)
		self.button_plus.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_minus = QPushButton(Calculator)
		self.button_minus.setObjectName(u"button_minus")
		self.button_minus.setGeometry(QRect(230, 150, 61, 51))
		self.button_minus.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_div = QPushButton(Calculator)
		self.button_div.setObjectName(u"button_div")
		self.button_div.setGeometry(QRect(230, 200, 61, 51))
		self.button_div.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_mul = QPushButton(Calculator)
		self.button_mul.setObjectName(u"button_mul")
		self.button_mul.setGeometry(QRect(230, 250, 61, 51))
		self.button_mul.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_equal = QPushButton(Calculator)
		self.button_equal.setObjectName(u"button_equal")
		self.button_equal.setGeometry(QRect(230, 300, 61, 51))
		self.button_equal.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_num6 = QPushButton(Calculator)
		self.button_num6.setObjectName(u"button_num6")
		self.button_num6.setGeometry(QRect(150, 190, 61, 81))
		self.button_num6.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_num5 = QPushButton(Calculator)
		self.button_num5.setObjectName(u"button_num5")
		self.button_num5.setGeometry(QRect(80, 190, 61, 81))
		self.button_num5.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_num4 = QPushButton(Calculator)
		self.button_num4.setObjectName(u"button_num4")
		self.button_num4.setGeometry(QRect(10, 190, 61, 81))
		self.button_num4.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_num1 = QPushButton(Calculator)
		self.button_num1.setObjectName(u"button_num1")
		self.button_num1.setGeometry(QRect(10, 280, 61, 81))
		self.button_num1.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_num2 = QPushButton(Calculator)
		self.button_num2.setObjectName(u"button_num2")
		self.button_num2.setGeometry(QRect(80, 280, 61, 81))
		self.button_num2.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_num3 = QPushButton(Calculator)
		self.button_num3.setObjectName(u"button_num3")
		self.button_num3.setGeometry(QRect(150, 280, 61, 81))
		self.button_num3.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.button_num0 = QPushButton(Calculator)
		self.button_num0.setObjectName(u"button_num0")
		self.button_num0.setGeometry(QRect(10, 370, 201, 31))
		self.button_num0.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")
		self.label_result = QLabel(Calculator)
		self.label_result.setObjectName(u"label_result")
		self.label_result.setGeometry(QRect(20, 20, 261, 51))
		self.label_result.setStyleSheet(u"font-size: 30px; font-weight: bold; color: white")
		self.label_result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
		self.button_clear = QPushButton(Calculator)
		self.button_clear.setObjectName(u"button_clear")
		self.button_clear.setGeometry(QRect(230, 350, 61, 51))
		self.button_clear.setStyleSheet(u"font-weight: bold;\n"
		"font-size: 30px;\n"
		"color: white;\n"
		"background-color: #616161;")

		self.retranslateUi(Calculator)
		self.button_num0.clicked.connect(lambda: self.label_result.setText("0") if self.label_result.text() == "0" else self.label_result.setText(self.label_result.text() + "0"))
		self.button_num1.clicked.connect(lambda: self.label_result.setText("1") if self.label_result.text() == "0" else self.label_result.setText(self.label_result.text() + "1"))
		self.button_num2.clicked.connect(lambda: self.label_result.setText("2") if self.label_result.text() == "0" else self.label_result.setText(self.label_result.text() + "2"))
		self.button_num3.clicked.connect(lambda: self.label_result.setText("3") if self.label_result.text() == "0" else self.label_result.setText(self.label_result.text() + "3"))
		self.button_num4.clicked.connect(lambda: self.label_result.setText("4") if self.label_result.text() == "0" else self.label_result.setText(self.label_result.text() + "4"))
		self.button_num5.clicked.connect(lambda: self.label_result.setText("5") if self.label_result.text() == "0" else self.label_result.setText(self.label_result.text() + "5"))
		self.button_num6.clicked.connect(lambda: self.label_result.setText("6") if self.label_result.text() == "0" else self.label_result.setText(self.label_result.text() + "6"))
		self.button_num7.clicked.connect(lambda: self.label_result.setText("7") if self.label_result.text() == "0" else self.label_result.setText(self.label_result.text() + "7"))
		self.button_num8.clicked.connect(lambda: self.label_result.setText("8") if self.label_result.text() == "0" else self.label_result.setText(self.label_result.text() + "8"))
		self.button_num9.clicked.connect(lambda: self.label_result.setText("9") if self.label_result.text() == "0" else self.label_result.setText(self.label_result.text() + "9"))

		self.button_mul.clicked.connect(lambda: self.label_result.setText(self.label_result.text() + " x ") if not (self.label_result.text().endswith(" x ") or self.label_result.text().endswith(" / ") or self.label_result.text().endswith(" + ") or self.label_result.text().endswith(" - ")) else None)
		self.button_div.clicked.connect(lambda: self.label_result.setText(self.label_result.text() + " / ") if not (self.label_result.text().endswith(" x ") or self.label_result.text().endswith(" / ") or self.label_result.text().endswith(" + ") or self.label_result.text().endswith(" - ")) else None)
		self.button_plus.clicked.connect(lambda: self.label_result.setText(self.label_result.text() + " + ") if not (self.label_result.text().endswith(" x ") or self.label_result.text().endswith(" / ") or self.label_result.text().endswith(" + ") or self.label_result.text().endswith(" - ")) else None)
		self.button_minus.clicked.connect(lambda: self.label_result.setText(self.label_result.text() + " - ") if not (self.label_result.text().endswith(" x ") or self.label_result.text().endswith(" / ") or self.label_result.text().endswith(" + ") or self.label_result.text().endswith(" - ")) else None)

		self.button_clear.clicked.connect(lambda: self.label_result.setText("0"))

		self.button_equal.clicked.connect(self.__handle_expression)

		QMetaObject.connectSlotsByName(Calculator)
		# setupUi

	def retranslateUi(self, Calculator):
		Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"MerCalc", None))
		self.button_num9.setText(QCoreApplication.translate("Calculator", u"9", None))
		self.button_num8.setText(QCoreApplication.translate("Calculator", u"8", None))
		self.button_num7.setText(QCoreApplication.translate("Calculator", u"7", None))
		self.button_plus.setText(QCoreApplication.translate("Calculator", u"+", None))
		self.button_minus.setText(QCoreApplication.translate("Calculator", u"-", None))
		self.button_div.setText(QCoreApplication.translate("Calculator", u"/", None))
		self.button_mul.setText(QCoreApplication.translate("Calculator", u"X", None))
		self.button_equal.setText(QCoreApplication.translate("Calculator", u"=", None))
		self.button_num6.setText(QCoreApplication.translate("Calculator", u"6", None))
		self.button_num5.setText(QCoreApplication.translate("Calculator", u"5", None))
		self.button_num4.setText(QCoreApplication.translate("Calculator", u"4", None))
		self.button_num1.setText(QCoreApplication.translate("Calculator", u"1", None))
		self.button_num2.setText(QCoreApplication.translate("Calculator", u"2", None))
		self.button_num3.setText(QCoreApplication.translate("Calculator", u"3", None))
		self.button_num0.setText(QCoreApplication.translate("Calculator", u"0", None))
		self.label_result.setText(QCoreApplication.translate("Calculator", u"0", None))
		self.button_clear.setText(QCoreApplication.translate("Calculator", u"CE", None))

	def __handle_expression(self):
		expression = self.label_result.text()

		# Check if there are mathematical signs in the expression
		if re.search(r'[x/+\-]', self.label_result.text()):
			try:
				result = eval(expression.replace('x', '*'))
				self.label_result.setText(str(result))
			except Exception as e:
				# Handle any evaluation errors here
				self.label_result.setText("Error")
				print(e)
		else:
			# No signs in the expression, so no calculation is needed
			pass
		

class CalculatorWindow(QMainWindow, Ui_Calculator):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

def main():
	app = QApplication(sys.argv)
	window = CalculatorWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
