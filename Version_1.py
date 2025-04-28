#Alle importierten Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import datetime as dt

#Startpage der Städtetrip Applikation

st.title("Plane deine Städtrip jetzt!")

#Eingabefeld erstellen und anzeigen
name1= st.text_input("Was ist dein Reiseziel für den nächsten Städtetrip?")
if name1:
    st.write(f'Alles klar, in {name1} könntest du folgende Aktivitäten machen')

#Heute als Standarddatum
heute = dt.date.today()
anreisetag = heute
abreisetag = heute

#Datum-Eingabefelder im Kalender
anreisetag = st.date_input(
    "An welchem Tag wirst du anreisen?",
    value=anreisetag, #Standardwert
    min_value=heute
)
abreisetag = st.date_input(
    "An welchem Tag wirst du abreisen?",
    value=(anreisetag + datetime.timedelta(days=1)), #Standardwert
    min_value=anreisetag)

#Budget Range Auswahl
budget = st.slider(f'Wie viel möchtest du maximal für eine Aktivität in {name1} ausgeben?', 0, 500, 0, step=10)


# Vordefinierte Checkboxen für Interessen des Reisenden
st.write("Deine Interessen:")
option1 = st.checkbox("Kultur & Geschichte")
option2 = st.checkbox("Kulinarik & Gastronomie")
option3 = st.checkbox("Sport & Aktivitäten")
option4 = st.checkbox("Architektur & Stadtbild")
option5 = st.checkbox("Natur & Outdoor")
option6 = st.checkbox("Shopping")
option7 = st.checkbox("Nachtleben")

st.button("übermitteln")











