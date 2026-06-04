import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from components.data_loader import get_csv, filtrer_df, filtrer_df_annee, get_mois_precedent
from components.sidebar import afficher_sidebar, MOIS
from components.logic import get_kpi
from components.ui import afficher_metriques_ventes, afficher_top_flop, afficher_bar_categ, afficher_donuts_categ


# --- 1. CONFIGURATION PAGE ---
st.set_page_config(page_title="Ventes", page_icon="📈", layout="wide")

st.markdown("""
    <style>
    [data-testid="stMetric"] {
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    [data-testid="stMetricLabel"] {
        justify-content: center;
        width: 100%;
        min-height: 2rem;
        display: flex;
        align-items: flex-end;
    }
    [data-testid="stMetricValue"] { width: 100%; }
    [data-testid="stMetricDelta"] { justify-content: center; width: 100%; }
    </style>
""", unsafe_allow_html=True)


# --- 2. CHARGEMENT ---
df = get_csv()
mois_num, annee, segments, categories = afficher_sidebar()


# --- 3. CALCULS ---
df_current = filtrer_df(df, mois_num, annee, segments, categories)

prev_mois, prev_annee = get_mois_precedent(mois_num, annee)
df_prev = filtrer_df(df, prev_mois, prev_annee, segments, categories)

kpis = get_kpi(df_current, df_prev)

# Données annuelles pour les graphiques (filtre mois ignoré)
df_annee = filtrer_df_annee(df, annee, segments, categories)


# --- 4. INTERFACE ---
st.markdown("<h1 style='text-align: center;'>📈 Ventes</h1>", unsafe_allow_html=True)
st.markdown(
    f"<h2 style='text-align: center;'>{MOIS[mois_num - 1]} {annee}</h2>",
    unsafe_allow_html=True
)
st.divider()

if df_current.empty:
    st.warning("Aucune donnée pour la période et les filtres sélectionnés.")
else:
    afficher_metriques_ventes(kpis)
    st.divider()

    tab1, tab2 = st.tabs(["🏆 Top / Flop", "📊 Répartition Catégories"])

    with tab1:
        afficher_top_flop(df_annee)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            afficher_bar_categ(df_annee)
        with col2:
            afficher_donuts_categ(df_annee)
