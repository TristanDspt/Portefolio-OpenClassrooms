import streamlit as st

MOIS = [
    "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
]


def afficher_sidebar():
    """
    Affiche la sidebar commune et retourne les filtres sélectionnés.
    Returns:
        mois_num (int)      : numéro du mois (1-12)
        annee (int)         : année sélectionnée
        segments (list)     : ex. ["BtoC", "BtoB"]
        categories (list)   : ex. [0, 1, 2]
    """
    with st.sidebar:
        st.title("⚙️ Menu")

        # --- Filtre date ---
        choix_mois = st.selectbox("Mois", MOIS, index=0)
        choix_annee = st.select_slider("Année", [2021, 2022, 2023], value=2022)
        mois_num = MOIS.index(choix_mois) + 1
        st.divider()

        # --- Filtre clients ---
        st.subheader("Type Clients")
        b2c = st.checkbox("BtoC", True)
        b2b = st.checkbox("BtoB", True)
        st.divider()

        # --- Filtre catégories ---
        st.subheader("Catégorie")
        cat0 = st.checkbox("Catégorie 0", True)
        cat1 = st.checkbox("Catégorie 1", True)
        cat2 = st.checkbox("Catégorie 2", True)

    # Construction des listes de filtres
    segments = []
    if b2c:
        segments.append("BtoC")
    if b2b:
        segments.append("BtoB")

    categories = []
    if cat0:
        categories.append(0)
    if cat1:
        categories.append(1)
    if cat2:
        categories.append(2)

    return mois_num, choix_annee, segments, categories
