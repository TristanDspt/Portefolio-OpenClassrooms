import streamlit as st
from components.charts import make_top_flop, make_ca, make_bar_categ, make_donuts_categ, make_corr_age_ca, make_corr_age_freq, make_corr_tranche_categ



def afficher_metriques_kpi(kpis):
    """Page 1 — CA | Sessions | Clients Uniques"""
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Chiffre d'Affaires",
            value=f"{kpis['ca']:,.0f} €".replace(",", " "),
            delta=f"{kpis['ca_delta']:+,.0f} €".replace(",", " ")
        )
    with col2:
        st.metric(
            label="Sessions",
            value=f"{kpis['sessions']:,.0f}".replace(",", " "),
            delta=f"{kpis['sessions_delta']:+,.0f}".replace(",", " ")
        )
    with col3:
        st.metric(
            label="Clients Uniques",
            value=f"{kpis['clients_unique']:,.0f}".replace(",", " "),
            delta=f"{kpis['clients_delta']:+,.0f}".replace(",", " ")
        )


def afficher_metriques_ventes(kpis):
    """Page 2 — Sessions | Clients Uniques | Panier Moyen"""
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Sessions",
            value=f"{kpis['sessions']:,.0f}".replace(",", " "),
            delta=f"{kpis['sessions_delta']:+,.0f}".replace(",", " ")
        )
    with col2:
        st.metric(
            label="Clients Uniques",
            value=f"{kpis['clients_unique']:,.0f}".replace(",", " "),
            delta=f"{kpis['clients_delta']:+,.0f}".replace(",", " ")
        )
    with col3:
        st.metric(
            label="Panier Moyen",
            value=f"{kpis['panier_moyen']:,.2f} €".replace(",", " "),
            delta=f"{kpis['panier_moyen_delta']:+,.2f} €".replace(",", " ")
        )


def afficher_top_flop(df):
    col1, col2 = st.columns(2)
    with col1:
        fig = make_top_flop(df, 'top')
        st.plotly_chart(fig, width='stretch')
    with col2:
        fig = make_top_flop(df, 'flop')
        st.plotly_chart(fig, width='stretch')


def afficher_ca(df, periode, window):
    fig = make_ca(df, periode, window)
    st.plotly_chart(fig, width='stretch')


def afficher_bar_categ(df):
    fig = make_bar_categ(df)
    st.plotly_chart(fig, width='stretch')


def afficher_donuts_categ(df):
    fig = make_donuts_categ(df)
    st.plotly_chart(fig, width='stretch')

def afficher_corr_age_ca(df):
    fig = make_corr_age_ca(df)
    st.plotly_chart(fig, width='stretch')

def afficher_corr_age_freq(df):
    fig = make_corr_age_freq(df)
    st.plotly_chart(fig, width='stretch')

def afficher_corr_tranche_categ(df):
    fig = make_corr_tranche_categ(df)
    st.plotly_chart(fig, width='stretch')