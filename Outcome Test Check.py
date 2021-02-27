from tkinter import *
from funcs import *
from keys import keys_dict

class Element():
    def __init__(self, master, num, r, c):
        self.num = str(num)
        self.frame = Frame(master, bg='beige')
        self.frame.grid(row=r, column=c)
        self.lab = Label(self.frame, text=self.num, font='Verdena 20', bg='beige')
        self.ent = Entry(self.frame, width=1, font='Verdena 20')
        self.space = Label(self.frame, text='   ', bg='beige')
        if num < 10:
            self.lab.pack(side=LEFT, ipadx=8.5)
        else:
            self.lab.pack(side=LEFT)
        self.ent.pack(side=LEFT, pady=10)
        self.space.pack(side=LEFT)
        

def result():
    answers = answers_to_dict(element_list)
    res = check(keys_dict, answers)
    show_res(res, score)
    
def info():
    answers = answers_to_dict(element_list)
    res = check(keys_dict, answers)
    more_info(res, score)

win = Tk()
win.minsize(width=880, height=520)
win['bg'] = 'beige'

top_frame = Frame(bg='beige')
mid_frame = Frame(bg='beige')
bot_frame = Frame(bg='beige')
top_frame.pack(expand=1)
mid_frame.pack(expand=1)
bot_frame.pack(expand=1)

element_list = []
order = 1
for i in range(5):
    for j in range(10):
        element_list.append(Element(top_frame, order, i, j))
        order += 1

check_btn = Button(mid_frame, text='Проверить', command=result)
check_btn.pack(side=LEFT, padx=20, pady=10)

info_btn = Button(mid_frame, text='Подробнее', command=info)
info_btn.pack(side=LEFT)

score = Label(bot_frame, width=100, height=8, font='Verdena 10', bg='lightgrey')
score.pack(expand=1)

win.mainloop()