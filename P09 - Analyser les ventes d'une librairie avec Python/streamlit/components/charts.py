import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np


def make_top_flop(df, choix):
    top_flop = df.groupby('id_prod')['price'].sum().reset_index().sort_values(by='price', ascending=False)
    if choix == 'top':
        df_trace = top_flop.head(5)
        name = "Top 5"
    else:
        df_trace = top_flop.tail(5)
        name = "Flop 5"

    fig = go.Figure()

    fig.add_trace(go.Bar(
    name=name,
    x=df_trace['id_prod'],
    y=df_trace['price'],
    hovertemplate="%{y:,.0f} €",
    marker_color=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']
    ))

    # Habillage
    fig.update_layout(
        showlegend=False,
        height=600,
        hovermode='x unified',
        hoverlabel=dict(font_size=12),
        separators=". ",
        margin=dict(t=40, b=25, l=25, r=25),
        title=f"{name} ventes (CA par produits)"
    )

    return fig


def make_ca(df, periode, window):
    if periode == 'Mois':
        freq = 'ME'
    else:
        freq = 'D'

    df = df.groupby(pd.Grouper(freq=freq))['price'].sum().to_frame()
    df['moy_mobile'] = round(df['price'].rolling(window=window).mean(), 2)
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['price'],
        name="CA",
        mode='lines+markers',
        marker=dict(size=4),
        line=dict(color="#003f5c"),
        hovertemplate="%{y:,.0f} €"
    ))

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['moy_mobile'],
        name="Moyenne mobile",
        mode='lines+markers',
        marker=dict(size=4),
        line=dict(color='#ffa600'),
        hovertemplate="%{y:,.0f} €"
    ))

    # Habillage
    fig.update_layout(
        xaxis=dict(tickformat="%b %Y",),
        legend=dict(orientation='h', y=1.1, x=0.5, xanchor='center'),
        height=400,
        width=800,
        hovermode='x unified',
        hoverlabel=dict(font_size=12),
        separators=". ",
        margin=dict(t=50, b=50, l=50, r=50),
        title="Evolution du chiffre d'affaire"
    )

    return fig


def make_bar_categ(df):
    df = df.groupby('categ', observed=True)['price'].sum().reset_index()
    total = df['price'].sum()
    df['pct'] = df['price'] / total * 100

    fig = go.Figure()

    fig.add_trace(go.Bar(
        name="CA catégorie",
        x=df['categ'],
        y=df['price'],
        customdata=df['pct'],
        hovertemplate="%{y:,.0f} € (%{customdata:.1f}%)",
        marker_color=['#1B2A4A', '#0D6E8A', '#E8A020']
    ))

    # Habillage
    fig.update_layout(
        height=600,
        hovermode='x unified',
        hoverlabel=dict(font_size=12),
        separators=". ",
        margin=dict(t=50, b=50, l=40, r=40),
        title="Repartition CA par Catégories"
    )

    return fig


def make_donuts_categ(df):
    df = df.groupby('categ', observed=True)['id_prod'].count().reset_index()

    fig = go.Figure()

    fig.add_trace(go.Pie(
        labels=df['categ'],
        values=df['id_prod'],
        hole=0.65,
        hovertemplate="%{value:,.0f}<extra></extra>",
        marker=dict(colors=['#1B2A4A', '#0D6E8A', '#E8A020']),
        textinfo='label+percent'
    ))
    fig.update_layout(
        separators=". ",
        height=600,
        margin=dict(t=50, b=15, l=15, r=15),
        showlegend=False,
        title="Répartition du Catalogue par Catégorie"
    )

    return fig

