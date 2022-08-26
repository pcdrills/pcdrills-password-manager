# Password Manager app by pcdrills
#  You can modify the values of the constants written 
# but if you are unsure what a portion of code does
#  Then it's better you allow it as it is.

from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Generate a random password for the generate button
import random
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 
            'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+', '-']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #selecting random values for the password using a for loops
    # for char in range(nr_letters):
    #     password_letters.append(random.choice(letters))
    # for char in range(nr_symbols):
    #     password_letters.append(random.choice(symbols))
    # for char in range(nr_numbers):
    #     password_letters.append(random.choice(numbers))
    
    #using list comprehensions to select the random values for the password letters
    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    
    # for char in password_list:
    #     password += char    
    password = "".join(password_list)
     
    #clear the previous password field and replace with the newly generated password   
    password_input.delete(0, END)
    values = password
    password_input.insert(0, password)
    # print(f'your password is {password}')

# ---------------------------- SAVE PASSWORD ------------------------------- #
# create or open the password file, save the website|username|email and clear the input fields

def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    validated_fields = True
    if len(email) < 3:
        messagebox.showinfo(title="OOPS! Invalid Email", message="Input a valid Email")
        
    elif len(website) < 3:
        messagebox.showinfo(title="OOPS! Invalid Website", message="Input a valid Website")
        
    elif len(password) < 3:
        messagebox.showinfo(title="OOPS! Invalid Password", message="Input a valid Password")
        
        
    # ask if it's ok to save and if it's ok
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website}\n Email: {email} \nPassword: {password} \n Is it OK to save?")
        if is_ok:
            with open("passwords.txt", mode='a') as password_file:
                line_of_values = f"{website} | {email} | {password} \n"
                password_file.write(line_of_values)
                # print(line_of_values)
                #clear the website and password entries
                website_input.delete(0, END)
                password_input.delete(0, END)
        


# ---------------------------- UI SETUP ------------------------------- #

# create the window
window = Tk()
window.title("pcdrills Password Manager - @pcdrills")
window.config(padx=50, pady=50)


# create the canvas
canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=mypass_img)
canvas.grid(column=1, row=0)

# create website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=2)
# create website field
website_input = Entry(width=43)
website_input.grid(column=1, row=2, columnspan=2)
website_input.focus()


# create email label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=3)
# create email field
email_input = Entry(width=43)
email_input.grid(column=1, row=3, columnspan=2)
email_input.insert(0, "email@email.com")

# create password label
password_label = Label(text="Generate Password:")
password_label.grid(column=0, row=4)
# create password field
password_input = Entry(width=33)
password_input.grid(column=1, row=4)

# create password generate button
generate_password_button = Button(text="Generate", command=generate_password)
generate_password_button.grid(column=2, row=4)

# create add button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=5, columnspan=2)

#pc drills text written at the bottum
pcdrills_text = Label(text="github.com/pcdrills")
pcdrills_text.grid(column=1, row=6)

window.mainloop()

