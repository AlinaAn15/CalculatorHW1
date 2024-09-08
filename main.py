from tkinter import *
from tkinter.messagebox import showerror, showinfo

root = Tk()
root.title('Калькулятор')
root.geometry('285x390+300+200')
root.resizable(False, False)
root['bg'] = 'light grey'

disp1 = StringVar()
disp2 = StringVar()

dis1 = Entry(root, textvariable=disp1, bd=5, state='readonly')
dis1.pack(side=TOP, pady=10)

dis2 = Entry(root, textvariable=disp2, bd=5, state='readonly')
dis2.pack(side=TOP, pady=10)

actField = 1
operation = None


def switchF():
    global actField
    actField = 2 if actField == 1 else 1


def button_click(x):
    global actField
    global operation
    if x == 'C':
        disp1.set('')
        disp2.set('')
        operation = None
        actField = 1
    elif x == '<>':
        switchF()
    elif x in ['%', '÷']:
        operation = x
        n = disp1.get()
        k = disp2.get()

        if not n or not k:
            showerror("Ошибка", "Оба поля должны быть заполнены")
            return

        try:
            if operation == '%':
                res = int(n) % int(k)
            elif operation == '÷':
                res = int(n) // int(k)
            else:
                res = "Ошибка"

            showinfo("Результат", f"Результат: {res}")
            disp1.set('')
            disp2.set('')
            actField = 1
        except Exception as e:
            showerror("Ошибка", "Неверный ввод")
    elif actField == 1:
        disp1.set(disp1.get() + x)
    else:
        disp2.set(disp2.get() + x)


buttons = [['C', '%', '÷'], ['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['-', '0', '<>']]

frame = Frame(root, bg='light grey')
frame.pack(side=BOTTOM, fill=X, padx=5, pady=5)

rc = 0
for row in buttons:
    cc = 0
    for text_btn in row:
        btn = Button(frame, text=text_btn, bg='grey', width=5, height=2, command=lambda x=text_btn: button_click(x))
        btn.grid(row=rc, column=cc, padx=5, pady=5)
        cc += 1
    rc += 1

root.mainloop()