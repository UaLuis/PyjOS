"""
import tkinter as tk
window = tk.Tk()
"""

class Storage:
    def __init__(self, line0, line1, line2):
        self.line0 = line0
        self.line1 = line1
        self.line2 = line2

    def __str__(self):
        return f"{self.line0}\n{self.line1}\n{self.line2}"

def spawn(filename):
    """
    window.title("Text Editor")

    def on_click():
        globals()[filename] = Storage(entry1.get(), entry2.get(), entry3.get())

    button = tk.Button(
        text='Write file',
        width=5,
        height=2,
        bg="blue",
        fg='black',
        command=on_click
    )

    entry1 = tk.Entry(fg="black", bg="white", width=50)
    entry2 = tk.Entry(fg="black", bg="white", width=50)
    entry3 = tk.Entry(fg="black", bg="white", width=50)

    entry1.pack()
    entry2.pack()
    entry3.pack()
    button.pack(pady=10)

    window.mainloop()
    """

    for name_var_range in range(3):
        name_var = f'text_{name_var_range}'
        globals()[name_var] = str(input('Text Editor > '))

    globals()[filename] = Storage(globals()['text_0'], globals()['text_1'], globals()['text_2'])

def burn(filename):
    if filename in globals():
        del globals()[filename]

def say(filename):
    if filename in globals():
        print(globals()[filename])