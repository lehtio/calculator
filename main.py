import tkinter as tk

# Luo pääikkuna
root = tk.Tk()
root.title("Laskin")
root.geometry("600x400")

# Luo laskukenttä
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)







print()








# Näytä ikkuna
root.mainloop()

