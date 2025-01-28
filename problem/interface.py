from tkinter import *
from database import *
from hash import hashFunction
from userClass import *

def closePage(root):
    root.destroy()


def loginSuccessfullyPage(root, username, title):
    root.destroy()
    newRoot = Tk()
    newRoot.title(title)
    newRoot.geometry("500x500")
    main_label = Label(newRoot, text=f"Welcom To HOPE Services {username}", font=200)
    main_label.pack(pady=50, padx=40)
    close_btn = Button(newRoot, text="close", font=100, command=lambda: closePage(newRoot))
    close_btn.pack(pady=40)
    newRoot.mainloop()

def signUpClick(inputs, email, root):
    username = inputs[0].get()
    password = inputs[1].get()
    email_value = email.get()

    if(not(is_username_in_database(username))):
        if (not(User.passwordValidation(password))):
            changenpassword_label = Label(root, text="password must have 8 letter or more", font=10)
            changenpassword_label.pack()
            print("chaing password")
        elif (not(User.usernameValidation(username))):
            changenusername_label = Label(root, text="username must have 4 letter or more", font=10)
            changenusername_label.pack()
            print("chaing username")  
        else:
            newUser = User(username, password, email_value)
            add_user_to_database(newUser)
            loginSuccessfullyPage(root, username, "SignUp")
    else:
        changename_label = Label(root, text="username is used before", font=30)
        changename_label.pack()
        print("not signUp")
    

def loignClick(inputs, root):
    username = inputs[0].get()
    password = str(inputs[1].get())
    acctual_password = get_acctual_password(username)

    if (acctual_password == -1):
        signup_handler(root)
    
    if (acctual_password == hashFunction(password)):
        print("loggedin")
        loginSuccessfullyPage(root, username, "Logged-In")
    else:
        wrongPassword_label = Label(root, text="password is not currect", font=30)
        wrongPassword_label.pack()
        print("not login")


def create_bases(root, labelTxt):
    main_label = Label(root, text=labelTxt, font=("Helvetica", 40))
    username_label = Label(root, text="Enter UserName: ")
    password_label = Label(root, text="Enter Password: ")
    username = Entry(root, font=100)
    password = Entry(root, font=100)
    main_label.pack(pady=50)
    username_label.pack()
    username.pack(pady=5)
    password_label.pack()
    password.pack(pady=5)

    return [username, password]

def signup_handler(root):
    root.destroy()
    newRoot = Tk()
    newRoot.title("signUp")
    newRoot.geometry("500x600")
    inputs = create_bases(newRoot, "SIGN-UP")

    email_label = Label(newRoot, text="Enter Email: ")
    email = Entry(newRoot, font=100)
    email_label.pack()
    email.pack(pady=5)
    end_btn = Button(newRoot, text="Sign-Up", font=100, command=lambda: signUpClick(inputs, email, newRoot))
    end_btn.pack(pady=40)

    newRoot.mainloop()

def login_handler(root):
    root.destroy()
    newRoot = Tk()
    newRoot.title("Login")
    newRoot.geometry("300x600")
    inputs = create_bases(newRoot, "Login")

    end_btn = Button(newRoot, text="Login", font=100, command=lambda: loignClick(inputs, newRoot))
    end_btn.pack(pady=100)

    newRoot.mainloop()

def inisializeApp():
    root = Tk()
    root.title("--------HOPE--------")
    root.geometry("700x500")

    main_label = Label(root, text="====HOPE database====", font=("Helvetica", 40))
    signUp_btn = Button(root, text="SIGNUP", font=300, command=lambda: signup_handler(root))
    login_btn = Button(root, text="LOGIN", font=300, command=lambda: login_handler(root))
    main_label.pack()
    signUp_btn.pack(pady=50)
    login_btn.pack(pady=50)

    root.mainloop()

