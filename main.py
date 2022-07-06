from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


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
	website = website_entry.get().title()
	email_username = email_username_entry.get()
	password = password_entry.get()

	new_data = {
		website: {
			"email/username": email_username,
			"password": password,
		}
	}

	if len(website) == 0 or len(password) == 0 or len(email_username) == 0:
		messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")

	else:
		try:
			with open("data.json", mode="r") as data_file:
				# Reading old data
				data = json.load(data_file)
				# Updating old data with new data
				data.update(new_data)
		except FileNotFoundError:
			with open("data.json", mode="w") as data_file:
				# Creating new json file if one does not already exist
				json.dump(new_data, data_file, indent=4)
		else:
			with open("data.json", mode="w") as data_file:
				# Saving updated data
				json.dump(data, data_file, indent=4)
		finally:
			website_entry.delete(0, END)
			password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
	website = website_entry.get().title()

	try:
		with open("data.json", mode="r") as data_file:
			data = json.load(data_file)
	except FileNotFoundError:
		messagebox.showerror(title="Error!", message="No Data File Found")
	else:
		if website in data:
			messagebox.showinfo(title=f"Your login details for {website}",
			                    message=f"Email/Username: {data[website]['email/username']}\n\n"
			                            f"Password: {data[website]['password']}")
		elif len(website) == 0:
			messagebox.showerror(title="Oops!", message="Please type in the name of the website to search.")
		elif website not in data:
			messagebox.showerror(title="Website not found", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------------ #
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
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="w")

email_username_entry = Entry(width=52)
email_username_entry.insert(0, "sandra.igwegbu@myemail.com")  # pre-populates user's email address
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="w")

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3, sticky="w")

# Buttons
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1, sticky="e")

generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="e")

add_password_button = Button(text="Add", width=44, command=save)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
