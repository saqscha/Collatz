from tkinter import *


class App():
    def __init__(self, master):

        #frames
        top_frame = Frame(master)
        bottom_frame = Frame(master)
        output_frame = Frame(bottom_frame)
        scrollb_frame = Frame(bottom_frame)

        top_frame.pack(side='top', fill='both', expand=True)
        bottom_frame.pack(side='bottom', fill='both', expand=True)
        output_frame.pack(side='left')
        scrollb_frame.pack(side='right')

        def enter():
            x = 1
            while x < 30:
                self.output_left.insert(END,"TEST\n")
                x = x + 1


        #widgets
        self.input_entry = Entry(top_frame, width=25, borderwidth=2, relief='groove')
        self.enter_button = Button(top_frame, text="ENTER", command=enter)
        self.output_left = Text(output_frame, width=17, borderwidth=2, relief='groove')
        self.output_right = Text(output_frame, width=17, borderwidth=2, relief='groove')
        self.scrollb = Scrollbar(scrollb_frame, orient='vertical', command=self.output_left.yview)


        self.input_entry.pack(side='left', padx=2, pady=12, anchor=NE)
        self.enter_button.pack(side='right', padx=2, pady=10, anchor=NW)
        self.output_left.pack(side='left', padx=2, pady=2)
        self.output_right.pack(side='right', padx=2, pady=2)
        self.scrollb.pack(side='right', expand=True, fill='y')

    
    


        




root = Tk()
root.geometry('300x350')
#root.resizable(0,0)
app = App(root)
root.mainloop()
root.destroy()
