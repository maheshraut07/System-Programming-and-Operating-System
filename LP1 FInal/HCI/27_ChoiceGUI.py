import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        listbox.delete(0, tk.END)  # Clear the listbox
        for item in os.listdir(folder_path):
            listbox.insert(tk.END, item)

def open_file():
    selected_file = listbox.get(listbox.curselection())
    os.system(f'open "{selected_file}"')  # Adjust for Windows or other operating systems

root = tk.Tk()
root.title("File Explorer")

# Frame for buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

# Browse button
browse_button = ttk.Button(button_frame, text="Browse Folder", command=browse_folder)
browse_button.pack(side=tk.LEFT, padx=5)

# Listbox to display directory contents
listbox = tk.Listbox(root)
listbox.pack(expand=True, fill="both")

# Open button
open_button = ttk.Button(root, text="Open File", command=open_file)
open_button.pack()

root.mainloop()
