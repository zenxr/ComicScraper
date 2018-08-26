"""
adder.py
~~~~~~

Creates a simple GUI for summing two numbers.
"""

import tkinter
from tkinter import ttk
from tkinter import filedialog
from multiprocessing import Process,Queue, Pipe
import scraper

folder_path = ""

def on_quit():
    """Exits program."""
    quit()

def file_browse_button():
    global folder_path
    directory = filedialog.askdirectory()
    folder_path = directory
    save_path_label['text'] = folder_path

def run_button():
    print(folder_path)
    print(url_entry.get())
    # on button click, run scraper
    scraper.getSeries(url_entry.get(), folder_path)


# set up tkinter root
root = tkinter.Tk()

root.title('Comic Downloader')
root.option_add('*tearOff', 'FALSE')

menubar = tkinter.Menu(root)

menu_file = tkinter.Menu(menubar)
menu_file.add_command(label='Exit', command=on_quit)

menu_edit = tkinter.Menu(menubar)

menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')

root.config(menu=menubar)

browseButton = ttk.Button(text="Select Save Location", command=file_browse_button)
browseButton.grid(row=0, column=0, ipadx=10, ipady=10, padx=20, pady=20)

# display base storage directory
save_path_label = ttk.Label(text = "/Some/Example/Storage/Location")
save_path_label.grid(row=0, column=1, columnspan=2, sticky=tkinter.W, ipadx=10, ipady=10, padx=10, pady=10)


# url textbox
url_entry = ttk.Entry(master=root)
url_entry.grid(row=1, column=0, ipadx=50, ipady=5, padx=10, pady=10, sticky=tkinter.E)

# display "URL to scrape" message
lbl1 = ttk.Label(text="Paste the URL to scrape to to the left.")
lbl1.grid(row=1, column=2, ipadx=10, ipady=10, padx=10, pady=10, sticky=tkinter.W)

# Button to run scraper
runButton = ttk.Button(text="Run!", command=run_button)
runButton.grid(row=2, column=0, ipadx=10, ipady=10, padx=10, pady=10, sticky=tkinter.N)

# scraping output
output_text = tkinter.Text(master=root)
output_text.grid(row=2, column=2, ipadx=10, ipady=10, padx=10, pady=10)
output_text.insert(tkinter.INSERT, "Just testing!\nJust testing!\nJust testing!\nJust testing!\nJust testing!\nJust testing!")

root.mainloop()
