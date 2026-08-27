import customtkinter as ctk

from database import initialize_database


class PasswordManagerApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Password Manager")
        self.geometry("900x600")

        self.title_label = ctk.CTkLabel(
            self,
            text="🔐 Password Manager",
            font=("Arial", 28, "bold")
        )

        self.title_label.pack(pady=30)

        self.search_entry = ctk.CTkEntry(
            self,
            placeholder_text="Search passwords..."
        )

        self.search_entry.pack(
            padx=40,
            pady=10,
            fill="x"
        )

        self.add_button = ctk.CTkButton(
            self,
            text="+ Add Password",
            command=self.add_password
        )

        self.add_button.pack(pady=20)

    def add_password(self):
        print("Add password clicked")


if __name__ == "__main__":
    initialize_database()

    app = PasswordManagerApp()
    app.mainloop()