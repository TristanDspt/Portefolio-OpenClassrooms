# P5 — Création et utilisation d'une base de données immobilière avec SQL

> Projet de formation | Janvier 2026

## Contexte

Mission pour **Laplace Immo**, réseau national d'agences immobilières, dans le cadre du projet **DATAImmo**.  
Objectif : concevoir et alimenter une base de données de transactions immobilières françaises pour alimenter un futur modèle de prédiction des prix.

Sources de données : DVF (Demandes de Valeurs Foncières, opendata), INSEE (recensement), data.gouv (référentiel géographique France + DROM-COM).

## Stack technique

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![DBeaver](https://img.shields.io/badge/DBeaver-382923?style=for-the-badge&logo=dbeaver&logoColor=white)
![Power Architect](https://img.shields.io/badge/Power%20Architect-FF6B35?style=for-the-badge&logo=databricks&logoColor=white)

## Démarche

### 1. Analyse & nettoyage des données
- Identification des colonnes inutiles (entièrement vides, hors périmètre métier, non conformes RGPD)
- Suppression des données personnelles (nom des acquéreurs) — conformité RGPD
- Minimisation des données : seules les variables utiles à la prédiction des prix sont conservées

### 2. Modélisation
- **MCD** — Modèle Conceptuel des Données : identification des entités et associations
- **MLD** — Modèle Logique : schéma relationnel normalisé (3NF) sous Power Architect
- **MPD** — Modèle Physique : script SQL généré avec index sur les clés étrangères pour optimiser les jointures
- **Dictionnaire des données** : 1 feuille par table, avec types, contraintes et règles de gestion

### 3. Création & chargement de la BDD

7 tables créées sous PostgreSQL :

| Table | Lignes |
|-------|--------|
| commune | 34 991 |
| département | 109 |
| région | 19 |
| type_local | 2 |
| type_voie | 80 |
| bien | 34 169 |
| mutation | 34 151 |

Choix documenté : exclusion des mutations à valeur foncière nulle.

### 4. Requêtes SQL d'analyse du marché immobilier

12 requêtes couvrant un spectre avancé :

| # | Analyse | Concept SQL |
|---|---------|-------------|
| 1 | Appartements vendus au S1 2020 | `COUNT` + `INNER JOIN` multi-tables |
| 2 | Ventes par région | `GROUP BY` + `ORDER BY` |
| 3 | Proportion par nombre de pièces | Sous-requête pour calcul de % |
| 4 | Top 10 départements prix/m² | `AVG` + `ROUND` + `LIMIT` |
| 5 | Prix moyen maison en Île-de-France | `JOIN` 5 tables + filtre région |
| 6 | Top 10 appartements les plus chers | Jointures multi-niveaux |
| 7 | Évolution ventes T1 → T2 2020 | `WITH` (CTE) + calcul de taux |
| 8 | Classement régions prix/m² > 4 pièces | Agrégation multi-critères |
| 9 | Communes avec ≥ 50 ventes au T1 | `HAVING` |
| 10 | Écart prix/m² 2 pièces vs 3 pièces | `WITH` (double CTE) |
| 11 | Top 3 communes par département (6, 13, 33, 59, 69) | `RANK() OVER (PARTITION BY...)` |
| 12 | Transactions pour 1000 habitants | Ratio population + `LIMIT 20` |

### 5. Conformité RGPD
Analyse structurée des 5 principes appliqués au projet : cartographie, minimisation, information/consentement, sécurité, désignation d'un DPO.

## Livrables

- `DESPONT_Tristan_1_dictionnaire_de_donnees` — Dictionnaire des données (Excel, 1 feuille par table)
- `DESPONT_Tristan_2_support_presentation` — Support de soutenance (MCD, MLD, MPD, requêtes et résultats)
