import subprocess # lets me run external programs
import os # to interact with the operating system
import hashlib # to have an interface to hash files
import requests # to interact with web services/make HTTP requests
import threading # to use concurrency for running tasks
import time # getting current date and time
import tkinter as tk # for the GUI
from tkinter import filedialog, scrolledtext, ttk
from datetime import datetime

YARA_PATH = "yara64.exe"
RULES_FILE = "rules\\trojan_rules.yar"
VT_API_KEY = "34923601df873108e50af7f497e636c88f6087851ca5321dde99cfebec76f509"
VT_URL = "https://virustotal.com/api/v3/files/"
UPLOAD_URL = "https://www.virustotal.com/api/v3"
DELAY = 15 # api rate limit is 1 req per 15 sec

# -------- GUI --------
root = tk.Tk() # main window
root.title("TREDR - Trojan Risk Education & Detection Resource") # main title seen in the window 
root.geometry("760x500") # size of the entire screen

# -------- NOTEBOOK --------
# creating a notebook so theres different tabs in the GUI
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=12, pady=8) #packs the notebook into the root window with padding

# frame for the tabs (can be extendable)
scan_tab = ttk.Frame(notebook) # the first main page for scanning
history_tab = ttk.Frame(notebook) # file list of all the files scanned

# adding the tabs to the notebook
notebook.add(scan_tab, text="Scan") # tab is called 'Scan'
notebook.add(history_tab, text="History") # tab is called 'History'

style = ttk.Style()
style.theme_use("clam") # this is the theme of the GUI (clam is a light theme)
style.configure("TNotebook", background="#0f1320", borderwidth=0)

style.configure("Treeview", rowheight=24, font=("Arial", 10)) #treeview is the table that will be used in the history tab - the name is from the tkinter library
style.configure("Treeview.Heading", font=("Arial", 12, "bold")) # the headings of the table will be bolded
style.configure("TButton", font=("Arial", 10), padding=6) # the buttons will have a font of Arial, size 10 and padding of 6 pixels
