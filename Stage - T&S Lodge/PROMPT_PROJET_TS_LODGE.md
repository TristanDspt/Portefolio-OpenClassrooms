# PROMPT PROJET — TS Lodge / Stage Data Analyst

## Contexte général

Stage d'un mois (13 avril → 13 mai 2025) chez **T&S Lodge**, gîte unique géré par **Sarah Blondel** et **Bernard Moizan** (co-gérants), situé au **330 route de Nouans, 36600 Villentrois-Faverolles-en-Berry** (Indre), à ~15 km du Zoo de Beauval.

**Mission** : analyser la performance du gîte et son potentiel de valorisation **en vue d'une mise en vente**. L'analyse viendra appuyer l'estimation réalisée par le cabinet comptable.

---

## Historique du bien

| Étape | Date |
|---|---|
| Acquisition | 24 février 2024 |
| Rénovation complète | février → juillet 2024 |
| Création société (registre) | mai 2024 |
| Premiers clients | 20 juillet 2024 |
| Changement modèle (ménage/linge retirés) | janvier 2026 |

**Régime fiscal : LMNP (Location Meublée Non Professionnelle)**
- Stratégie délibérément déficitaire pour optimiser la fiscalité
- Seuil de CA volontairement maintenu **sous 23 000€/an** (pour garder le statut LMNP et éviter la TVA)
- Aucune démarche d'optimisation commerciale n'a été engagée — **le gîte a tourné en dessous de son potentiel réel**
- ⚠️ L'analyse doit donc distinguer : performance réelle actuelle vs potentiel si optimisé

---

## Contacts

| Rôle | Nom | Téléphone | Email |
|---|---|---|---|
| Propriétaire / gérante | Sarah Blondel | 06 50 99 14 02 | blondelsarah41@gmail.com |
| Co-gérant | Bernard Moizan | 06 63 03 18 41 | bernard.moizan@enedis.fr |
| Comptable | Élodie Gresle (Axescibles) | 06 72 46 00 60 | elodie.gresle@axescibles.fr |
| Contact général | — | — | tslodge@tslodge.net |

---

## Données disponibles

### Comptabilité

| Fichier | Contenu | Période | Encodage |
|---|---|---|---|
| `2BLONDEL.csv` | Journal comptable PCG | mai → déc 2024 | latin-1, sep `;`, decimal `,` |
| `2BLONDEL_2025.csv` | Journal comptable PCG | jan → déc 2025 | cp850, sep `;`, decimal `,` |

- Codes journaux : `ACH` (achats), `BQ` (banque), `OD` (opérations diverses), `AC` (honoraires comptable)
- **Bilan 2025** — en cours de préparation par Élodie Gresle, attendu début de stage

### Éléments comptables clés identifiés (2024)

| Élément | Détail |
|---|---|
| Achat bien | 64 500€ bâtiment + 27 030€ terrain |
| Prêt immo | 92 515€ — échéance mai 2039 |
| Remboursement mensuel | ~753€ capital |
| Assurance Thelem | 32,87€/mois |
| Box Orange | 25,99€/mois |
| Achat cuisine | ~286€ — achat en fonds propres pour le gîte, pas un crédit |
| Commissions Airbnb 2024 | 299,74€ |
| IK (indemnités km) | 3 464€ sur l'année |
| Plateformes de revenus | Airbnb + Booking.com + virements directs |
| Entrées AC | Honoraires comptable Axescibles (base + TVA) — ne pas confondre avec ACH |

### Données Airbnb

| Fichier | Contenu | Période | Granularité |
|---|---|---|---|
| `consultations_janvier2026.xlsx` | Consultations + réservations + taux de conversion | juil 2024 → fév 2026 | Mensuelle (synthèse utilisée) |

- Données Booking.com et Gîtes de France : **non disponibles** — mentionner comme limite dans le rapport

### Données publiques (bonus si temps)
- INSEE (fréquentation touristique locale)
- Données marché / benchmark concurrence locale

---

## Offre & positionnement du gîte

