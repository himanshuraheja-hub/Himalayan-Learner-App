import os
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from login import LoginScreen
from dashboard import DashboardScreen
from notes import NotesScreen
from course import CourseScreen
from assignment import AssignmentScreen
from quiz import QuizScreen
from profile import ProfileScreen 
from cheatsheet import CheatSheetScreen
from kivy.core.window import Window

Window.size = (360, 640)

class HimalayanLearnerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        sm = ScreenManager()
        
        # Sari screens register karna
        screens = [
            LoginScreen(name='login'),
            DashboardScreen(name='dashboard'),
            ProfileScreen(name='profile'),
            NotesScreen(name='notes'),
            CheatSheetScreen(name='cheatsheet'),
            CourseScreen(name='course'),
            AssignmentScreen(name='assignment'),
            QuizScreen(name='quiz')
        ]
        
        for screen in screens:
            sm.add_widget(screen)

        # --- AUTO-LOGIN CHECK ---
        if os.path.exists("user_session.txt"):
            with open("user_session.txt", "r") as f:
                email = f.read().strip()
                if email:
                    sm.current = 'dashboard' # Seedha Dashboard par bhejo
        
        return sm

if __name__ == '__main__':
    HimalayanLearnerApp().run()