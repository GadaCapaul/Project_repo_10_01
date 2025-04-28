
st.header("Zeilenüberschrift")
st.markdown("Neue :blue[Zeile]")
x = st.slider("Wie gut kennst du dich in Madrid aus?", 1, 10)

import tkinter as tk

with st.sidebar:
    st.header("Neuer Städtetrip planan")
    st.header("Europakarte")
    st.header("Bereits besuchste Städte")

from tkinter import simpledialog

# Fenster erstellen
root = tk.Tk()
root.withdraw()  # Das Hauptfenster ausblenden

# Eingabefeld anzeigen
name = simpledialog.askstring("Name der Stadt", "In welcher Stadt möchtest du reisen??")

# Antwort anzeigen
print("Du reist nach,", name)



