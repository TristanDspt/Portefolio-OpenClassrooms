# P9 — Analyse des ventes d'une librairie avec Python

> Projet de formation | Mars 2026

## Contexte

Mission d'analyse pour une librairie en ligne : comprendre les comportements d'achat des clients à travers des statistiques descriptives et des tests statistiques, afin d'identifier des leviers de segmentation et de ciblage marketing.

## Stack technique

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4c8cbf?style=for-the-badge&logo=python&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

## Analyses réalisées

### Genre vs Catégories — Le "Mirage Statistique"
Test du chi² sur 600k lignes → résultat significatif en apparence. Mais en analysant par individu (profil client unique) → p > 0.05 : les goûts sont totalement mixtes entre genres. **Conclusion : le genre n'est pas un levier de segmentation valide pour les catégories.**

> Point méthodologique clé : avec un volume de données suffisant, le chi² détecte des effets statistiquement significatifs mais sans valeur pratique. Analyse au niveau individuel indispensable.

### Âge vs Dépense totale (cumul vs individu)
- **Approche cumulative :** les jeunes semblent dépenser plus — mais c'est un artefact de volume, pas de comportement.
- **Approche individuelle (R² = 0,03) :** un client de 20 ans dépense individuellement autant qu'un client de 60 ans. **L'âge n'explique pas la dépense totale.**

### Âge vs Fréquence d'achat (R² = 0,01)
Tendance très légère : les clients plus âgés achètent légèrement plus souvent. Mais R² = 0,01 — **l'âge ne prédit pas la fréquence d'achat.**

### Âge vs Panier moyen (R² = 0,11)
Seule corrélation modérée identifiée. **L'âge a une influence sur la taille du panier moyen, mais pas sur la fréquence ni la dépense totale.**

### Âge vs Catégories — Test de Kruskal-Wallis
Différence hautement significative (p < 0.05). La Catégorie 2 est quasi-exclusive aux 18-25 ans — **seul levier de segmentation par âge réellement actionnable.**

## Synthèse des R²

| Variable | R² | Interprétation |
|----------|----|----------------|
| Âge → Dépense totale | 0.03 | L'âge n'explique rien |
| Âge → Fréquence | 0.01 | L'âge n'explique rien du tout |
| Âge → Panier moyen | 0.11 | Influence modérée, seul levier pertinent |

## Dashboard Streamlit (hors périmètre OC)

Dashboard interactif 3 pages construit sur les données du projet, avec une architecture modulaire en composants.

**Pages :**
- **KPIs** — CA, sessions, clients uniques du mois sélectionné avec delta vs mois précédent + évolution CA annuelle (moyenne mobile paramétrable)
- **Ventes** — Top/Flop 5 produits par CA, répartition par catégorie (barchart + donut)
- **Corrélations** — Tableau synthèse des tests statistiques + analyses détaillées avec graphiques et recommandations

**Filtres sidebar communs :** mois, année (2021–2023), segment BtoB/BtoC, catégories 0/1/2

**Stack :** Streamlit · Plotly · Pandas · `@st.cache_data`

| Corrélation | Méthode | Score | Force |
|-------------|---------|-------|-------|
| Genre → Catégorie | Chi² / V de Cramer | 0.007 | Aucune |
| Âge → CA global | Spearman | −0.88 | Forte |
| Âge → CA / client | Spearman | −0.18 | Faible |
| Âge → Fréquence | Spearman | +0.11 | Faible |
| Âge → Panier moyen | Spearman | −0.34 | Modérée |
| Tranche d'âge → Catégorie favorite | Chi² / V de Cramer | **0.416** | **Forte ★** |

## Storytelling

> *"La librairie pensait pouvoir segmenter par genre et par âge. Deux faux positifs à démonter : le chi² genre/catégorie semblait significatif — il l'était sur le volume, pas sur le comportement individuel. L'âge semblait prédire la dépense — c'était juste un effet de pyramide des âges dans la base. Le vrai insight : l'âge n'est pas un levier pour le panier ou la fréquence, mais la Catégorie 2 est une enclave générationnelle 18-25 ans. C'est là qu'il faut jouer."*

## Structure du projet

```
P9/
├── oc/                              ← Partie formation OC
│   ├── 01_exploration.ipynb         ← Chargement, sherlock(), feature engineering
│   ├── 02_analyses_annabelle.ipynb  ← Analyses genre & catégories
│   ├── 03_analyses_julie.ipynb      ← Analyses âge & comportement d'achat
│   └── Despont_Tristan_2_support.pptx
└── streamlit/                       ← Dashboard interactif (hors périmètre OC)
    ├── app.py                       ← Point d'entrée, navigation multi-pages
    ├── pages/
    │   ├── 1_📊_KPIs.py             ← KPIs mensuels avec delta vs mois précédent
    │   ├── 2_📈_Ventes.py           ← Top/Flop produits, répartition catégories
    │   └── 3_🔍_Correlations.py     ← Tableau synthèse + analyses détaillées
    ├── components/
    │   ├── data_loader.py           ← Chargement CSV + filtres (@st.cache_data)
    │   ├── logic.py                 ← Calcul KPIs (CA, sessions, panier moyen, deltas)
    │   ├── charts.py                ← Graphiques Plotly (CA, top/flop, corrélations)
    │   ├── sidebar.py               ← Sidebar commune (mois, année, segment, catég.)
    │   └── ui.py                    ← Rendu Streamlit des composants
    └── src/
        └── data_manager.py          ← Fonction sherlock() (EDA custom)
```

> **Note :** L'exploration utilise `sherlock()`, une fonction EDA custom développée en parallèle du parcours, importée depuis `src/data_manager`.

## Données

3 sources fusionnées (687 534 transactions) :
- `customers.csv` — 8 621 clients (client_id, sex, birth)
- `products.csv` — 3 286 produits (id_prod, price, categ)
- `Transactions.csv` — 687 534 lignes (id_prod, date, session_id, client_id)

**Features engineerées :** segmentation BtoB/BtoC (seuil CA > 50 000€), âge calculé à la date de transaction.

## Livrables

- `oc/01_exploration.ipynb` — Chargement, nettoyage, jointures, feature engineering
- `oc/02_analyses_annabelle.ipynb` — Analyses genre & catégories
- `oc/03_analyses_julie.ipynb` — Analyses âge & comportement d'achat
- `oc/Despont_Tristan_2_support.pptx` — Support de soutenance
- `streamlit/` — Dashboard interactif 3 pages (KPIs · Ventes · Corrélations)
