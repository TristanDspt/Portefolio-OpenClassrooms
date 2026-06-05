import pandas as pd
import streamlit as st
import os


@st.cache_data
def get_csv():
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, '..', '..', 'data', 'processed', 'final.csv')
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df['categ'] = df['categ'].astype('category')
    df['sex'] = df['sex'].astype('category')
    df = df.set_index('date')
    return df


def filtrer_df(df, mois_num, annee, segments, categories):
    """
    Filtre le DataFrame sur un mois précis + segments + catégories.
    Utilisé pour les KPIs (calcul du mois courant et du mois précédent).
    """
    df_filtre = df[
        (df.index.month == mois_num) &
        (df.index.year == annee)
    ]
    if segments:
        df_filtre = df_filtre[df_filtre['segment'].isin(segments)]
    if categories:
        df_filtre = df_filtre[df_filtre['categ'].isin(categories)]
    return df_filtre


def filtrer_df_annee(df, annee, segments, categories):
    """
    Filtre le DataFrame sur une année entière + segments + catégories.
    Utilisé pour les graphiques d'évolution (page 2).
    """
    df_filtre = df[df.index.year == annee]
    if segments:
        df_filtre = df_filtre[df_filtre['segment'].isin(segments)]
    if categories:
        df_filtre = df_filtre[df_filtre['categ'].isin(categories)]
    return df_filtre


def get_mois_precedent(mois_num, annee):
    """Retourne (mois, annee) du mois précédent."""
    if mois_num == 1:
        return 12, annee - 1
    return mois_num - 1, annee
