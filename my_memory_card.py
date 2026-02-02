#создай приложение для запоминания информации
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from memory_card_ui import Memory_card_ui
from random import shuffle
from questions import Questions
class MemoryCard(QMainWindow,Memory_card_ui):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.groupBox_answer.hide()


        self.currect_question_right = None
        self.correct, self.wrong = 0, 0

        self.questions = Questions()
        self.questions.add_question('Сколько будет 2*2', '4', '7', '9', '2')
        self.questions.add_question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский')
        self.questions.add_question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий')
        self.questions.add_question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата')
        self.questions.shuffle_question()

        self.test_question = ('Сколько будет 2 + 2', '4', '8', '12', '22')

        self.buttons = [self.radioButton1,
                self.radioButton2,
                self.radioButton3,
                self.radioButton4
                ]


        self.ask()
        self.connect()


    def connect(self):
        self.pushButton.clicked.connect(self.groupBox_switch)
    
    def error(self, error_text):
        error = QMessageBox()
        error.setWindowTitle('Ошибка')
        error.setText(error_text)
        error.exec_()

    def groupBox_switch(self):
        if self.groupBox.isVisible():
                if not any([btn.isChecked() for btn in self.buttons]):
                    self.error('Выберете ответ')
                    return
                self.check_answer()
                self.groupBox.hide()
                self.groupBox_answer.show()
                self.pushButton.setText('Следуюющий вопрос')
        else:

            for button in self.buttons:
                button.setAutoExclusive(False)
                button.setChecked(False)
                button.setAutoExclusive(True)

            
            self.ask()
            self.groupBox.show()
            self.groupBox_answer.hide()
            self.pushButton.setText('Ответить')
        
    def ask(self):
        question, right_answer, random_answer = self.questions.next_question_random()
        self.currect_question_right = right_answer

        self.label_question.setText(question)

        for index, btn in enumerate(self.buttons):
            btn.setText(random_answer[index])

    def check_answer(self):
        right_btn = max(self.buttons, key=lambda btn: btn.isChecked())
        if right_btn.text() == self.currect_question_right:
            self.labelAnswerResult.setText('Правильно!')
            self.correct += 1
            self.labelAnswerCorrect.setText(f'Все верно правильный ответ {self.currect_question_right}')
        else:
            self.wrong += 1
            self.labelAnswerResult.setText('Не правильно!')
            self.labelAnswerCorrect.setText(f'Правильный ответ {self.currect_question_right}')
        self.update_statistics()

    def update_statistics(self):
        self.label_statistics.setText(f'Правильных ответов: {self.correct}\nНе правильных ответов: {self.wrong}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MemoryCard()
    window.show()
    sys.exit(app.exec_())
    