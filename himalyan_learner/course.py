from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import webbrowser

Builder.load_string('''
<CourseScreen>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.95, 0.95, 0.95, 1
        
        MDTopAppBar:
            title: "My Courses"
            left_action_items: [["arrow-left", lambda x: root.back()]]
            elevation: 4

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "15dp"
                spacing: "20dp"
                adaptive_height: True

                # COURSE 1: Python
                MDCard:
                    orientation: "vertical"
                    size_hint: 1, None
                    height: "280dp"
                    radius: [15,]
                    padding: "10dp"
                    elevation: 2
                    
                    FitImage:
                        source: "C:/Users/Himan/Downloads/python_thumb.png" # Path check karein
                        radius: [15, 15, 0, 0]
                        size_hint_y: .6

                    MDBoxLayout:
                        orientation: "vertical"
                        padding: "10dp"
                        MDLabel:
                            text: "Python for Beginners"
                            font_style: "H6"
                            bold: True
                        MDLabel:
                            text: "Learn from zero to hero"
                            theme_text_color: "Secondary"
                            font_style: "Subtitle2"
                        
                        MDRaisedButton:
                            text: "WATCH NOW"
                            icon: "play"
                            pos_hint: {"right": 1}
                            on_release: root.open_course("https://youtube.com/link_to_python_playlist")

                # COURSE 2: Data Analysis
                MDCard:
                    orientation: "vertical"
                    size_hint: 1, None
                    height: "280dp"
                    radius: [15,]
                    padding: "10dp"
                    elevation: 2
                    
                    FitImage:
                        source: "C:/Users/Himan/Downloads/data_thumb.png"
                        radius: [15, 15, 0, 0]
                        size_hint_y: .6

                    MDBoxLayout:
                        orientation: "vertical"
                        padding: "10dp"
                        MDLabel:
                            text: "Data Analysis Masterclass"
                            font_style: "H6"
                            bold: True
                        MDLabel:
                            text: "Pandas, Numpy & Matplotlib"
                            theme_text_color: "Secondary"
                            font_style: "Subtitle2"
                        
                        MDRaisedButton:
                            text: "WATCH NOW"
                            icon: "play"
                            pos_hint: {"right": 1}
                            on_release: root.open_course("https://youtube.com/link_to_data_playlist")

                MDWidget:
                    size_hint_y: None
                    height: "20dp"
''')

class CourseScreen(MDScreen):
    def back(self):
        self.manager.current = 'dashboard'
    
    def open_course(self, url):
        # Yeh link ko browser mein khol dega
        webbrowser.open(url)