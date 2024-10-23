from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generateur():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [choice(letters) for _ in range(randint(8, 10)) ]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4)) ]

    password_number = [choice(numbers) for _ in range(randint(2, 4)) ]
    password_list = password_letter + password_symbols + password_number
    shuffle(password_list)

    password = "".join(password_list)


    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_and_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:

        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving update data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_website:
            data = json.load(data_website)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_imager = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_imager)
canvas.grid(column=1, row=0)
website = Label(text="Website:")
website.grid(column=0, row=1)
email_and_username = Label(text="Email/Username:")
email_and_username.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)
website_entry = Entry(width=17)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_and_username_entry = Entry(width=35)
email_and_username_entry.grid(row=2, column=1, columnspan=2)
email_and_username_entry.insert(0, "meher@gmail.com")
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)
G_password_button= Button(text="Generate Password", command=password_generateur)
G_password_button.grid(row=3, column=2)
Add_button = Button(text="Add", width=30, command=save)
Add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
