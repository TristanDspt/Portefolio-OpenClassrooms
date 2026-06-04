# P3 — Requêter une base de données avec SQL

> Projet de formation | Décembre 2025

## Contexte

Projet d'entraînement aux fondamentaux SQL dans le cadre d'une formation Data Analyst.  
Données fictives d'une compagnie d'assurance habitation (~30 000 contrats couvrant l'ensemble du territoire français).

## Objectifs

- Modéliser une base de données relationnelle à partir de fichiers CSV bruts
- Créer et charger la BDD sur PostgreSQL
- Assurer la qualité et l'intégrité des données
- Répondre à des questions métier via des requêtes SQL

## Stack technique

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![DBeaver](https://img.shields.io/badge/DBeaver-382923?style=for-the-badge&logo=dbeaver&logoColor=white)
![Power Architect](https://img.shields.io/badge/Power%20Architect-FF6B35?style=for-the-badge&logo=databricks&logoColor=white)

## Démarche

### 1. Modélisation
- Exploration des CSV et création du dictionnaire des données
- Conception du schéma relationnel (2 tables : `Contrat` et `Region`)
- Génération du script SQL de création des tables avec contraintes et clés étrangères

### 2. Chargement
- Création de la BDD sur PostgreSQL
- Import des données : **30 335 lignes** (Contrat) et **38 916 lignes** (Region)

### 3. Contrôle qualité
- Détection de 9 lignes orphelines via `LEFT JOIN` (codes commune sans correspondance)
- Identification des communes concernées (Saint-Paul et Saint-Benoît, La Réunion — dep. 974)
- Correction des clés étrangères incohérentes

### 4. Analyse SQL
12 requêtes couvrant les cas d'usage courants :

| # | Objectif | Concepts utilisés |
|---|----------|-------------------|
| 1-2 | Filtrage et valeurs distinctes | `WHERE`, `DISTINCT` |
| 3-4 | Comptage et tri | `COUNT`, `ORDER BY`, `LIMIT` |
| 5-6 | Agrégats | `AVG`, `ROUND`, `GROUP BY` |
| 7-8 | Jointures multi-conditions | `INNER JOIN`, filtres combinés |
| 9-10 | Agrégats sur jointures | `AVG` + `JOIN` + `GROUP BY` |
| 11-12 | Filtrage sur agrégats | `HAVING`, `RIGHT JOIN` |

## Livrables

- `Despont_Tristan_1_document_technique` — dictionnaire des données + schéma relationnel
- `Despont_Tristan_2_liste` — liste complète des 12 requêtes et résultats
- `Despont_Tristan_3_methodologie` — support de présentation de la démarche
- `Despont_Tristan_4_grille` — grille d'autoévaluation
