# P13 — Piloter un projet data augmenté avec l'IA — BottleNeck (suite P6)

> Projet de formation | Juin 2026

## Contexte

Projet en deux parties :
- **Partie 1** : Amélioration du livrable P6 (analyse BottleNeck) par une approche ML non supervisé, documentée et critique, avec usage encadré de l'IA.
- **Partie 2** : Réalisation du portfolio professionnel — ce repo GitHub.

## Stack technique

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

## Partie 1 — Segmentation du catalogue BottleNeck par clustering

### Problématique métier

> *« Tous les produits du catalogue ne se valent pas. Peut-on les regrouper automatiquement en familles cohérentes — selon leur positionnement, leur volume de ventes, leur ancienneté et leur rotation de stock — afin d'orienter les décisions d'assortiment, de pricing et de gestion de stock ? »*

Le P6 produisait une analyse **variable par variable**. Le P13 passe à une segmentation **multivariée et data-driven** : c'est l'algorithme qui révèle les groupes, l'analyste qui les interprète et les nomme.

### Démarche

#### Isolement des régimes particuliers (avant ML)

Les cas hors-régime sont sortis par règle métier **avant** le clustering — ne pas demander à l'algorithme de deviner des états qualitatifs distincts.

| Règle | Volume |
|-------|--------|
| Invendus (`total_sales == 0`) | 25 produits |
| → Cœur de catalogue (clustering) | 689 produits |

#### Comparaison de deux variantes de segmentation

| | Variante A — 3 axes | Variante B — 4 axes |
|---|---|---|
| Variables | prix, ventes, ancienneté | prix, ventes, ancienneté, **rotation de stock** |
| Meilleure silhouette KMeans | **0,400** (k=3) | 0,387 (k=3) |
| k=4 viable ? | Non (chute à 0,333) | Oui (0,375) |

**Arbitrage multi-critères :**

| Critère | Favorise | Commentaire |
|---------|----------|-------------|
| Netteté statistique (silhouette) | Variante A | 0,400 > 0,387 |
| Parcimonie / reproductibilité | Variante A | Moins d'axes |
| **Valeur métier** | **Variante B** | Révèle 32 produits à stock dormant — invisibles dans A |

**Décision : Variante B (4 axes, k=4)** — perte marginale de netteté statistique (−0,013) contre un gain franc de valeur métier. *L'actionnabilité prime sur la netteté.*

#### Quatre segments métier

| Segment | Volume | Profil clé | Action |
|---------|--------|-----------|--------|
| **Moteur de CA** | 326 | Prix 15€ · ventes 10 · ancien | Sécuriser la disponibilité |
| **Nouveautés performantes** | 142 | Prix 24€ · récent (446j) | Accélérer la mise en avant |
| **Premium** | 188 | Prix 50€ · rotation lente assumée | Piloter par le stock |
| **Stock dormant** | 32 | Prix 61€ · **16,5 mois de stock** · marge 40% | Déstocker en priorité |

> Le segment *Stock dormant* était **invisible** dans une segmentation prix/ventes seule — c'est l'ajout de la rotation de stock qui le révèle.

### Choix techniques documentés

- **`log1p`** appliqué à `price`, `total_sales`, `stock_mois` (asymétrie à droite) — pas à `anciennete` (asymétrie à gauche)
- **`StandardScaler`** sur toutes les variables — KMeans raisonne en distances
- **Exclusion explicite** de `ca` et `price_zscore` des features (data leakage)
- **`tx_marge`** conservée en lecture seule uniquement — quasi-plate (75% des produits entre 56,6% et 66,3%)
- **KMeans retenu** vs Agglomératif (meilleure silhouette à tous les k) — DBSCAN écarté (paramétrage inadapté)
- **Données source en Parquet** — types préservés, portable, préféré au pickle
- **`random_state=42`** + ancienneté ancrée sur `post_date.max()` (pas la date d'exécution)

### Usage de l'IA

Mobilisée comme outil de travail critique : brainstorming d'axes, aide au code, relecture méthodologique. Chaque suggestion soumise à validation — plusieurs écartées (piste prévision temporelle, détection d'anomalies, cadre stratégique non maîtrisé). Les décisions finales relèvent d'un jugement métier et statistique **assumé par l'auteur**.

### Veille technologique

| Solution | Décision |
|----------|----------|
| **KMeans** | ✅ Retenu |
| Clustering hiérarchique (Ward) | Comparé — témoin de robustesse |
| DBSCAN | Écarté — paramétrage inadapté |
| **Pandera** | Piste retenue pour industrialisation future |
| Great Expectations | Écarté — surdimensionné pour un notebook |

---

## Partie 2 — Portfolio professionnel

Ce repo GitHub constitue le livrable de la partie 2.

---

## Livrables

- `p6_extended.ipynb` — Notebook de segmentation (amélioration du P6)
- `df_merge.parquet` — Export consolidé du P6 (source de travail)
- `documentation.md` — Documentation complète de la démarche (cahier des charges, veille, hypothèses, décisions, pilotage, registre des risques)
