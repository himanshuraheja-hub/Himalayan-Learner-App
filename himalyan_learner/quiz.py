from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import NumericProperty, StringProperty

Builder.load_string('''
<QuizScreen>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1
        MDTopAppBar:
            title: "Quiz Score: " + str(root.score)
            left_action_items: [["arrow-left", lambda x: root.back()]]
        
        MDBoxLayout:
            orientation: "vertical"
            padding: "20dp"
            spacing: "15dp"

            MDLabel:
                text: "Question " + str(root.question_index + 1) + " of " + str(len(root.quiz_data[root.current_set]))
                halign: "right"
                font_style: "Caption"

            MDCard:
                size_hint: 1, None
                height: "150dp"
                padding: "15dp"
                md_bg_color: 0.9, 0.9, 1, 1
                MDLabel:
                    text: root.question_text
                    halign: "center"
                    bold: True

            MDRaisedButton:
                text: root.opt1
                size_hint_x: 1
                on_release: root.check_answer(self.text)
            MDRaisedButton:
                text: root.opt2
                size_hint_x: 1
                on_release: root.check_answer(self.text)
            MDRaisedButton:
                text: root.opt3
                size_hint_x: 1
                on_release: root.check_answer(self.text)
            MDWidget:
''')

class QuizScreen(MDScreen):
    score = NumericProperty(0)
    question_index = NumericProperty(0)
    current_set = NumericProperty(0)
    question_text = StringProperty("")
    opt1 = StringProperty(""); opt2 = StringProperty(""); opt3 = StringProperty("")
    correct_answer = StringProperty("")

    # 20 Questions Data
    quiz_data = [[
        # Easy
        {"q": "Python extension kya hai?", "a": ".py", "opts": [".py", ".python", ".pt"]},
        {"q": "List ko kaise represent karte hain?", "a": "[]", "opts": ["()", "[]", "{}"]},
        {"q": "Python kisne banayi?", "a": "Guido van Rossum", "opts": ["Dennis", "Guido", "James"]},
        {"q": "Output function?", "a": "print()", "opts": ["echo", "output", "print()"]},
        {"q": "Comment symbol?", "a": "#", "opts": ["//", "/*", "#"]},
        # Medium
        {"q": "List mutable hai?", "a": "Haan", "opts": ["Haan", "Nahi", "Dono"]},
        {"q": "Tuple symbol?", "a": "()", "opts": ["()", "[]", "{}"]},
        {"q": "Range(5) last no?", "a": "4", "opts": ["5", "4", "0"]},
        {"q": "Dict storage?", "a": "Key-Value", "opts": ["Index", "Key-Value", "Random"]},
        {"q": "String to Int?", "a": "int()", "opts": ["str", "int()", "float"]},
        {"q": "Function keyword?", "a": "def", "opts": ["func", "define", "def"]},
        {"q": "Stop loop?", "a": "break", "opts": ["stop", "break", "exit"]},
        {"q": "Add to list?", "a": "append()", "opts": ["add", "insert", "append()"]},
        {"q": "Duplicate in Set?", "a": "No", "opts": ["Yes", "No", "All Of This"]},
        {"q": "Slicing syntax?", "a": "[start:stop]", "opts": ["(s,e)", "[s:e]", "{s-e}"]},
        # Hard
        {"q": "Anonymous function?", "a": "Lambda", "opts": ["Def", "Lambda", "Inline"]},
        {"q": "Self refers to?", "a": "Object", "opts": ["Class", "Object", "Parent"]},
        {"q": "Memory management?", "a": "Garbage Collector", "opts": ["Compiler", "User", "Garbage Collector"]},
        {"q": "Decorator use?", "a": "Modify Func", "opts": ["Delete", "Modify Func", "Speed"]},
        {"q": "Is Python compiled?", "a": "Interpreted", "opts": ["Compiled", "Interpreted", "Both"]}
    ]]

    def on_pre_enter(self):
        self.score = 0; self.question_index = 0
        self.load_question()

    def load_question(self):
        if self.question_index < len(self.quiz_data[self.current_set]):
            data = self.quiz_data[self.current_set][self.question_index]
            self.question_text = data["q"]
            self.opt1, self.opt2, self.opt3 = data["opts"]
            self.correct_answer = data["a"]

    def check_answer(self, user_choice):
        msg = "Correct!" if user_choice == self.correct_answer else "Wrong!"
        if user_choice == self.correct_answer: self.score += 5 # 20 questions * 5 = 100
        self.dialog = MDDialog(title=msg, text=f"Answer: {self.correct_answer}",
                               buttons=[MDFlatButton(text="NEXT", on_release=self.next_question)])
        self.dialog.open()

    def next_question(self, *args):
        self.dialog.dismiss()
        if self.question_index < len(self.quiz_data[self.current_set]) - 1:
            self.question_index += 1
            self.load_question()
        else:
            MDDialog(title="Finish", text=f"Final Score: {self.score}", 
                     buttons=[MDFlatButton(text="HOME", on_release=self.go_home)]).open()

    def go_home(self, *args):
        self.manager.current = 'dashboard'

    def back(self):
        self.manager.current = 'dashboard'

