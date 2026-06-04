# P4 — Étude de santé publique avec Python

> Projet de formation | Janvier 2026

## Contexte

Mission d'analyse pour la FAO (Organisation des Nations Unies pour l'alimentation et l'agriculture) sur l'état de la sous-nutrition mondiale en 2017.  
Données issues de 4 datasets FAO : population mondiale, disponibilité alimentaire, aide alimentaire et sous-nutrition.

## Objectifs

- Quantifier la proportion de personnes en état de sous-nutrition dans le monde
- Évaluer le potentiel nourricier de la production mondiale (globale et végétale)
- Analyser la répartition de la disponibilité alimentaire intérieure
- Identifier les pays les plus touchés et les plus bénéficiaires de l'aide alimentaire
- Réaliser un zoom analytique sur le manioc en Thaïlande comme cas d'étude concret

## Stack technique

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4c8cbf?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

## Démarche

### 1. Exploration & nettoyage
- Analyse exploratoire des 4 datasets (types, dimensions, valeurs manquantes)
- Harmonisation des unités (milliers de tonnes → kg, millions → unités réelles)
- Gestion des anomalies FAO : détection des pays majeurs avec données plafonnées (Chine, USA, Russie)

### 2. Analyses thématiques

| # | Analyse | Insight clé |
|---|---------|-------------|
| 1 | Proportion de sous-nutrition mondiale | 7,1% de la population mondiale — 536M de personnes |
| 2 | Potentiel nourricier de la production | La production couvre **126%** des besoins mondiaux |
| 3 | Potentiel avec végétaux seuls | Les végétaux seuls couvrent **104%** des besoins |
| 4 | Répartition de la disponibilité intérieure | 49% pour l'alimentation humaine, 22% agro-alimentaire |
| 5 | Utilisation des céréales | 36% part aux animaux, seulement 43% aux humains |
| 6 | Top 10 pays en sous-nutrition | Haïti & Corée du Nord : 1 habitant sur 2 |
| 7-8 | Aide alimentaire 2013-2016 | Syrie, Éthiopie, Yémen = 40% de l'aide mondiale |
| 9-10 | Disparités caloriques | Écart de +61% entre pays riches et seuil de besoin |

### 3. Zoom cas d'étude — Manioc en Thaïlande
- La Thaïlande exporte **83%** de sa production de manioc (1er exportateur mondial avec 70% des exports)
- Le manioc exporté pourrait nourrir **35 millions de personnes** par an
- **92%** du manioc importé par la Chine est utilisé à des fins non alimentaires (animaux + industrie)
- Paradoxe : 6,2M de Thaïlandais en sous-nutrition, pendant que le pays exporte l'équivalent de 51% de ses besoins caloriques

### 4. Conclusion analytique

> *"La production alimentaire mondiale permettrait de nourrir 9,5 milliards de personnes — soit 126% des besoins. Les végétaux seuls suffiraient à couvrir 104%. Le problème n'est donc pas la production, mais la répartition, l'usage et l'accès aux ressources. L'étude de cas Thaïlande/manioc l'illustre concrètement : un pays qui exporte 70% des exportations mondiales de manioc tout en ayant 9% de sa population en sous-nutrition."*

## Livrables

- `Tristan_Despont_1_notebook` — Notebook Jupyter complet (exploration, nettoyage, analyses, visualisations)
- `Tristan_Despont_2_notebook-pdf` — Export PDF du notebook
- `Tristan_Despont_3_presentation` — Support de présentation de la soutenance
