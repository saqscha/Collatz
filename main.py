from tkinter import *


class App():

   
    def enter(self, e = None):
        self.output_left.config(state='normal')
        self.output_right.config(state='normal')

        self.output_left.delete(0., END)
        self.output_right.delete(0., END)

        self.inp = self.input_entry.get()
        self.inp_int = int(self.inp)

        self.output_right.insert(0.1, '\todd')
        self.output_left.insert(END, '\teven')

        # Anfangs-Zahl einfügen
        if self.inp_int % 2:
                self.output_right.insert(END, '\n-> ')
                self.output_right.insert(END, int(self.inp_int))
                self.output_left.insert(END, '\n-> ')

        else:
            self.output_left.insert(END, '\n-> ')
            self.output_left.insert(END, int(self.inp_int))
            self.output_right.insert(END, '\n-> ')

        # 'rechnen'
        while self.inp_int > 1:
            # ungerade / odd
            if self.inp_int % 2:
                self.inp_int = self.inp_int*3+1
                self.output_right.insert(END, '\n-> ')
                self.output_right.insert(END, int(self.inp_int))
                self.output_left.insert(END, '\n-> ')

            # gerade / even
            else:
                self.inp_int = self.inp_int/2
                self.output_left.insert(END, '\n-> ')
                self.output_left.insert(END, int(self.inp_int))
                self.output_right.insert(END, '\n-> ')
    
        self.input_entry.delete(0, END)
        self.output_left.config(state='disabled')
        self.output_right.config(state='disabled')


    def __init__(self, master):

        #frames
        top_frame = Frame(master, bg='lightgrey')
        bottom_frame = Frame(master, bg='lightgrey')
        output_frame = Frame(bottom_frame, bg='lightgrey', )
        output_frame_left = Frame(output_frame, bg='lightgrey',
                                highlightbackground='lightgrey', borderwidth=2, relief='groove')
        output_frame_right = Frame(output_frame, bg='lightgrey', 
                                highlightbackground='lightgrey', borderwidth=2, relief='groove')
        top_frame.pack(side='top', fill='both', expand=True, padx=2)
        bottom_frame.pack(side='bottom', fill='both', expand=True)
        output_frame.pack(side='bottom', pady=5)
        output_frame_left.pack(side='left', padx=4, pady=2)
        output_frame_right.pack(side='right', padx=4, pady=2)
    

        #widgets
        self.input_entry = Entry(top_frame, width=25, \
            highlightbackground='lightgrey', borderwidth=2, relief='groove')
        self.enter_button = Button(top_frame, text="ENTER", \
            highlightbackground='lightgrey', command=self.enter)
        self.output_left = Text(output_frame_left, width=16, state='disabled')
        self.output_right = Text(output_frame_right, width=16, state='disabled')
        self.scrollb_left = Scrollbar(output_frame_left)
        self.scrollb_right = Scrollbar(output_frame_right)
       

        self.input_entry.pack(side='left', padx=2, pady=12, anchor=NE)
        self.input_entry.bind('<Return>', self.enter)
        self.enter_button.pack(side='right', padx=2, pady=10, anchor=NW)
        self.output_left.pack(side='left')
        self.output_right.pack(side='right')

        self.scrollb_left.pack(side='right', fill='y')
        self.scrollb_right.pack(side='left', fill='y')


        # Configure Scrollbar
        self.scrollb_left.config(command=self.output_left.yview)
        self.scrollb_right.config(command=self.output_right.yview)


root = Tk()
root.title('Collatz Conjecture')
root.geometry('300x350')
root.config(bg='lightgrey')
#root.resizable(0,0)
app = App(root)
root.mainloop()
#root.destroy()
