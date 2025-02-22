import cv2
import numpy as np
import pyautogui
import mss
import time
import requests
import psutil
from ultralytics import YOLO
import customtkinter as ctk
from PIL import Image, ImageTk
import threading

model = YOLO(r'C:\Users\famil\Downloads\yolo11n_cs2.pt')

keys_url = "https://raw.githubusercontent.com/BROKENISTXD/website/refs/heads/main/keys.txt"
try:
    response = requests.get(keys_url)
    response.raise_for_status()
    keys = response.text.strip().split("\n")
except Exception as e:
    keys = ["default_key"]

sct = mss.mss()
monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ExScript Aimbot")
        self.geometry("1200x800")
        self.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.logo = Image.open("logo.png")
        self.logo = self.logo.resize((200, 200), Image.Resampling.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = ctk.CTkLabel(self.main_frame, image=self.logo, text="")
        self.logo_label.pack(pady=10)

        self.title_label = ctk.CTkLabel(self.main_frame, text="ExScript Aimbot", font=("Arial", 36, "bold"))
        self.title_label.pack(pady=10)

        self.key_frame = ctk.CTkFrame(self.main_frame)
        self.key_frame.pack(pady=20)

        self.key_label = ctk.CTkLabel(self.key_frame, text="Enter Key:", font=("Arial", 18))
        self.key_label.pack(side="left", padx=10)

        self.key_entry = ctk.CTkEntry(self.key_frame, width=300, font=("Arial", 16))
        self.key_entry.pack(side="left", padx=10)

        self.key_button = ctk.CTkButton(self.key_frame, text="Validate", command=self.validate_key)
        self.key_button.pack(side="left", padx=10)

        self.mode_frame = ctk.CTkFrame(self.main_frame)
        self.mode_frame.pack(pady=20)

        self.mode_label = ctk.CTkLabel(self.mode_frame, text="Select Mode:", font=("Arial", 18))
        self.mode_label.pack(side="left", padx=10)

        self.mode_var = ctk.StringVar(value="aimbot")
        self.aimbot_radio = ctk.CTkRadioButton(self.mode_frame, text="Aimbot", variable=self.mode_var, value="aimbot")
        self.aimbot_radio.pack(side="left", padx=10)
        self.triggerbot_radio = ctk.CTkRadioButton(self.mode_frame, text="Triggerbot", variable=self.mode_var, value="triggerbot")
        self.triggerbot_radio.pack(side="left", padx=10)

        self.status_label = ctk.CTkLabel(self.main_frame, text="Status: Idle", font=("Arial", 16))
        self.status_label.pack(pady=10)

        self.loading_label = ctk.CTkLabel(self.main_frame, text="Loading...", font=("Arial", 24))
        self.loading_label.pack_forget()

        self.aimbot_running = False
        self.animation_thread = None

    def validate_key(self):
        entered_key = self.key_entry.get().strip()
        if entered_key in keys:
            self.status_label.configure(text="Status: Key Valid", text_color="green")
            self.show_loading_screen()
            self.start_aimbot()
        else:
            self.status_label.configure(text="Status: Invalid Key", text_color="red")

    def show_loading_screen(self):
        self.loading_label.pack(pady=20)
        self.update()
        time.sleep(2)
        self.loading_label.pack_forget()

    def start_aimbot(self):
        self.aimbot_running = True
        self.animation_thread = threading.Thread(target=self.run_aimbot, daemon=True)
        self.animation_thread.start()

    def run_aimbot(self):
        while self.aimbot_running:
            if not self.is_cs2_running():
                self.status_label.configure(text="Status: Waiting for CS2...", text_color="yellow")
                time.sleep(1)
                continue

            img = np.array(sct.grab(monitor))
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

            results = model(img)

            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                    cls = int(box.cls.item())

                    target_center = ((x1 + x2) // 2, (y1 + y2) // 2)

                    if self.mode_var.get() == "aimbot":
                        pyautogui.moveTo(target_center[0], target_center[1])
                        pyautogui.click()
                    else:
                        cursor_x, cursor_y = pyautogui.position()
                        if abs(cursor_x - target_center[0]) < 10 and abs(cursor_y - target_center[1]) < 10:
                            pyautogui.click()

            self.update()

    def is_cs2_running(self):
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == 'cs2.exe':
                return True
        return False

if __name__ == "__main__":
    app = App()
    app.mainloop()