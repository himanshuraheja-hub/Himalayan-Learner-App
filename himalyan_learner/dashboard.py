import os
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from database import get_connection

# Assuming your logo is saved as "assets/logo.png" or similar path
# Update the source path below to your actual logo file path.

Builder.load_string('''
<DashboardScreen>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.95, 0.96, 0.98, 1

        MDTopAppBar:
            title: "Himalayan Learner"
            right_action_items: [["logout-variant", lambda x: root.logout()]]
            elevation: 2
            # Optional: Add logo icon here too, in the top bar
            # left_action_items: [["image", lambda x: None]] 

        ScrollView:
            do_scroll_x: False
            MDBoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "25dp"  
                adaptive_height: True

                # --- BRANDING & WELCOME SECTION ---
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: "10dp"
                    padding: [0, "15dp", 0, "15dp"] # More top padding for logo

                    # --- LOGO ---
                    Image:
                        source: "C:/Users/Himan/Downloads/Firefly.png" # <--- YOUR LOGO PATH HERE
                        size_hint: None, None
                        size: "120dp", "120dp" # Adjusted size for good balance
                        pos_hint: {"center_x": .5}
                        # allow_stretch: True # optional, if logo is small

                    MDLabel:
                        id: welcome_text
                        text: "Welcome, Himanshu!"
                        font_style: "H5"
                        bold: True
                        halign: "center" # Center the name below logo
                        theme_text_color: "Primary"
                        adaptive_height: True

                    MDLabel:
                        text: "Ready to continue your learning journey?"
                        font_style: "Caption"
                        halign: "center" # Center the subtitle too
                        theme_text_color: "Secondary"
                        adaptive_height: True

                # --- MODERN GRID LAYOUT ---
                MDGridLayout:
                    cols: 2
                    spacing: "15dp"
                    adaptive_height: True
                    padding: [0, 0, 0, "20dp"]

                    NavCard:
                        icon: "account-circle"
                        text: "PROFILE"
                        on_release: root.manager.current = 'profile'

                    NavCard:
                        icon: "file-document-edit"
                        text: "QUIZ"
                        on_release: root.manager.current = 'quiz'

                    NavCard:
                        icon: "book-open-page-variant"
                        text: "NOTES"
                        on_release: root.manager.current = 'notes'

                    NavCard:
                        icon: "code-tags"
                        text: "CHEATS"
                        on_release: root.manager.current = 'cheatsheet'

                    NavCard:
                        icon: "clipboard-text"
                        text: "TASKS"
                        on_release: root.manager.current = 'assignment'

                    NavCard:
                        icon: "play-circle-outline"
                        text: "COURSES"
                        on_release: root.manager.current = 'course'

<NavCard@MDCard>:
    icon: ""
    text: ""
    orientation: "vertical"
    padding: "15dp"
    radius: [20, ]
    elevation: 1
    ripple_behavior: True
    size_hint_y: None
    height: "140dp" 
    md_bg_color: 1, 1, 1, 1

    MDIcon:
        icon: root.icon
        halign: "center"
        font_size: "45sp"
        theme_text_color: "Custom"
        text_color: 0.12, 0.58, 0.95, 1
        pos_hint: {"center_x": .5}

    MDLabel:
        text: root.text
        halign: "center"
        font_style: "Button"
        theme_text_color: "Primary"
        bold: True
''')

class DashboardScreen(MDScreen):
    def on_pre_enter(self):
        self.load_user_info()

    def load_user_info(self):
        if os.path.exists("user_session.txt"):
            with open("user_session.txt", "r") as f:
                email = f.read().strip()
            try:
                conn = get_connection()
                if conn:
                    cursor = conn.cursor(dictionary=True)
                    query = "SELECT username FROM users WHERE email = %s"
                    cursor.execute(query, (email,))
                    user = cursor.fetchone()
                    if user:
                        # self.ids.welcome_text.text = f"Welcome, {user['username']}!" # Original full message
                        self.ids.welcome_text.text = user['username'] # Dynamic only name below logo
                    conn.close()
            except Exception as e:
                print(f"Error: {e}")

    def logout(self):
        if os.path.exists("user_session.txt"):
            os.remove("user_session.txt")
        self.manager.current = 'login'
        