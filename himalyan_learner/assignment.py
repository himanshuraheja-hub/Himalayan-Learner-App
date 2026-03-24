from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from database import get_connection
import os
import shutil

Builder.load_string('''
<AssignmentScreen>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.95, 0.95, 0.95, 1

        MDTopAppBar:
            title: "My Assignments"
            left_action_items: [["arrow-left", lambda x: root.back()]]
            elevation: 4

        MDBoxLayout:
            orientation: "vertical"
            padding: "20dp"
            spacing: "15dp"

            # --- UPLOAD SECTION ---
            MDCard:
                orientation: "vertical"
                size_hint: 1, None
                height: "180dp"
                padding: "15dp"
                radius: [15, ]
                elevation: 1

                MDLabel:
                    text: "Submit New Assignment"
                    font_style: "H6"
                    theme_text_color: "Primary"

                MDTextField:
                    id: assignment_title
                    hint_text: "Assignment Title (e.g. Python Lab 1)"
                    mode: "line"

                MDRaisedButton:
                    text: "SELECT & UPLOAD FILE"
                    pos_hint: {"center_x": .5}
                    on_release: root.open_file_manager()

            # --- LIST SECTION ---
            MDLabel:
                text: "Pending/Submitted Tasks"
                bold: True
                font_style: "Subtitle1"
                size_hint_y: None
                height: "40dp"

            ScrollView:
                MDList:
                    id: assignment_list
                    # Yahan hum submitted assignments dikhayenge
''')

class AssignmentScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )

    def back(self):
        self.manager.current = 'dashboard'

    def open_file_manager(self):
        # Laptop/PC ka home folder open karega
        self.file_manager.show(os.path.expanduser("~"))

    def select_path(self, path):
        self.exit_manager()
        self.upload_to_db(path)

    def exit_manager(self, *args):
        self.file_manager.close()

    def upload_to_db(self, file_path):
        title = self.ids.assignment_title.text.strip()
        
        if not title:
            MDDialog(title="Error", text="Pehle assignment ka naam likhein!").open()
            return

        try:
            # 1. Folder check/create
            dest_dir = "uploads/assignments"
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            dest_path = os.path.join(dest_dir, os.path.basename(file_path))
            shutil.copy(file_path, dest_path)

            # 2. Database entry
            conn = get_connection()
            if conn:
                cursor = conn.cursor()
                query = "INSERT INTO assignments (title, file_path) VALUES (%s, %s)"
                cursor.execute(query, (title, dest_path))
                conn.commit()
                conn.close()
                
                self.ids.assignment_title.text = ""
                MDDialog(title="Success", text="Assignment jama ho gaya hai!").open()
        
        except Exception as e:
            MDDialog(title="Upload Failed", text=f"Error: {str(e)}").open()