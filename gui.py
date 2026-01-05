import tkinter as tk
import tkinter.font as tkfont
from network_checker import check_host_status
import threading
from datetime import datetime

# Terminal-style GUI for network checks
root = tk.Tk()
root.title("Network Monitor — Terminal View")
root.geometry("700x400")

# Top frame for input
top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X, padx=8, pady=6)

label = tk.Label(top_frame, text="Enter IP or Domain:")
label.pack(side=tk.LEFT)

entry = tk.Entry(top_frame, width=40)
entry.pack(side=tk.LEFT, padx=(6, 6))
entry.focus_set()

check_button = tk.Button(top_frame, text="Check", width=10, command=lambda: start_check())
check_button.pack(side=tk.LEFT)

clear_button = tk.Button(top_frame, text="Clear", width=10, command=lambda: clear_text())
clear_button.pack(side=tk.LEFT, padx=(6, 0))

# Terminal-style text area with scrollbar
font = tkfont.Font(family="Consolas", size=10)
text_frame = tk.Frame(root)
text_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0,8))

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_box = tk.Text(
    text_frame,
    height=20,
    wrap=tk.NONE,
    bg="#0b0b0b",
    fg="#00ff6a",
    insertbackground="#ffffff",
    font=font,
    yscrollcommand=scrollbar.set,
)
result_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
result_box.config(state=tk.DISABLED)
scrollbar.config(command=result_box.yview)

# Helper functions

def append_text(line):
    result_box.config(state=tk.NORMAL)
    result_box.insert(tk.END, line + "\n")
    result_box.see(tk.END)
    result_box.config(state=tk.DISABLED)


def clear_text():
    result_box.config(state=tk.NORMAL)
    result_box.delete("1.0", tk.END)
    result_box.config(state=tk.DISABLED)


def start_check(event=None):
    host = entry.get().strip()
    if not host:
        append_text("Please enter a host to check.")
        return
    check_button.config(state=tk.DISABLED)
    threading.Thread(target=do_check, args=(host,), daemon=True).start()


def do_check(host):
    append_text(f">>> Checking: {host}    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    result = check_host_status(host)

    if isinstance(result, dict):
        log = result.get("log", str(result))
    else:
        log = str(result)

    for line in log.splitlines():
        append_text(line)

    append_text("---")
    check_button.config(state=tk.NORMAL)

# Key binding: Enter to start
entry.bind("<Return>", start_check)

root.mainloop()