def make_corr_age_ca(df):
    df.reset_index()
    ca_par_age = df.groupby('age')['price'].sum().reset_index()
    profil_age = df.groupby(['client_id', 'age'])['price'].sum().reset_index()

    fig = make_subplots(rows=2, cols=1, vertical_spacing=0.15,
                        subplot_titles=["CA total par âge", "CA total par client selon son âge"])

    # Graph 1 — ca_par_age
    fig.add_trace(go.Scatter(
        name="CA",
        x=ca_par_age['age'], y=ca_par_age['price'],
        mode='markers',
        marker=dict(color='#0D6E8A', size=6)
    ), row=1, col=1)

    # Graph 2 — profil_age  
    fig.add_trace(go.Scatter(
        name="CA",
        x=profil_age['age'], y=profil_age['price'],
        mode='markers',
        marker=dict(color='#0D6E8A', size=4, opacity=0.5)
    ), row=2, col=1)

    # Habillage
    fig.update_layout(
        showlegend=False,
        height=600,
        margin=dict(t=50, b=50, l=80, r=20),
        hovermode='x unified'
    )

    # Droite de régression pour ca_par_age
    z = np.polyfit(ca_par_age['age'], ca_par_age['price'], 1)
    p = np.poly1d(z)
    x_line = np.linspace(ca_par_age['age'].min(), ca_par_age['age'].max(), 100)

    fig.add_trace(go.Scatter(
        name="Régression",
        x=x_line, y=p(x_line),
        mode='lines',
        line=dict(color='#E8A020', width=2)
    ), row=1, col=1)

    # Droite de régression pour profil_age
    z = np.polyfit(profil_age['age'], profil_age['price'], 1)
    p = np.poly1d(z)
    x_line = np.linspace(profil_age['age'].min(), profil_age['age'].max(), 100)

    fig.add_trace(go.Scatter(
        name="Régression",
        x=x_line, y=p(x_line),
        mode='lines',
        line=dict(color='#E8A020', width=2)
    ), row=2, col=1)

    return fig


def make_corr_age_freq(df):
    freq = df.groupby(['client_id', 'age']).agg({'session_id': 'nunique'}).reset_index()
    
    fig = go.Figure()

    # Dessin
    fig.add_trace(go.Scatter(
        x=freq['age'], y=freq['session_id'],
        mode='markers',
        marker=dict(color='#0D6E8A', size=6)
    ))

    # Habillage
    fig.update_layout(
        showlegend=False,
        height=500,
        margin=dict(t=50, b=50, l=80, r=20),
        hovermode='x unified'
    )

    # Droite de régression
    z = np.polyfit(freq['age'], freq['session_id'], 1)
    p = np.poly1d(z)
    x_line = np.linspace(freq['age'].min(), freq['age'].max(), 100)

    fig.add_trace(go.Scatter(
        x=x_line, y=p(x_line),
        mode='lines',
        line=dict(color='#E8A020', width=2)
    ))

    return fig


def make_corr_tranche_categ(df):
    # Préparation du df
    count = df.groupby(['client_id', 'age', 'categ'], observed=True).size().reset_index(name='nb_achats')
    count = count.sort_values(['client_id', 'nb_achats'], ascending=[True, False])
    categ_fav = count.drop_duplicates('client_id').copy()

    # Création de tranche d'age pour pouvoir calculer une force sur la correlation
    categ_fav['tranche_age'] = pd.cut(
                            categ_fav['age'], bins=[17, 34, 59, 100], 
                            labels=['18-34', '35-59', '60+']
                            )
    categ_fav['tranche_age'] = categ_fav['tranche_age'].astype('category')

    # Préparation des données
    counts = categ_fav.groupby(['tranche_age', 'categ'], observed=True).size().reset_index(name='nb_clients')

    fig = go.Figure()

    fig.add_trace(go.Bar(
        name='Catégorie 0',
        x=counts[counts['categ'] == 0]['tranche_age'],
        y=counts[counts['categ'] == 0]['nb_clients'],
        marker_color='#1B2A4A'
    ))
    fig.add_trace(go.Bar(
        name='Catégorie 1',
        x=counts[counts['categ'] == 1]['tranche_age'],
        y=counts[counts['categ'] == 1]['nb_clients'],
        marker_color='#0D6E8A'
    ))
    fig.add_trace(go.Bar(
        name='Catégorie 2',
        x=counts[counts['categ'] == 2]['tranche_age'],
        y=counts[counts['categ'] == 2]['nb_clients'],
        marker_color='#E8A020'
    ))
    # Habillage
    fig.update_layout(
        height=500,
        margin=dict(t=50, b=50, l=80, r=20),
        legend=dict(orientation='h', y=1.1, x=0.5, xanchor='center'),
        hovermode='x unified',
        barmode='group'
    )

    return fig