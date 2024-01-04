import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tqdm import tqdm
import time

class FileProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Easy DocX Translator")
        self.root.geometry("500x300")
        self.root.configure(bg="black")

        # Окно выбора файлов
        self.file_label = tk.Label(self.root, text="Выберите файлы:", bg="black", fg="white")
        self.file_label.pack(pady=10)
        self.file_button = tk.Button(self.root, text="Выбрать файлы", command=self.select_files, bg="white", fg="black")
        self.file_button.pack(pady=5)

        # Окно сохранения файлов
        self.save_label = tk.Label(self.root, text="Выберите место сохранения:", bg="black", fg="white")
        self.save_label.pack(pady=10)
        self.save_button = tk.Button(self.root, text="Выбрать папку", command=self.select_save_location, bg="white", fg="black")
        self.save_button.pack(pady=5)

        # Кнопка "Start"
        self.start_button = tk.Button(self.root, text="Start", command=self.start_processing, bg="green", fg="white")
        self.start_button.pack(pady=10)

        # Окно прогресса
        self.progress_label = tk.Label(self.root, text="Прогресс:", bg="black", fg="white")
        self.progress_label.pack(pady=5)
        self.progress_bar = ttk.Progressbar(self.root, length=300, mode="determinate")
        self.progress_bar.pack(pady=5)

    def select_files(self):
        file_paths = filedialog.askopenfilenames(title="Выберите файлы", filetypes=[("Text files", "*.docx"), ("All files", "*.*")])
        print("Выбранные файлы:", file_paths)

    def select_save_location(self):
        save_path = filedialog.askdirectory(title="Выберите место сохранения")
        print("Выбранное место сохранения:", save_path)

    def start_processing(self):
        # tqdm для отображения прогресса
        files = range(10)
        for file in tqdm(files, desc="Processing files", unit="file"):
            
            time.sleep(0.5)  

            
            self.progress_bar["value"] += 10
            self.root.update_idletasks()
