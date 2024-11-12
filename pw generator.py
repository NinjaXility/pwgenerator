import customtkinter as ctk
import random
import string
from tkinter import filedialog

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class PasswordGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator made by H3lios")
        self.geometry("400x300")

        self.password_display = ctk.CTkEntry(self, width=300, font=("Arial", 14))
        self.password_display.grid(row=0, column=0, columnspan=3, pady=(20, 10))

        self.include_numbers = ctk.BooleanVar()
        self.include_letters = ctk.BooleanVar()
        self.include_special_chars = ctk.BooleanVar()

        self.number_checkbox = ctk.CTkCheckBox(self, text="Numbers", variable=self.include_numbers)
        self.letter_checkbox = ctk.CTkCheckBox(self, text="Letters", variable=self.include_letters)
        self.special_chars_checkbox = ctk.CTkCheckBox(self, text="Special Characters", variable=self.include_special_chars)

        self.number_checkbox.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.letter_checkbox.grid(row=2, column=0, padx=10, pady=0, sticky="w")
        self.special_chars_checkbox.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="w")

        self.length_label = ctk.CTkLabel(self, text="Password Length:")
        self.length_label.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")

        self.length_slider = ctk.CTkSlider(self, from_=4, to=32, orientation="horizontal", command=self.update_length_label)
        self.length_slider.set(12)
        self.length_slider.grid(row=4, column=1, columnspan=2, padx=(0, 10), pady=(10, 0))

        self.length_value_label = ctk.CTkLabel(self, text="12")
        self.length_value_label.grid(row=4, column=2, padx=10, pady=(10, 0))

        self.generate_button = ctk.CTkButton(self, text="Generate", command=self.generate_password)
        self.generate_button.grid(row=5, column=1, pady=(20, 10))

        self.export_button = ctk.CTkButton(self, text="Export as .txt", command=self.export_password, width=100)
        self.export_button.grid(row=6, column=0, pady=(10, 10), padx=(10, 0), sticky="w")

    def update_length_label(self, value):
        self.length_value_label.configure(text=str(int(value)))

    def generate_password(self):
        length = int(self.length_slider.get())
        password_characters = ""

        if self.include_numbers.get():
            password_characters += string.digits
        if self.include_letters.get():
            password_characters += string.ascii_letters
        if self.include_special_chars.get():
            password_characters += string.punctuation

        if not password_characters:
            self.password_display.delete(0, ctk.END)
            self.password_display.insert(0, "Select at least one option")
            return

        password = ''.join(random.choice(password_characters) for _ in range(length))
        self.password_display.delete(0, ctk.END)
        self.password_display.insert(0, password)

    def export_password(self):
        password = self.password_display.get()
        if password:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(password)

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()