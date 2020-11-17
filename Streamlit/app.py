from matplotlib.pyplot import figure
import streamlit as st
import numpy as np
import pandas as pds
import seaborn as sb
import matplotlib.pyplot as plt
import os

data = os.listdir("ML\Data")


@st.cache
def load_data(name):
    return pds.read_csv("ML\\Data\\"+name)


rad = st.sidebar.radio(
    "Sommaire", ["Home", "Affichage des datasets", "Visualisation graphique"])

if rad == "Home":
    st.title("Streamlit Crash course")
    st.subheader("Home")
    st.text("Voici le cours de streamlit")

if rad == "Affichage des datasets":
    st.title("Affichage des datasets")
    option = st.selectbox("Choisi un dataset",
                          data)

    df = load_data(option)
    nb_line = st.number_input(
        "Nombre de lignes à charger : ", min_value=1, max_value=len(df))

    st.subheader("Affichage des {} premieres lignes : ".format(nb_line))

    st.dataframe(df.head(nb_line))
    st.subheader("Types : ")

    st.write(df.dtypes)

    selected_type = st.selectbox(
        "Choisi une colonne : ", df.columns)

    st.write("Le type de {} est {} ".format(
        selected_type, df[selected_type].dtype))

    st.subheader("Informations (nombre de lignes et de colonnes) : ")

    st.write("Il y a {} lignes et {} colonnes pour le dataset".format(
        df.shape[0], df.shape[1]))

    st.subheader("Statistiques : ")

    st.write("Les statistiques du dataset : ")
    st.write(df.describe())

if rad == "Visualisation graphique":
    st.title("Visualisation graphique")
    option = st.selectbox("Choisi un dataset",
                          data)
    df = load_data(option)
    plt.figure(figsize=(15, 10))
    st.write(sb.heatmap(df.corr(), annot=True, linewidths=.30))
    st.pyplot()
    try:
        st.write(plt.hist(df))
        st.pyplot()
    except:
        st.error(
            "Le diagramme n'a pas pu être chargé car il n'y a pas que des valeurs numériques dans ce dernier")
