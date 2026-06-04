# P6 — Optimisation de la gestion des données d'une boutique avec Python

> Projet de formation | Février 2026

## Contexte

Mission pour **Bottleneck**, caviste en ligne, afin de fiabiliser et consolider les données produits issues de deux systèmes d'information hétérogènes : l'ERP interne et le site web e-commerce.

3 fichiers sources : `erp.xlsx` (stock & prix), `web.xlsx` (données produits web), `liaison.xlsx` (table de correspondance des identifiants).

## Stack technique

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4c8cbf?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

## Démarche

### 1. Analyse exploratoire des 3 sources
- Audit de chaque fichier : dimensions, types, valeurs manquantes, doublons
- Détection des incohérences entre `stock_status` et `stock_quantity`

### 2. Nettoyage & fiabilisation
Anomalies détectées et traitées variable par variable :

| Variable | Anomalie détectée | Traitement |
|----------|-------------------|------------|
| `price` | 3 prix négatifs (-20€, -8€, -9.1€) | Remontée métier + correction après vérification |
| `stock_quantity` | Valeurs négatives | Traitement + signal donneur d'ordre |
| `stock_status` | Incohérences avec la quantité réelle | Recalcul depuis `stock_quantity` |

### 3. Jointure des sources
- Fusion ERP × Web via table de liaison
- Gestion des produits sans correspondance (analyse des non-matchs)

### 4. Analyses univariées & corrélations
- Distribution des prix, stocks et ventes par catégorie de produit
- Heatmap de corrélation Stock / Prix / Ventes :
  - **-0.52** entre Prix et Ventes — relation négative marquée
  - **+0.44** entre Stock et Ventes — corrélation positive modérée
  - **-0.11** entre Stock et Prix — pas de relation significative

### 5. Indicateurs métier calculés

5 indicateurs construits sur le dataset consolidé (825 → 714 lignes après Inner Join) :

| Indicateur | Résultat |
|------------|----------|
| Chiffre d'affaires total | 143 680 € |
| Valeur du stock immobilisé | 277 000 € (~2 mois de CA) |
| Taux de marge moyen | 61% (spiritueux > 75%, Champagne ~40%) |
| Autonomie de stock max | 25 mois sur certaines références |
| Z-score outliers prix | Références Prestige > 115€ isolées |

### 6. Export
Dataset consolidé `df_merge` exportable en Excel pour partage avec les équipes métier.

## Storytelling

> *"Le catalogue est résilient : il faut 61% des références pour couvrir 80% du CA — pas de dépendance à 3 bouteilles stars. Mais le stock est le vrai sujet : 277 000€ immobilisés, des références à 25 mois de stock théorique, et une corrélation prix/ventes de -0.52 qui dit clairement que toute hausse de prix se paie en volume. Anomalie critique identifiée : un produit acheté 77€ HT revendu 10€ HT — erreur de saisie prioritaire à corriger."*

## Livrables

- `Despont_Tristan_1_notebook` — Notebook Jupyter complet (EDA, nettoyage, fusion, analyses)
- `Despont_Tristan_2_presentation` — Support de présentation
