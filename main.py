import threading
import socket
import tkinter as tk
from tkinter import scrolledtext, messagebox

def scan_ports():
    target = entry_ip.get().strip()
    if not target:
        messagebox.showerror("Error", "الرجاء ادخال اي IP او وب لوك")
        return
    
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, f"[-] Starting scan on {target}...\n", "info")
    
    ports = [21, 22, 23, 80, 443, 8080, 3306]
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                text_result.insert(tk.END, f"[+] Port {port} is OPEN\n", "open")
            s.close()
        except:
            pass
            
    text_result.insert(tk.END, "[-] Scan finished, fuck yeah.\n", "done")

def start_thread():
    threading.Thread(target=scan_ports).start()

app = tk.Tk()
app.title("Hackethics Pro Scanner")
app.geometry("450x400")
app.configure(bg="#1e1e1e")

label = tk.Label(app, text="Target IP:", fg="#ffffff", bg="#1e1e1e")
label.pack(pady=5)

entry_ip = tk.Entry(app, width=30, font=("Arial", 11))
entry_ip.pack(pady=5)

btn = tk.Button(app, text="Start Scan", command=start_thread, bg="#00aa00", fg="#ffffff")
btn.pack(pady=10)

text_result = scrolledtext.ScrolledText(app, height=14, width=50, bg="#111111", fg="#ffffff")
text_result.pack(pady=5)
text_result.tag_config("open", foreground="#4ec9b0")
text_result.tag_config("info", foreground="#9cdcfe")
text_result.tag_config("done", foreground="#ce9178")

app.mainloop()

