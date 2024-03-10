import tkinter as tk
from tkinter import messagebox
import socket

def get_ip_addresses():
    value = EditBox.get()
    try:
        addrs = socket.getaddrinfo(value, None)
        for addr in addrs:
            print(addr)
            messagebox.showinfo('結果',addrs)
    except socket.gaierror:
        print("Invalid or unreachable address.")

root = tk.Tk()
root.title("wawan a1.0")

static1 = tk.Label(text='wawan a1.0')
static1.pack()

EditBox = tk.Entry()
EditBox.insert(tk.END, "URLを入力")
EditBox.pack()

button = tk.Button(text="Get IP Addresses", command=get_ip_addresses)
button.pack()

root.mainloop()