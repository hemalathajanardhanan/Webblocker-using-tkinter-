import os
import tkinter as tk

if os.name == 'nt':
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
else:
    hosts_path = '/etc/hosts'



def block_websites():
    websites = entry.get().split()
    with open(hosts_path, 'a') as file:
        for website in websites:
            file.write(f'127.0.0.1 {website}\n')
    label.config(text="Websites blocked successfully!")

def unblock_websites():
    websites = entry.get().split()
    with open(hosts_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(website in line for website in websites):
                file.write(line)
        file.truncate()
    label.config(text="Websites unblocked successfully!")

window = tk.Tk()
window.title("Website Blocker")

label = tk.Label(window, text="Enter websites to block/unblock:")
label.pack()

entry = tk.Entry(window)
entry.pack()

block_button = tk.Button(window, text="Block", command=block_websites)
block_button.pack()

unblock_button = tk.Button(window, text="Unblock", command=unblock_websites)
unblock_button.pack()

window.mainloop()
