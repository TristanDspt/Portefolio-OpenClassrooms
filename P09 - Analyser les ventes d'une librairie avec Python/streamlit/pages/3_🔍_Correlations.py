import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from components.data_loader import get_csv
from components.ui import afficher_corr_age_ca, afficher_corr_age_freq, afficher_corr_tranche_categ


# --- 1. CONFIGURATION PAGE ---
st.set_page_config(page_title="Corrélations", page_icon="🔍", layout="wide")


# --- 2. CHARGEMENT (pas de sidebar sur cette page) ---
df = get_csv()
df_filtre = df.query("segment == 'BtoC'")


# --- 3. INTERFACE ---
st.markdown("<h1 style='text-align: center;'>🔍 Corrélations</h1>", unsafe_allow_html=True)
st.divider()

# --- Tableau récap (full width) ---
st.subheader("Synthèse des corrélations")

data_tableau = {
    "Variable 1":  ["Genre", "Âge", "Âge", "Âge", "Âge", "Tranche d'âge"],
    "Variable 2":  ["Catégorie", "CA global", "CA / client", "Fréquence", "Panier moyen", "Catégorie favorite"],
    "Méthode":     ["Chi² / V Cramer", "Spearman", "Spearman", "Spearman", "Spearman", "Chi² / V Cramer"],
    "Score":       ["0.007", "−0.88", "−0.18", "+0.11", "−0.34", "0.416"],
    "Force":       ["Aucune", "Forte", "Faible", "Faible", "Modérée", "Forte ★"],
}

import pandas as pd
df_tableau = pd.DataFrame(data_tableau)
st.dataframe(df_tableau, width='stretch', hide_index=True)

st.divider()

# --- Tabs des 3 corrélations détaillées ---
st.subheader("Analyse détaillée")

tab1, tab2, tab3 = st.tabs([
    "📊 Âge & CA",
    "🔄 Âge & Fréquence",
    "🎯 Tranche d'âge & Catégorie"
])

with tab1:
    col_graph, col_text = st.columns([2, 1])
    with col_graph:
        afficher_corr_age_ca(df_filtre)
    with col_text:
        st.markdown("**Résultat**")
        st.markdown("Spearman : **−0,88** (global) / **−0,18** (par client)")
        st.markdown("**Conclusion**")
        st.markdown(
            "Les clients jeunes génèrent davantage de CA global. "
            "Cet effet est lié au volume : ramené au client individuel, "
            "la corrélation tombe à −0,18."
        )
        st.markdown("**→ Recommandation**")
        st.markdown(
            "Cibler les jeunes en acquisition reste pertinent, "
            "mais ne pas négliger les seniors dont la valeur individuelle est sous-estimée."
        )

with tab2:
    col_graph, col_text = st.columns([2, 1])
    with col_graph:
        afficher_corr_age_freq(df_filtre)
    with col_text:
        st.markdown("**Résultat**")
        st.markdown("Spearman : **+0,11**")
        st.markdown("**Conclusion**")
        st.markdown(
            "Légère tendance : la fréquence augmente avec l'âge. "
            "Effet marginal mais cohérent."
        )
        st.markdown("**→ Recommandation**")
        st.markdown(
            "Un programme de fidélité ciblé 50+ pourrait amplifier "
            "cet avantage naturel et sécuriser un socle de revenus récurrents."
        )

with tab3:
    col_graph, col_text = st.columns([2, 1])
    with col_graph:
        afficher_corr_tranche_categ(df_filtre)
    with col_text:
        st.markdown("**Résultat**")
        st.markdown("V de Cramer : **0,416** — Forte ★")
        st.markdown("**Conclusion**")
        st.markdown(
            "La tranche d'âge est le meilleur prédicteur de la catégorie favorite. "
            "Les profils d'achat diffèrent significativement entre 18–34, 35–59 et 60+."
        )
        st.markdown("**→ Recommandation**")
        st.markdown(
            "Segmenter les campagnes marketing par tranche d'âge "
            "plutôt que par genre. Adapter les recommandations produits selon ce critère."
        )