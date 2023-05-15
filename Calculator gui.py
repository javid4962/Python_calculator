from tkinter import *
from tkinter import font

root = Tk()
root.title("Simple calculator")
root.configure(bg='black')
root.geometry('350x480')

e = Entry(root, width=30, borderwidth=30, bg="black",
          fg="white", font=20, justify=RIGHT)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_num = e.get()
    global f_num, tp
    f_num = float(first_num)
    tp = 1
    e.delete(0, END)


def button_sub():
    first_num = e.get()
    global f_num, tp
    f_num = float(first_num)
    tp = 2
    e.delete(0, END)


def button_mul():
    first_num = e.get()
    global f_num, tp
    f_num = float(first_num)
    tp = 3
    e.delete(0, END)


def button_div():
    first_num = e.get()
    global f_num, tp
    f_num = float(first_num)
    tp = 4
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    match tp:
        case 1:
            return e.insert(0, float(f_num) + float(second_number))
        case 2:
            return e.insert(0, float(f_num) - float(second_number))
        case 3:
            return e.insert(0, float(f_num) * float(second_number))
        case 4:
            return e.insert(0, float(f_num) / float(second_number))


button_1 = Button(root, text="1", padx=30, pady=20, font=1, border=5,
                  bg="#1a2327", fg="white", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=20, font=1, border=5,
                  bg="#1a2327", fg="white", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=20, font=1, border=5,
                  bg="#1a2327", fg="white", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=20, font=1, border=5,
                  bg="#1a2327", fg="white", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=20, font=1, border=5,
                  bg="#1a2327", fg="white", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=20, font=1, border=5,
                  bg="#1a2327", fg="white", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=20, font=1, border=5,
                  bg="#1a2327", fg="white", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=20, font=1, border=5,
                  bg="#1a2327", fg="white", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=20, font=1, border=5,
                  bg="#1a2327", fg="white", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=20, font=1, border=5,
                  bg="#1a2327", fg="white", command=lambda: button_click(0))
button_add = Button(root, text="+", padx=28, pady=20, font=1,
                    border=5, bg="#1a2327", fg="white", command=button_add)
button_sub = Button(root, text="-", padx=29, pady=20, font=1,
                    border=5, bg="#1a2327", fg="white", command=button_sub)
button_mul = Button(root, text="*", padx=29, pady=20, font=1,
                    border=5, bg="#1a2327", fg="white", command=button_mul)
button_div = Button(root, text="/", padx=29, pady=20, font=1,
                    border=5, bg="#1a2327", fg="white", command=button_div)
button_equal = Button(root, text="=", padx=29, pady=20,
                      font=1, bg="#f50000", border=5,  command=button_equal)
button_clear = Button(root, text="clear", padx=18, pady=20, font=1,
                      border=5, bg="#1a2327", fg="white", command=button_clear)
button_dot = Button(root, text=".", padx=31, pady=20, font=1, border=5,
                bg="#1a2327", fg="white", command=lambda: button_click('.'))


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

button_add.grid(row=1, column=4)
button_sub.grid(row=2, column=4)
button_mul.grid(row=3, column=4)
button_div.grid(row=4, column=4)
button_equal.grid(row=5, column=4)
button_clear.grid(row=4, column=0)
button_dot.grid(row=4, column=2)

root.mainloop()
