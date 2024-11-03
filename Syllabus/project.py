import tkinter as tk
from tkinter import messagebox
import requests
import os
from tkinter import filedialog
import webbrowser
def submit_choice():
    opt = var.get()
    if opt == 1:
        webbrowser.open('https://drive.google.com/file/d/19ZOUIbXvOvocXQ_qxUGSXGndgXWH8tHT/view')
    elif opt==2:
        webbrowser.open('https://drive.google.com/file/d/1VNXRTPNzu3dca0DNg-XuuyJlpkRQH4sn/view')
    elif opt==3:
        webbrowser.open('https://drive.google.com/file/d/1VcmVJ_AWAjHzzpUaPQs8ou_BCkcdWHPq/view')
    elif opt==4:
        webbrowser.open('https://drive.google.com/file/d/1NF8LBFHr0PLVnHESTmRpRCLvATdblgTx/view')
    elif opt==5:
        webrowser.open('https://drive.google.com/file/d/1ki7dso3gZciYMnWk6T7F7a3jlZGBpdJ4/view?usp=sharing')
    elif opt==6:
        webbrowser.open('https://drive.google.com/file/d/11MzjPcrghH4SWxv4yioTnjmWQ8z71F3h/view?usp=sharing')
    elif opt==7:
        webbrowser.open('https://drive.google.com/file/d/1KWu9bkDVhjysMX1LClagxqH3coBFdKDc/view')
    elif opt==8:
        webbrowser.open('https://drive.google.com/file/d/1GmRFTYdeQsvDEcgaBJUuLMv6dpp6tuVr/view?usp=sharing')
    elif opt==9:
        webbrowser.open('https://drive.google.com/file/d/1xf_-77Bp9LBxNGWqHJEpfzP5Y96PtJt9/view?usp=sharing')
    elif opt==10:
        messagebox.showwarning("No File","Yet to be uploaded")
    else:
        messagebox.showwarning("Warning", "Please select an option!")
root = tk.Tk()
root.title("Welcome")
root.geometry("1920x1080")
welcome_label = tk.Label(root, text="Welcome to SECE", font=("Arial", 16))
welcome_label.pack(pady=10)
var = tk.IntVar(value=0)

option1 = tk.Radiobutton(root, text="CSE Syllabus", variable=var, value=1)
option1.pack(anchor='w')

option2 = tk.Radiobutton(root, text="AI&ML Syllabus", variable=var, value=2)
option2.pack(anchor='w')

option3 = tk.Radiobutton(root, text="CCE Syllabus", variable=var, value=3)
option3.pack(anchor='w')

option4 = tk.Radiobutton(root, text="ECE Syllabus", variable=var, value=4)
option4.pack(anchor='w')

option5 = tk.Radiobutton(root, text="EEE Syllabus", variable=var, value=5)
option5.pack(anchor='w')

option6 = tk.Radiobutton(root, text="IT Syllabus", variable=var, value=6)
option6.pack(anchor='w')

option7 = tk.Radiobutton(root, text="AI&DS Syllabus", variable=var, value=7)
option7.pack(anchor='w')

option8 = tk.Radiobutton(root, text="Mechanical Syllabus", variable=var, value=8)
option8.pack(anchor='w')

option9 = tk.Radiobutton(root, text="CSBS Syllabus", variable=var, value=9)
option9.pack(anchor='w')

option10 = tk.Radiobutton(root, text="Cyber Security Syllabus", variable=var, value=10)
option10.pack(anchor='w')

submit_button = tk.Button(root, text="View", command=submit_choice)
submit_button.pack(pady=10)

root.mainloop()
