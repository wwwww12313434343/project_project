from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QGroupBox, QMessageBox
import random
app = QApplication([])
main_win = QWidget()
main_win.resize(500, 500)
j = -1
def show_correct(arg):
    if arg == True:
        text1.show()
        btn.setText('Следующий вопрос')
        text.setText('Ответ')
        btn1.hide()
        btn2.hide()
        btn3.hide()
        btn4.hide()
    if arg == False:
        if btn.text() == 'Ответить':
            text2.show()
            btn.setText('Следующий вопрос')
            text.setText('Ответ')
            btn1.hide()
            btn2.hide()
            btn3.hide()
            btn4.hide()
        else:
            text1.hide()
            text2.hide()
            btn.setText('Ответить')
            text.setText('Вопрос')
            btn1.show()
            btn2.show()
            btn3.show()
            btn4.show()
def check_answer():
    if btn.text() == 'Ответить' and btn1.isChecked():
        show_correct(True)
    else:
        show_correct(False)
class Question():
    def __init__(self, quest, answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    def showquest(self):
        text.setText(self.quest)
        btn1.setText(self.answer)
        btn2.setText(self.wrong1)
        btn3.setText(self.wrong2)
        btn4.setText(self.wrong3)
def ask(q: Question):
    q.showquest()

box = QGroupBox("Варианты ответов")
main_win.setWindowTitle('Memory Card')
text1 = QLabel('Правильно')
text2 = QLabel('Неправильно')
text = QLabel('Какой национальности не существует?')
btn = QPushButton('Ответить')
btn1 = QRadioButton('Энцы')
btn2 = QRadioButton('Смурфы')
btn3 = QRadioButton('Чулымцы')
btn4 = QRadioButton('Алеуты')
v_LINE = QVBoxLayout()
h_line = QHBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()

v3_line = QVBoxLayout()
v4_line = QVBoxLayout()
h3_line = QHBoxLayout()

v3_line.addWidget(btn1)
v3_line.addWidget(btn2)
v4_line.addWidget(btn3)
v4_line.addWidget(text1, alignment = Qt.AlignCenter)
v4_line.addWidget(text2, alignment = Qt.AlignCenter)
v4_line.addWidget(btn4)

h3_line.addLayout(v3_line)
h3_line.addLayout(v4_line)
box.setLayout(h3_line)
h_line.addWidget(text, alignment = Qt.AlignCenter)

h2_line.addWidget(btn, alignment = Qt.AlignCenter)

v_LINE.addLayout(h_line)
v_LINE.addWidget(box)
v_LINE.addLayout(h2_line)

main_win.setLayout(v_LINE)
text1.hide()
text2.hide()
btn.clicked.connect(check_answer)
q = Question('Государственный язык Бразилии?', 'Португальский', 'Итальянский', 'Испанский', 'Бразильский')
ask(q)
main_win.show()
app.exec()