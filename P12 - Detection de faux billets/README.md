# P12 — Détection automatique de faux billets — ONCFM

> Projet de formation | Juin 2026

## Contexte

Mission pour l'**ONCFM** (Organisation nationale de lutte contre le faux-monnayage). Objectif : construire un algorithme capable de classifier automatiquement un billet — vrai ou faux — à partir de ses seules dimensions géométriques, et le livrer sous forme d'un **script de production utilisable directement par les équipes**.

Dataset : 1 500 billets labellisés (1 000 vrais / 500 faux), 6 variables géométriques.

## Stack technique

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

## Variables

| Variable | Description |
|----------|-------------|
| `diagonal` | Diagonale du billet (mm) |
| `height_left` | Hauteur côté gauche (mm) |
| `height_right` | Hauteur côté droit (mm) |
| `margin_up` | Marge bord supérieur (mm) |
| `margin_low` | Marge bord inférieur (mm) — 37 NaN (2,47%) |
| `length` | Longueur du billet (mm) |

## Démarche

### 1. Exploration
- Audit `sherlock()` : 1 500 lignes, 7 colonnes, 0 doublon, 37 NaN sur `margin_low`
- Variables les plus discriminantes : **`length`** et **`margin_low`** (distributions quasi non chevauchantes)
- `diagonal` quasi inutile (distributions superposées) — conservée dans le pipeline pour simplicité

### 2. Preprocessing
- **StandardScaler** appliqué avant imputation — variables à échelles très différentes (diagonal ~171mm vs margin_low ~4mm)
- **KNNImputer** (k=5) pour les 37 valeurs manquantes — choisi car les NaN sont distribués aléatoirement (pas de lien avec le statut du billet)
- Scaler et imputer fittés **uniquement sur le train** → appliqués sans refit sur le test (pas de data leakage)
- Les deux objets sauvegardés en `.pkl` pour réutilisation en production

### 3. Stratégie de modélisation
- Split 80/20 stratifié (random_state=42)
- **Métrique cible : Recall** — choix métier : un faux billet non détecté (FN) est bien plus grave qu'un vrai billet bloqué (FP)
- GridSearchCV 5-fold sur le train pour chaque modèle
- Fonction `evaluate_model()` : matrice de confusion + courbe ROC automatiques

### 4. Comparaison des 4 modèles

| Modèle | Recall | AUC | FN | FP |
|--------|--------|-----|----|----|
| Régression Logistique | 96% | 0.9990 | 4 | 0 |
| KNN | 97% | 0.9825 | 3 | 1 |
| **Random Forest** ✅ | **98%** | **0.9997** | **2** | **2** |
| K-Means | instable* | — | — | — |

*K-Means : 97% sur seed=42, 3% sur seed=10 — instabilité fondamentale liée à l'initialisation aléatoire → **écarté d'emblée pour la production**.

**Modèle retenu : Random Forest** — meilleur recall (98%), meilleure AUC (0,9997), stable sur deux seeds différents, max_depth=2 cohérent avec la séparabilité quasi-linéaire des données.

### 5. Script de production

```bash
# Mode CSV (déposer un fichier dans data/fresh/)
python app.py

# Mode valeurs directes
python app.py --values 171.81 104.86 104.95 3.07 6.28 112.83
```

Sortie :
```
==================================================
   ONCFM - Résultats de l'analyse
==================================================
  Billet   1 | Vrai billet ✅
  Billet   2 | FAUX BILLET ⚠️
==================================================
  Total analysés : 2
  Faux détectés  : 1
  Vrais          : 1
==================================================
```

Pipeline en production : `scaler.pkl` → `imputer.pkl` → `RF.pkl` — garantit que la transformation est exactement la même qu'à l'entraînement.

## Storytelling

> *"Le Random Forest détecte 98% des faux billets — 2 faux négatifs sur 100, contre 4 pour la régression logistique. Ce n'est pas qu'une question de performance : c'est un choix métier. Pour l'ONCFM, un faux billet qui circule est un scandale ; un vrai billet bloqué est juste un contrôle manuel de plus. Le K-Means ? Écarté immédiatement — 97% sur un seed, 3% sur un autre. Un algorithme dont le résultat dépend du hasard n'a pas sa place en production."*

## Livrables

- `app.py` — Script CLI de production (deux modes : valeurs directes ou CSV)
- `models/RF.pkl` — Modèle Random Forest sérialisé
- `models/scaler.pkl` — StandardScaler sérialisé
- `models/imputer.pkl` — KNNImputer sérialisé
- `01_explo_billets.ipynb` — Exploration & preprocessing
- `02_LR.ipynb` — Régression Logistique
- `03_KNN.ipynb` — K-Nearest Neighbors
- `04_RF.ipynb` — Random Forest
- `05_KMeans.ipynb` — K-Means
- `despont_tristan_presentation_06_2026.pptx` — Support de soutenance
- `cahier_des_charges.pdf` — Cahier des charges ONCFM
