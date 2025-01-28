from tkinter import *


def plus():
    result = float(num1.get()) + float(num2.get())
    output.delete(0, END)
    output.insert(0, result)


def mines():
    result = float(num1.get()) - float(num2.get())
    output.delete(0, END)
    output.insert(0, result)


def mul():
    result = float(num1.get()) * float(num2.get())
    output.delete(0, END)
    output.insert(0, result)


def div():
    result = float(num1.get()) / float(num2.get())
    output.delete(0, END)
    output.insert(0, result)


# Elements

root = Tk()
root.title("HOPE Calculator")
root.geometry("1400x650")

main_label = Label(root, text="Simple Calculator From HOPE", font=("Helvetica", 40))
main_label.pack(pady=20)

plus_btn = Button(root, text="+", font=55, command=plus)
mines_btn = Button(root, text="-", font=55, command=mines)
multi_btn = Button(root, text="X", font=55, command=mul)
div_btn = Button(root, text="/", font=55, command=div)

num1_label = Label(root, text="Enter First Number :", font=80)
num1_label.pack(pady=7)
num1 = Entry(root, font=100)
num1.pack()

num2_label = Label(root, text="Enter Second Number :", font=80)
num2_label.pack(pady=7)
num2 = Entry(root, font=100)
num2.pack()

# result_label = Label(root, text="Result :", font=150)
# result_label.pack(pady=7)
output = Entry(root, font=300)
output.insert(0, "Result Here....")
output.pack()

plus_btn.pack(padx=150, side=LEFT)
mines_btn.pack(padx=150, side=LEFT)
multi_btn.pack(padx=150, side=LEFT)
div_btn.pack(padx=150, side=LEFT)

root.mainloop()