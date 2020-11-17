import streamlit as st
import numpy as np
import pandas as pds
import seaborn as sb
import matplotlib.pyplot as plt


@st.cache
def load_data(name):
    return pds.read_csv("https://raw.githubusercontent.com/kevintsi/pythonIOT/master/ML/Data/"+name+".csv")


rad = st.sidebar.radio(
    "Sommaire", ["Home", "Affichage des datasets", "Visualisation graphique"])

if rad == "Home":
    st.title("Streamlit Crash course")
    st.subheader("Home")
    st.text("Voici le cours de streamlit")

if rad == "Affichage des datasets":
    st.title("Affichage des datasets")
    option = st.selectbox("Choisi un dataset",
                          ("Titanic_Dataset", "weatherAUS"))
    nb_line = st.text_input("Number of lines : ")

    if nb_line:
        df = load_data(option)
        st.subheader("Colonnes : ")

        st.dataframe(df.head(int(nb_line)))
        df.columns.tolist()
        st.subheader("Types : ")

        st.write(df.dtypes)

        st.subheader("Informations (nombre de lignes et de colonnes) : ")

        st.write("Il y a {} lignes et {} colonnes pour la dataset Titanic".format(
            df.shape[0], df.shape[1]))

        st.subheader("Statistiques : ")

        st.write("Les statistiques du dataset Titanic : ")
        st.write(df.describe())

if rad == "Visualisation graphique":
    st.title("Visualisation graphique")
    option = st.selectbox("Choisi un dataset",
                          ("Titanic_Dataset", "weatherAUS"))
    df = load_data(option)
    st.write(sb.heatmap(df.corr(), annot=True))
    st.pyplot()
    try:
        st.write(plt.hist(df))
        st.pyplot()
    except:
        st.error(
            "Le diagramme n'a pas pu être chargé car il n'y a pas que des valeurs numériques dans ce dernier")
