# Author - Jesvin Palatty

from pathlib import Path
from tkinter import filedialog, Tk
from tkinter.messagebox import showerror

import tkinter

root = tkinter.Tk()  # tkinter Object is created

root.fileName = filedialog.askopenfilename(filetypes=(
    ("PDF Files", ".pdf"), ("Doc files", ".docx"), ("All FIles", "*")))  # Asks User to Import the file they want

# if Path(root.fileName).suffix == '.pdf':  # Detection of Type of File That Has been Imported
#     print("PDF File")
# elif Path(root.fileName).suffix == '.doc':
#     print("A Word Document")
# else:
#     showerror("Save", "Unknown extension '{}'".format(Path(root.fileName).suffix))
#
