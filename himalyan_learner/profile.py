from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.camera import Camera
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from database import get_connection
import os

Builder.load_string('''
<ProfileScreen>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.95, 0.95, 0.95, 1
        
        MDTopAppBar:
            title: "My Profile"
            left_action_items: [["arrow-left", lambda x: root.back()]]
            elevation: 4

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "20dp"
                adaptive_height: True

                MDRelativeLayout:
                    size_hint: None, None
                    size: "180dp", "180dp"
                    pos_hint: {"center_x": .5}
                    
                    MDCard:
                        size_hint: None, None
                        size: "180dp", "180dp"
                        radius: [90, ]
                        elevation: 2
                        FitImage:
                            id: profile_pic
                            # Agar captured image nahi hai toh default dikhayega
                            source: "profile_update.png" if os.path.exists("profile_update.png") else "assets/default_user.png"
                            radius: [90, ]

                    MDIconButton:
                        icon: "camera"
                        pos_hint: {"center_x": .85, "center_y": .15}
                        md_bg_color: app.theme_cls.primary_color
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        on_release: root.show_camera_dialog()

                MDTextField:
                    id: edit_name
                    hint_text: "Full Name"
                    icon_left: "account"
                    mode: "rectangle"

                MDTextField:
                    id: edit_email
                    hint_text: "Email Address"
                    icon_left: "email"
                    mode: "rectangle"
                    readonly: True 

                MDFillRoundFlatButton:
                    text: "SAVE CHANGES"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": .5}
                    on_release: root.save_profile()
''')

class ProfileScreen(MDScreen):
    camera_dialog = None

    def on_pre_enter(self):
        """Page khulne se pehle session wala email read karega"""
        self.load_user_data()

    def load_user_data(self):
        # 1. Session file se email nikalein
        email = ""
        if os.path.exists("user_session.txt"):
            with open("user_session.txt", "r") as f:
                email = f.read().strip()

        if not email:
            return

        try:
            conn = get_connection()
            if conn:
                cursor = conn.cursor(dictionary=True)
                # LIMIT 1 ki jagah specific email use karein
                query = "SELECT username, email FROM users WHERE email = %s" 
                cursor.execute(query, (email,))
                user = cursor.fetchone()
                
                if user:
                    self.ids.edit_name.text = user['username']
                    self.ids.edit_email.text = user['email']
                
                conn.close()
        except Exception as e:
            print(f"Fetch Error: {e}")

    def show_camera_dialog(self):
        try:
            self.cam = Camera(resolution=(640, 480), play=True)
            self.camera_dialog = MDDialog(
                title="Click Photo",
                type="custom",
                content_cls=self.cam,
                size_hint=(0.9, 0.8),
                buttons=[
                    MDRaisedButton(text="CANCEL", on_release=self.close_dialog),
                    MDRaisedButton(text="CAPTURE", on_release=self.capture_photo),
                ],
            )
            self.camera_dialog.open()
        except Exception:
            MDDialog(title="Error", text="Camera module not working!").open()

    def capture_photo(self, *args):
        filename = "profile_update.png"
        self.cam.export_to_png(filename)
        self.ids.profile_pic.source = filename
        self.ids.profile_pic.reload()
        self.close_dialog()

    def save_profile(self):
        name = self.ids.edit_name.text
        email = self.ids.edit_email.text
        
        try:
            conn = get_connection()
            if conn:
                cursor = conn.cursor()
                query = "UPDATE users SET username = %s WHERE email = %s"
                cursor.execute(query, (name, email))
                conn.commit()
                conn.close()
                
                # Dashboard pe welcome text update karna
                self.manager.get_screen('dashboard').ids.welcome_text.text = f"Welcome, {name}!"
                MDDialog(title="Success", text="Profile Saved!").open()
        except Exception as e:
            MDDialog(title="Error", text=f"Update failed: {e}").open()

    def close_dialog(self, *args):
        if self.camera_dialog:
            self.cam.play = False
            self.camera_dialog.dismiss()

    def back(self):
        self.manager.current = 'dashboard'