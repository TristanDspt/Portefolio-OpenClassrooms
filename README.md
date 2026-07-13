# Formation Data Analyst — Portfolio de projets

> Tristan Despont | Reconversion professionnelle | 2025–2026

Ce repo regroupe l'ensemble des projets réalisés dans le cadre de ma formation Data Analyst, du SQL fondamental jusqu'au machine learning, en passant par Python, Power BI et DBT.

---

## Projets

| # | Projet | Stack | Date |
|---|--------|-------|------|
| [P3](#p3) | Requêter une base de données avec SQL | PostgreSQL · DBeaver · Power Architect | 12/2025 |
| [P5](#p5) | Base de données immobilière avec SQL | PostgreSQL · DBeaver · Power Architect | 01/2026 |
| [P4](#p4) | Étude de santé publique avec Python | Python · Pandas · Matplotlib · Seaborn · Jupyter | 01/2026 |
| [P6](#p6) | Optimisation gestion des données d'une boutique | Python · Pandas · NumPy · Plotly · Jupyter | 02/2026 |
| [P7](#p7) | Tableau de bord dynamique Power BI — Sanitoral | Power BI · Power Query · Excel | 02/2026 |
| [P8](#p8) | Analyse sociodémographique avec DBT | Snowflake · dbt · Python · Pandas · Seaborn | 03/2026 |
| [P9](#p9) | Analyse des ventes d'une librairie + Dashboard | Python · SciPy · Streamlit · Plotly · Jupyter | 03/2026 |
| [Stage](#stage) | Analyse financière T&S Lodge | Python · Pandas · Plotly · Jupyter | 04–05/2026 |
| [P10](#p10) | Tableau de bord accès à l'eau potable — DWFA | Power BI · Python · Pandas | 06/2026 |
| [P11](#p11) | Étude de marché export avec Python — La Poule qui Chante | Python · Scikit-learn · Pandas · Jupyter | 06/2026 |
| [P12](#p12) | *(à venir)* | — | — |

---

## P3
### Requêter une base de données avec SQL
**12/2025** · [Voir le dossier](./P03%20-%20Requêter%20une%20BDD%20SQL/)

Projet d'entraînement aux fondamentaux SQL sur des données fictives d'une compagnie d'assurance habitation (~30 000 contrats). Modélisation relationnelle, création et chargement de la BDD, contrôle qualité, 12 requêtes SQL.

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![DBeaver](https://img.shields.io/badge/DBeaver-382923?style=flat-square&logo=dbeaver&logoColor=white)

---

## P5
### Création et utilisation d'une base de données immobilière — DATAImmo
**01/2026** · [Voir le dossier](./P05%20-%20Création%20et%20utilisation%20d'une%20base%20de%20données%20immobilière%20avec%20SQL/)

Modélisation complète MCD → MLD → MPD pour Laplace Immo. BDD PostgreSQL de 7 tables (34k+ transactions), 12 requêtes SQL avancées dont window functions (`RANK() OVER PARTITION BY`), conformité RGPD.

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![DBeaver](https://img.shields.io/badge/DBeaver-382923?style=flat-square&logo=dbeaver&logoColor=white)

---

## P4
### Étude de santé publique avec Python — FAO
**01/2026** · [Voir le dossier](./P04%20-%20Etude%20de%20santé%20publique%20en%20Python/)

Analyse de la disponibilité alimentaire mondiale et de la sous-nutrition à partir des données FAO (2013–2017). Zoom cas concret sur le manioc en Thaïlande.

> *La production mondiale couvre 126% des besoins caloriques. La faim est un problème de répartition, pas de production.*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

---

## P6
### Optimisation de la gestion des données d'une boutique — Bottleneck
**02/2026** · [Voir le dossier](./P06%20-%20Optimiser%20la%20gestion%20des%20données%20d'une%20boutique%20avec%20Python/)

Consolidation de 3 sources hétérogènes (ERP, web, table de liaison) pour un caviste en ligne. Nettoyage, jointures, analyses univariées, corrélations, indicateurs métier (CA, taux de marge, Pareto, Gini).

> *61% des références portent 80% du CA — catalogue résilient. Mais 277k€ immobilisés en stock et une corrélation prix/ventes de -0.52 à surveiller.*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)

---

## P7
### Tableau de bord dynamique Power BI — Sanitoral
**02/2026** · [Voir le dossier](./P07%20-%20Créer%20un%20tableau%20de%20bord%20dynamique%20avec%20Power%20BI/)

Dashboard 8 vues pour piloter 104 projets mondiaux (retard, coût, livrables, Gantt). Démarche PSC avant implémentation, modèle en étoile, filtres croisés persistants.

> *31% de projets en alerte — mais en creusant : les retards s'améliorent, les livrables sont à zéro déficit. Le vrai problème est uniquement budgétaire.*

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Power Query](https://img.shields.io/badge/Power%20Query-217346?style=flat-square&logo=microsoft-excel&logoColor=white)

---

## P8
### Analyse sociodémographique avec DBT — OpenClassrooms
**03/2026** · [Voir le dossier](./P08%20-%20Analyser%20l'évolution%20de%20profils%20sociodémographiques%20avec%20DBT/)

Pipeline DBT (Raw → Staging → Intermediate → Mart) sur Snowflake. Analyse des étudiants Data OC vs population INSEE sur 4 ans. Prétraitement Python du format Excel multi-index INSEE.

> *Profil type : homme 30-34 ans francilien. Trois leviers identifiés : féminisation (-20pts vs France), décentralisation (+27pts IDF), jeunes 20-24 ans quasi absents.*

![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=flat-square&logo=snowflake&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=flat-square&logo=dbt&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

---

## P9
### Analyse des ventes d'une librairie + Dashboard Streamlit
**03/2026** · [Voir le dossier](./P09%20-%20Analyser%20les%20ventes%20d'une%20librairie%20avec%20Python/)

Analyses statistiques (chi², Spearman, Kruskal-Wallis) sur 687k transactions. Démystification de deux faux positifs statistiques. Dashboard Streamlit 3 pages avec architecture modulaire en composants.

> *L'âge ne prédit ni la dépense ni la fréquence (R²≈0). Seule la Catégorie 2 est une enclave générationnelle 18-25 ans — c'est là qu'il faut jouer.*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)

---

## Stage
### Analyse financière T&S Lodge
**04–05/2026** · [Voir le dossier](./Stage%20-%20T%26S%20Lodge/)

*Données partagées avec l'accord explicite des co-gérants.*

Stage d'un mois chez T&S Lodge, gîte en Indre (36) en vue d'une mise en vente. Analyse complète sur 18 mois d'exploitation : CA, charges, cash-flow, taux d'occupation, saisonnalité, croisement comptabilité × Airbnb, prévisionnel cible.

> *Premier exercice rentable en 2025 (+4 117€ CF), taux d'occupation 50% sur un gîte de 18 mois en zone rurale. Cible prévisionnel 19 635€ — conservative et atteignable.*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)

---

## P10
### Tableau de bord accès à l'eau potable — DWFA
**06/2026** · [Voir le dossier](./P10%20-%20Etude%20sur%20l'eau%20potable/)

Dashboard Power BI 3 vues (Monde / Continent / Pays) pour identifier les pays prioritaires d'une ONG. Prétraitement Python, blueprint de conception, indicateur composite d'efficacité gouvernementale.

> *84% d'accès mondial — mais l'Afrique est à 32% de safely managed. Le dashboard permet d'identifier en un clic où investir selon le domaine d'intervention.*

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

---

## P11
### Étude de marché export avec Python — La Poule qui Chante
**06/2026** · [Voir le dossier](./P11%20-%20Etude%20de%20marché%20avec%20Python)

Analyse de 131 pays (FAO + Banque Mondiale) pour identifier les meilleurs marchés à l'export pour un producteur de volailles bio. ACP (85% variance en 5 composantes), double clustering CAH + K-Means (K=4), scoring composite des 37 pays cibles.

> *Sur 131 pays, un seul cluster réunit toutes les conditions : riche, importateur, business-friendly. 37 pays. Podium : Japon · Allemagne · Émirats. Le clustering ne ment pas.*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

---

## P12
### *(à venir)*

---

## À propos

Reconversion professionnelle vers le Data Analyst / Dev IA.  
Parcours OpenClassrooms — Formation Data Analyst.

Tous les projets de formation sont réalisés dans le cadre du parcours OC. Les données du stage T&S Lodge sont partagées avec l'accord explicite des co-gérants du gîte.
