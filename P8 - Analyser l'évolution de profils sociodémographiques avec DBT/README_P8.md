# P8 — Analyse sociodémographique des étudiants Data avec DBT

> Projet de formation | Mars 2026

## Contexte

Analyse de l'évolution du profil sociodémographique des étudiants inscrits aux parcours Data chez **OpenClassrooms** sur la période **2022–2025**, comparé à la population française (données INSEE).

Objectif : identifier les écarts de représentation (genre, âge, région) et formuler des recommandations actionnables.

## Stack technique

![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4c8cbf?style=for-the-badge&logo=python&logoColor=white)

## Pipeline DBT — Architecture en couches

```mermaid
flowchart LR
    A[📥 Raw\nDonnées brutes OC + INSEE] --> B[🧹 Staging\nNettoyage & harmonisation]
    B --> C[🔗 Intermediate\nAgrégations par dimension\nrégion · sexe · âge · année]
    C --> D[📊 Mart\nCSV livrable final]
```

Les modèles DBT et le data warehouse Snowflake ne sont pas versionnés ici (données sensibles + environnement cloud). Seuls le CSV de sortie et le notebook de visualisation sont disponibles.

## Traitement des données

**Sources :** données internes OC (inscriptions) + données publiques INSEE (population française).

**Nettoyage OC :** valeurs nulles de genre remplacées par `NC` (Non Communiqué), exclus des comparaisons via RIGHT JOIN.

**Nettoyage INSEE :** pré-traitement Python pour convertir le format Excel multi-index en format compatible Snowflake — harmonisation des noms de régions, agrégation des tranches 60+ en une seule catégorie, reformatage des tranches d'âge pour alignement des deux sources.

**Jointures :** agrégation séparée OC et INSEE en deux CTEs avant jointure — évite le double comptage.

## Résultats clés

| Dimension | Écart OC vs France |
|-----------|-------------------|
| **Région** | Île-de-France sur-représentée de **+27,7 pts**, toutes autres régions déficitaires |
| **Genre** | 69% d'hommes chez OC vs 48% en France → **-20 pts sur les femmes** |
| **Âge** | Pic sur les 30-34 ans (**+17,7 pts**) — profil reconversion professionnelle |
| **Inscriptions** | Pic 2022 (~1700), baisse de **-44%** jusqu'en 2024, reprise 2025 (~950) |

## Conformité RGPD

Données agrégées uniquement (tranche d'âge, genre, région) — risque de ré-identification très faible. Hébergement Snowflake région EU-Paris. En contexte production : DPA Snowflake, chiffrement, RBAC, anonymisation dès le staging.

## Storytelling

> *"Le profil type étudiant OC Data : un homme de 30-34 ans francilien. Mais derrière ce portrait, trois leviers de croissance : féminisation (20 points d'écart), décentralisation (IDF sur-représentée de +27 points), et les 20-24 ans quasi absents. La baisse de -44% des inscriptions entre 2022 et 2024 interroge — effet post-covid ? Saturation du marché ? La reprise 2025 est encourageante mais 4 ans d'historique ne suffisent pas à trancher."*

## Livrables

- `Despont_Tristan_1_fichier` — CSV de sortie du pipeline (données agrégées OC × INSEE)
- `graph.ipynb` — Notebook de visualisation des écarts sociodémographiques
- `Despont_Tristan_3_presentation` — Support de soutenance
