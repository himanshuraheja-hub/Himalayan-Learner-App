from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from database import get_connection
from kivymd.uix.dialog import MDDialog
import os

Builder.load_string('''
<LoginScreen>:
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        
        Image:
            source: "C:/Users/Himan/Downloads/Firefly.png"
            size_hint: None, None
            size: "180dp", "180dp"
            pos_hint: {"center_x": .5, "center_y": .75}

        MDLabel:
            text: "Himalayan Learner"
            pos_hint: {"center_x": .5, "center_y": .58}
            halign: "center"
            font_style: "H4"
            bold: True

        MDTextField:
            id: user
            hint_text: "Choose Username"
            icon_left: "account"
            pos_hint: {"center_x": .5, "center_y": .45}
            size_hint_x: .8

        MDTextField:
            id: email
            hint_text: "Enter Email"
            icon_left: "email"
            pos_hint: {"center_x": .5, "center_y": .35}
            size_hint_x: .8

        MDTextField:
            id: password
            hint_text: "Set Password"
            icon_left: "key"
            pos_hint: {"center_x": .5, "center_y": .25}
            size_hint_x: .8
            password: True

        MDRaisedButton:
            text: "SUBMIT & START"
            pos_hint: {"center_x": .5, "center_y": .12}
            size_hint_x: 0.8
            on_release: root.do_register_and_login()
''')

class LoginScreen(MDScreen):
    def do_register_and_login(self):
        username = self.ids.user.text.strip()
        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()

        # Check agar fields khali na hon
        if username and email and password:
            try:
                conn = get_connection()
                if conn:
                    cursor = conn.cursor()
                    
                    # 1. Database mein data INSERT karna (No restrictions)
                    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
                    cursor.execute(query, (username, email, password))
                    conn.commit()
                    
                    # 2. Local Session save karna
                    with open("user_session.txt", "w") as f:
                        f.write(email)
                    
                    # 3. Dashboard ka welcome message update karna
                    self.manager.get_screen('dashboard').ids.welcome_text.text = f"Welcome, {username}!"
                    
                    # 4. Success Dialog
                    MDDialog(title="Success", text=f"Account created for {username}!").open()
                    
                    # 5. Dashboard par bhejna
                    self.manager.current = 'dashboard'
                    
                    cursor.close()
                    conn.close()
            except Exception as e:
                # Agar email pehle se exist karta hai ya koi error hai
                MDDialog(title="Database Error", text=str(e)).open()
        else:
            MDDialog(title="Input Error", text="Please fill all the boxes!").open()