import streamlit as st



class App:
    def __init__(self):
        self._page_choice_sidebar()

    def _page_choice_sidebar(self):
        page_choice = st.sidebar.radio("Que voulez vous faire?", ["Ajouter Saison", "Ajouter Match", "Ajouter Joueur"])


if __name__=="__main__":
    app = App()

