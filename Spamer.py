import pyautogui as pg
import time
import pyperclip as ppc
import customtkinter as ctk
import tkinter as tk
import threading as th
from tkinter import messagebox




class app():
    def __init__(self, root):
        self.root = root
        self.fnt = ('Arial',7)
        self.fnt_label = ('Arial', 100)


        self.frame_left = ctk.CTkFrame(self.root, fg_color = '#2A2D2E')
        self.frame_left.pack(side = 'left', fill = tk.Y)

        self.frame_entry_bg = ctk.CTkFrame(self.frame_left, fg_color = '#585E60')
        self.frame_entry_bg.pack(side = 'top', pady = 10, padx = 10)

        self.label_ap = ctk.CTkLabel(self.frame_entry_bg, text = 'SPAMER')
        self.label_ap.pack(pady = 10, padx = 5)

        self.entry_text = ctk.CTkEntry(self.frame_entry_bg, justify = 'center')
        self.entry_text.configure(font = self.fnt)
        self.entry_text.insert(tk.END, 'Введи сюда текс спама')
        self.entry_text.pack(pady = 5, padx = 10)

        self.entry_reply = ctk.CTkEntry(self.frame_entry_bg, justify = 'center')
        self.entry_reply.configure(font = self.fnt)
        self.entry_reply.insert(tk.END, 'Кол-во повторений')
        self.entry_reply.pack(pady = 5, padx = 10)


        self.frame_label_info_bg = ctk.CTkFrame(self.frame_left, fg_color = '#585E60')
        self.frame_label_info_bg.pack(side = 'bottom', pady = 10, padx = 10)

        self.label_info = ctk.CTkLabel(self.frame_label_info_bg,
            text = 'После нажатия кнопки \n start у тебя будет \n 3 секунды чтобы \n перейти в телеграм \n или куда-то еще')
        self.label_info.pack(side = 'bottom', pady = 70, padx =10)


        self.frame_timer_bg = ctk.CTkFrame(self.root, fg_color = '#585E60')
        self.frame_timer_bg.pack(expand = True)

        self.frame_timer_main = ctk.CTkFrame(self.frame_timer_bg)
        self.frame_timer_main.pack(pady = 10, padx = 10)


        self.label_timer = ctk.CTkLabel(self.frame_timer_main, text = '')
        self.label_timer.configure(font = self.fnt_label)
        self.label_timer.pack(expand = True)

        self.btn_start = ctk.CTkButton(self.root, text = 'start', command = self.start)
        self.btn_start.pack(expand = True)

    def start(self):
        self.count = self.entry_reply.get()

        def main():
            try:
                self.count = int(self.count)
            except:
                try:
                    self.entry_reply.delete(0, 'end')
                except:
                    None

                self.entry_reply.insert(tk.END, 'Введи сюда число!')
                for i in range(4):
                    self.entry_reply.configure(fg_color = 'red')
                    time.sleep(0.01)
                    self.entry_reply.configure(fg_color = '#343638')
                    time.sleep(0.01)
                return False

            self.text_spam = self.entry_text.get()
            self.text_previous = ppc.paste()

            ppc.copy(self.text_spam)

            for i in range(3):
                self.label_timer.configure(text = str(3-i))
                time.sleep(1)

            for i in range(self.count):
                pg.hotkey('ctrl', 'v')
                pg.press('enter')
                self.label_timer.configure(text = str(i+1))


        th.Thread(target = main).start()


def main():
    #pg.FAILSAFE = False

    root = ctk.CTk()
    root.geometry('500x400')
    root.title('Spamer')
    root.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app(root)


    root.mainloop()

main()