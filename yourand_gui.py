import tkinter as tk
import webbrowser as wb
import random

char_list = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
base_url = "https://youtube.com/watch?v="

def genlink():
	vid = ""
	for x in range(11):
		vid = vid+(random.choice(char_list))

	full_url = base_url+vid
	lbl_ytlink["text"] = full_url

def openlink():
    wb.open(lbl_ytlink["text"])


window = tk.Tk()

lbl_title = tk.Label(text="Youtube Random Link Generator")
lbl_ytlink = tk.Label(text="Youtube Link Here")
btn_generate = tk.Button(text="Generate Link", command=genlink)
btn_open = tk.Button(text="Open Link", command=openlink)

lbl_title.pack()
lbl_ytlink.pack()
btn_generate.pack()
btn_open.pack()

genlink()

window.mainloop()
