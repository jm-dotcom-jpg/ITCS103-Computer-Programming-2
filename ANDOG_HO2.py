import tkinter as tk

window = tk.Tk()
window.title("John Manuel's Profile")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg="skyblue")


title = tk.Label(
    window,
    text="Student Profile",
    font=("Arial", 24, "bold"),
    bg="skyblue",
    fg="black"
)

title.pack(pady=30)

info_font = ("Times New Roman", 14)

tk.Label(window, text="Name : John Manuel C. Andog",
         font=info_font, bg="skyblue", anchor="w").pack(fill="x", padx=40)

tk.Label(window, text="Age : 19 years old",
         font=info_font, bg="skyblue", anchor="w").pack(fill="x", padx=40, pady=5)

tk.Label(window, text="Course : BSIT",
         font=info_font, bg="skyblue", anchor="w").pack(fill="x", padx=40, pady=5)

tk.Label(window, text="Birthday : May 8, 2006",
         font=info_font, bg="skyblue", anchor="w").pack(fill="x", padx=40, pady=5)


tk.Label(window, text="Motto :",
         font=info_font, bg="skyblue", anchor="w").pack(fill="x", padx=40, pady=(20, 5))

tk.Label(window,
         text="Rise above the rest, or be buried beneath them.",
         font=("Times New Roman", 12, "italic"),
         bg="skyblue",
         wraplength=500,
         justify="left").pack(padx=40)

window.mainloop()
