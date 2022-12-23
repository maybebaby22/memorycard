from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle, randint 

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский' ))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Белый', 'Синий', 'Красный'))
question_list.append(Question('Кто президент РФ?', 'В.В.Путин', 'Вася Пупкин', 'Санек из 3 подьезда','Абраам Линкольн'))
question_list.append(Question('Как будет луч по английски?', 'beam', 'line', 'luch', 'laser'))
question_list.append(Question('Сколько миллионов мощи считаются приемлемыми?','5','3','2','10'))
question_list.append(Question('Из какого фильма Прекрасный принц?','Золушка','Русалочка','Спящая красавица','Мулан'))
question_list.append(Question('Из какой страны родом Джастин Бибер?','Канада','США','Россия','Чили'))
question_list.append(Question('В сиквеле какого праздничного фильма снялся Дональд Трамп?','Один дома 2: Затерянный в Нью-Йорке','Один дома','Ричи Рич','Маленькие негодяи'))
question_list.append(Question('Какой герой мультфильма живет в ананасе под водой?','Губка Боб Квадратные Штаны','Рик и Морти','Немо','Сквидвард'))
question_list.append(Question('Что является национальным животным Шотландии?','Единорог','Лошадь','Волк','Корова'))
question_list.append(Question('В каком известном романе фигурировали Джо, Мег, Бет и Эми Марч?','Маленькие женщины','Маленькие женщины','Том Сойер','Убить пересмешника'))
question_list.append(Question('Когда было крещение Руси?', '988', '938', '980', '679'))
question_list.append(Question('Сколько грамм семечек съест Дюймовочка за год', '6', '5', '4', '2'))
question_list.append(Question('Какой рост Майкла Джексона?', '175см', '165см', '180см', '168см'))
question_list.append(Question('Кто аписал Бородина?', 'Лермонтов', 'Пушкин', 'Песков', 'Ахматова'))
question_list.append(Question('Когда была война с Наполеоном?', '1812', '1342', '1879', '1814'))
question_list.append(Question('Когда сняли первый фильм про человека паука?', '1977', '1877', '1677', '1986'))
question_list.append(Question('Где самое сухое место на Земле?', 'Атакама', 'Антарктида', 'Евразия', 'Австралия'))
question_list.append(Question('Сколько надо лет, чтобы посмотеть все видео на YouTube?', '18678', '1000', '157', '10054'))
question_list.append(Question('Самый сильный мускул у человека?', 'язык', 'пальцу', 'нога', 'ухо'))
question_list.append(Question('Сколько будет 2+2?', '4', '5', '6', '7'))
question_list.append(Question('Сколько будет 7*8?', '56', '64', '75', '34'))
question_list.append(Question('Каких животных не было в Ирландии?', 'кроты', 'коровы', 'коты', 'слизни'))

app = QApplication([])
 
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!') 
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    cur_question = randint(0, len(question_list)-1)
    q = question_list [cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')#название

btn_OK.clicked.connect(click_ok)
window.show()
app.exec()