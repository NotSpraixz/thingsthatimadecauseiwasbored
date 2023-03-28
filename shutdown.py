import tkinter as tk
import os

root = tk.Tk()
root.geometry("200x100")
root.title("Shutdown Prompt")

def shutdown():
    os.system("shutdown /s /t 1")

def cancel():
    root.destroy()

label = tk.Label(root, text="Do you want to shut down your computer?")
label.pack()

yes_button = tk.Button(root, text="Yes", command=shutdown)
yes_button.pack(side="left")

no_button = tk.Button(root, text="No", command=cancel)
no_button.pack(side="right")

root.mainloop()
