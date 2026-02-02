from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class Memory_card_ui():
    def setup_ui(self, main_window):
        self.central_widget = QWidget()
        main_window.setCentralWidget(self.central_widget)
        main_window.resize(300 , 300)
        main_window.setWindowTitle('Memory card')

        self.label_question = QLabel('Какой национальности не существует?')
        self.pushButton = QPushButton('Ответить')

        self.groupBox = QGroupBox('Варианты ответов:')
        self.radioButton1 = QRadioButton('Энцы')
        self.radioButton2 = QRadioButton('Чулымцы')
        self.radioButton3 = QRadioButton('Смурфы')
        self.radioButton4 = QRadioButton('Алеуты')

        self.verticalLayoutMain = QVBoxLayout()
        self.horizontalloyautGroupBox = QHBoxLayout()
        self.verticalLayout1 = QVBoxLayout()
        self.verticalLayout2 = QVBoxLayout()
        self.horizontalloyautLine1 = QHBoxLayout()
        self.horizontalloyautLine2 = QHBoxLayout()
        self.horizontalloyautLine3 = QHBoxLayout()

        self.label_statistics = QLabel('Статистика')

        self.verticalLayoutMain.addWidget(self.label_statistics, alignment=Qt.AlignRight)
        self.verticalLayoutMain.addLayout(self.horizontalloyautLine1,stretch=2)
        self.verticalLayoutMain.addLayout(self.horizontalloyautLine2,stretch=8)
        self.verticalLayoutMain.addStretch(1)
        self.verticalLayoutMain.addLayout(self.horizontalloyautLine3,stretch=1)
        self.verticalLayoutMain.addStretch(1)
        self.verticalLayoutMain.addSpacing(5)

        self.horizontalloyautGroupBox.addLayout(self.verticalLayout1)
        self.horizontalloyautGroupBox.addLayout(self.verticalLayout2)

        self.verticalLayout1.addWidget(self.radioButton1)
        self.verticalLayout1.addWidget(self.radioButton2)
        self.verticalLayout2.addWidget(self.radioButton3)
        self.verticalLayout2.addWidget(self.radioButton4)

        self.groupBox_answer = QGroupBox('Результат теста')
        self.verticalLayoutGroupAnswer = QVBoxLayout()
        self.labelAnswerResult = QLabel('Прав или нет')
        self.labelAnswerCorrect = QLabel('Правильный ответ')
        self.verticalLayoutGroupAnswer.addWidget(self.labelAnswerResult, alignment=(Qt.AlignLeft | Qt.AlignTop))
        self.verticalLayoutGroupAnswer.addWidget(self.labelAnswerCorrect, alignment=Qt.AlignCenter, stretch=2)
        self.groupBox_answer.setLayout(self.verticalLayoutGroupAnswer)

        

        self.horizontalloyautLine1.addWidget(self.label_question, alignment=Qt.AlignCenter)

        self.horizontalloyautLine2.addWidget(self.groupBox)
        self.horizontalloyautLine2.addWidget(self.groupBox_answer)
        
        self.horizontalloyautLine3.addStretch(1)
        self.horizontalloyautLine3.addWidget(self.pushButton, stretch=2)
        self.horizontalloyautLine3.addStretch(1)

        self.groupBox.setLayout(self.horizontalloyautGroupBox)
        self.central_widget.setLayout(self.verticalLayoutMain)