- Environnement : vue sur étang, village, nature — tourisme vert/familial/œnologique
- Proximité Zoo de Beauval (~15 min) — fort levier de fréquentation
- Capacité : chambre principale (140×200) + grande chambre (3-4 lits 90×190) + canapé-lit (160×200) + lit parapluie
- Services optionnels : location linge (8,50€→11€/parure), forfait ménage (75€)
- Équipements extérieurs : jeux, tir à l'arc, barbecues, bains de soleil, cave troglodyte, vélos, prise VE
- **Jusqu'en janvier 2026** : ménage + linge inclus → retirés ensuite **sans ajustement tarifaire** (piste d'analyse)

### Potentiel de développement (argument de valorisation)
- 5 000 m² dont 2 000 m² exploitables
- Infrastructures (eau, élec, assainissement) déjà anticipées pour hébergements supplémentaires
- 3 projets possibles : gîte supplémentaire / hébergement insolite / gîte troglodyte
- Autorisation d'exploitation déjà obtenue (de plus en plus rare)
- Terrain voisin non constructible → pas de voisinage futur garanti

---

## User Stories

### US1 — Mesurer la performance actuelle
> En tant que propriétaire, je veux connaître la performance réelle du gîte (CA, charges, taux d'occupation, saisonnalité) pour disposer d'une base factuelle solide.

### US2 — Identifier les leviers de marge
> En tant que propriétaire, je veux identifier ce qui peut être optimisé (canaux, tarifs, charges) pour montrer le potentiel non exploité du gîte.

### US3 — Produire un prévisionnel pour le repreneur
> En tant que propriétaire, je veux disposer d'un prévisionnel de CA réaliste sur 2-3 ans, basé sur les données réelles et les hypothèses d'optimisation identifiées, à destination du repreneur et de la comptable — **pour favoriser la vente au meilleur prix**.
>
> ⚠️ La valorisation du bien reste du ressort de la comptable (Axescibles). Notre livrable = la matière première chiffrée.

---

## Objectifs & livrables

### Dans le scope
- Nettoyage + exploration des CSV comptables (2024 + 2025)
- KPIs clés : CA, charges, cash-flow, saisonnalité
- Analyse Airbnb : consultations, réservations, taux de conversion (mensuel)
- Croisement comptabilité × Airbnb
- Prévisionnel de CA 2-3 ans (scénario réaliste optimisé)
- **Rapport d'analyse structuré en Word** — livrable principal

### Bonus si temps
- Benchmark concurrence (annonces publiques)
- Dashboard Streamlit

### Hors scope
- Estimation du prix de vente du bien → comptable
- Scénarios de valorisation poussés (DCF, multiples) → comptable
- Données Booking / Gîtes de France → non disponibles

---

## Stack technique

- **Python / pandas / numpy** — exploration et analyse
- **VS Code + Jupyter** — notebooks d'exploration
- **Matplotlib / Seaborn / Plotly** — visualisation
- **PostgreSQL / DBeaver** — si mise en base nécessaire
- **Streamlit** — dashboard (bonus)
- Venv dédié au projet

---

## Mode de travail

- **MVP first** — on finit un truc avant d'en commencer un autre
- Un fil Claude par feature, ce fil = chef de projet / suivi global
- Réponses directes, pas de chichi
- Contexte pro : aide directe sur le code, pas de mode pédagogique

---

## Roadmap

| Semaine | Focus |
|---|---|
| S1 | Nettoyage + exploration CSV comptable 2024 & 2025 — KPIs de base |
| S2 | Analyse Airbnb + croisement comptabilité × OTA |
| S3 | Prévisionnel + rapport structuré |
| S4 | Finalisation rapport + bonus (benchmark, dashboard) |

---

## Contraintes & contexte humain

- Co-gestion Sarah / Bernard (situation personnelle délicate) — **rester 100% factuel, laisser les chiffres parler, zéro prise de position**
- Le cabinet comptable fait l'estimation du bien — notre analyse vient en **appui**, pas en substitution
- 1 mois de stage — prioriser rapport, dashboard en bonus

---

## Points en suspens

- [ ] Benchmark concurrence si temps disponible

---

*Dernière mise à jour : 10 avril 2025*
