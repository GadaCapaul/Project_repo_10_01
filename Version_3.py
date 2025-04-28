

import tkinter as tk
from tkinter import messagebox

def absenden():
    name = entry_name.get()
    alter = entry_alter.get()
    stadt = entry_stadt.get()
    messagebox.showinfo("Eingaben", f"Name: {name}\nAlter: {alter}\nStadt: {stadt}")

# Fenster erstellen
root = tk.Tk()
root.title("Mehrere Eingaben")

# Name
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Alter
tk.Label(root, text="Alter:").pack()
entry_alter = tk.Entry(root)
entry_alter.pack()

# Stadt
tk.Label(root, text="Stadt:").pack()
entry_stadt = tk.Entry(root)
entry_stadt.pack()

# Button zum Absenden
tk.Button(root, text="Absenden", command=absenden).pack()

# Fenster starten
root.mainloop()


anreisetag, abreisetag = st.date_input(
    "An welchem Tag wirst du an- und abreisen?",
    value=(anreisetag, anreisetag + datetime.timedelta(days=1)), #Standardwert
    min_value=heute
)

anreisedaten = st.date_input(
    "An welchem Tag wirst du an- und abreisen?",
    value=(datetime.date.today(), datetime.date.today() + datetime.timedelta(days=1)),
)

if isinstance(anreisedaten, tuple):
    anreisetag, abreisetag = anreisedaten
else:
    st.error("Bitte wähle sowohl einen Anreise- als auch einen Abreisetag aus.")































