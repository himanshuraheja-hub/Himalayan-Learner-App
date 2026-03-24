from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import webbrowser

Builder.load_string('''
<CheatSheetScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Quick Cheat Sheets"
            left_action_items: [["arrow-left", lambda x: root.back()]]
        
        ScrollView:
            MDList:
                TwoLineIconListItem:
                    text: "Python Syntax Cheat Sheet"
                    secondary_text: "Quick Syntax Guide"
                    on_release: root.open_sheet("https://quickref.me/python")
                    IconLeftWidget:
                        icon: "file-code"
                        
                TwoLineIconListItem:
                    text: "PHP Syntax Cheat Sheet"
                    secondary_text: "Quick Syntax Guide"
                    on_release: root.open_sheet("https://quickref.me/python")
                    IconLeftWidget:
                        icon: "file-code"
                
                TwoLineIconListItem:
                    text: "MySQL Commands"
                    secondary_text: "All SQL Queries"
                    on_release: root.open_sheet("file:///C:/Users/Himan/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/LocalState/sessions/08D33828631AF41C40E7633673066503FE0AE994/transfers/2026-11/MySQL%20Cheatsheet.pdf")
                    IconLeftWidget:
                        icon: "database"
''')

class CheatSheetScreen(MDScreen):
    def back(self):
        self.manager.current = 'dashboard'
    def open_sheet(self, url):
        webbrowser.open(url)