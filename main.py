from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- RANDOM PASSWORD GENERATOR ------------------------------- #
def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
	           'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
	           'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	letters_list = [choice(letters) for _ in range(randint(8, 10))]
	symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
	numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

	password_list = letters_list + symbols_list + numbers_list
	shuffle(password_list)

	password = "".join(password_list)
	password_entry.delete(0, END)
	password_entry.insert(0, password)
	pyperclip.copy(password)  # copies password to the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	website = website_entry.get()
	email_username = email_username_entry.get()
	password = password_entry.get()

	if len(website) == 0 or len(password) == 0 or len(email_username) == 0:
		messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")

	else:
		is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
		                                                      f"\nEmail/Username: {email_username}"
		                                                      f"\n"f"Password: {password}\n"
		                                                      f"\nIs it okay to save?")

		if is_ok:
			# saves username, password and website information to .txt file for future reference
			with open("data.txt", mode="a") as file:
				file.write(f"{website} | {email_username} | {password}\n")

			website_entry.delete(0, END)
			password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.config(padx=10)
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_username_entry = Entry(width=52)
email_username_entry.insert(0, "sandra.igwegbu@myemail.com")  # pre-populates user's email address
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_password_button = Button(text="Add", width=44, command=save)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
