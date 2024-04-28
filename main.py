from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = ('Modern', 15, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(8, 10)]
    password_list += [random.choice(symbols) for _ in range(2, 4)]
    password_list += [random.choice(numbers) for _ in range(2, 4)]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        data = {}  # data to fill
        try:
            with open("data.json", "r") as data_file:  # fill with data from file
                # read old data
                data = json.load(data_file)
                # update old data with new data
                data.update(new_data)
        except FileNotFoundError:
            print("No file existed before.")
            data = new_data  # fill only with new data

        # write data to file
        with open("data.json", "w") as data_file:
            # saving updated data
            json.dump(data, data_file, indent=4)

            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# --------------------------- FIND PASSWORD ------------------------------ #

def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No file found", message="No data file found")
    else:
        if website_input.get() in data:
            print("It is there")
        else:
            messagebox.showinfo(title="Missing details", message="No details for the website found")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="Black")

canvas = Canvas(width=200, height=200, bg="Black", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website", font=FONT_NAME, bg="Black", fg="White")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=FONT_NAME, bg="Black", fg="White")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=FONT_NAME, bg="Black", fg="White")
password_label.grid(column=0, row=3)

# Inputs
website_input = Entry(width=21, highlightthickness=0, bg="#d3d3d3")
website_input.grid(column=1, row=1,)
website_input.focus()

username_input = Entry(width=36, highlightthickness=0, bg="#d3d3d3")
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(END, "astridskillingstad@gmail.com")

password_input = Entry(width=21, highlightthickness=0, bg="#d3d3d3")
password_input.grid(column=1, row=3)

# Buttons
border = LabelFrame(window, bd=4, bg="gray")
border.grid(column=2, row=1, pady=1)
search_button = Button(border, text="Search", width=13, highlightthickness=0, bg="#d3d3d3", command=find_password)
search_button.grid(column=2, row=1)

border2 = LabelFrame(window, bd=4, bg="gray")
border2.grid(column=2, row=3, pady=1)
generate_button = Button(border2, text="Generate Password", bg="#d3d3d3", highlightthickness=0,
                         command=generate_password)
generate_button.grid(column=2, row=3)

border3 = LabelFrame(window, bd=4, bg="gray")
border3.grid(column=1, row=4, columnspan=2, pady=1)
add_button = Button(border3, text="Add", width=36, bg="#d3d3d3", highlightthickness=0, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
