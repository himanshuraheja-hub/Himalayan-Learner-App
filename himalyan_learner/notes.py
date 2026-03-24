from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import webbrowser
import os

# notes.py ke andar

Builder.load_string('''
<NotesScreen>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1
        
        MDTopAppBar:
            title: "Study Notes"
            left_action_items: [["arrow-left", lambda x: root.back()]]
        
        ScrollView:
            MDList:
                # Purana Note 1
                OneLineIconListItem:
                    text: "Python Basics Notes"
                    on_release: root.open_note("Python_Notes.pdf")
                    IconLeftWidget:
                        icon: "language-python"

                # Purana Note 2
                OneLineIconListItem:
                    text: "Data Analysis Guide"
                    on_release: root.open_note("Data_Analyst.pdf")
                    IconLeftWidget:
                        icon: "chart-bar"

                # --- add new NOTE YAHAN ADD KAREIN ---
                OneLineIconListItem:
                    text: "C++ Programming Notes" # Jo screen par dikhega
                    on_release: root.open_note("Cpp_Notes.pdf") # Aapki PDF file ka naam
                    IconLeftWidget:
                        icon: "language-cpp" # Icon ka naam
''')

class NotesScreen(MDScreen):
    def back(self):
        self.manager.current = 'dashboard'
    def open_note(self, filename):
        path = f"C:/Users/Himan/Downloads/{filename}"
        if os.path.exists(path):
            webbrowser.open(path)