import customtkinter as ctk 
import sqlite3 

conexao = sqlite3.connect("hospital.db")
cursor = conexao.cursor()

cursor.execute("""
            create table if not exists users (
                id integer primary key autoincrement,
                name varchar(30) not null,
                password varchar(10) not null,
                balance integer not null
               
               );
               
               
               
               """)


# User: user1 Password: 123

class Rootbank:
    def __init__(self,balance):
        self.balance = balance

        self.root = ctk.CTk()
        self.root.title("Bank")
        self.root.geometry("500x500")

        self.label = ctk.CTkLabel(self.root,text=f"Balance: {self.balance}")
        self.label.pack(pady=5)

        # Formular botões de Depósito e Saque. Após a elaboração do sistema, estudos para realizar uma interface digna.
    
    def open(self):
        self.root.mainloop()


def search():
    name_out = entry_name.get()
    pass_out = entry_pass.get()
    cursor.execute("Select * from users where name = ? and password = ?",(name_out,pass_out,))
    user = cursor.fetchone()
    if user:
        root.withdraw()
        new_root = Rootbank(user[3])
        new_root.open()
    else:
        secret_label.configure(text="Not found!")


root = ctk.CTk()
root.title("Login")
root.geometry("500x500")
root.resizable(False,False)

label_name = ctk.CTkLabel(root,text="Name: ")
label_name.pack(pady=5)

entry_name = ctk.CTkEntry(root,placeholder_text="...")
entry_name.pack(pady=5)

label_pass = ctk.CTkLabel(root,text="Password")
label_pass.pack(pady=5)

entry_pass = ctk.CTkEntry(root,placeholder_text="...",show="*")
entry_pass.pack(pady=5)

button = ctk.CTkButton(root,text="Login",command=search)
button.pack(pady=5)

secret_label = ctk.CTkLabel(root,text="")
secret_label.pack(pady=5)

root.mainloop()