# 📜 Les Papyrus de Héron

> *L’ordre naît de l’algorithme.*

---

## 🧠 Contexte du projet

Dans les couloirs majestueux de la Bibliothèque d'Alexandrie, l’érudit Héron est confronté à un problème inattendu : des milliers de papyrus sont en désordre ! Pour l’aider à restaurer le savoir antique, nous avons développé un outil de tri algorithmique, capable de trier des listes de valeurs selon 7 algorithmes classiques.

Ce projet mêle **algorithmique**, **visualisation graphique** et **analyse de performances** pour offrir une solution aussi scientifique qu’artistique.

---

## 📂 Structure du dépôt

```
sorting-algorithms/
│
├── sorting.py           # Implémentations des 7 tris classiques
├── main.py              # Interface utilisateur en ligne de commande
├── graphical.py         # Interface Pygame avec menu et logo
├── visuals/             # 📦 Visualisation POO (1 classe = 1 tri)
│   ├── base.py          # Classe de base VisualSort
│   ├── selection.py     # Classe SelectionSortVisualizer
│   ├── quick.py         # Classe QuickSortVisualizer
│   └── merge.py         # Classe MergeSortVisualizer
├── logo.png             # Logo du projet (affiché au lancement)
└── README.md            # Documentation complète
```

---

## 🔢 Algorithmes implémentés

| Nom du tri           | Complexité moyenne | Type         | Stable ? | Méthode          |
|----------------------|--------------------|--------------|----------|------------------|
| Tri par sélection    | O(n²)              | Comparatif   | ❌        | Itératif         |
| Tri à bulles         | O(n²)              | Comparatif   | ✅        | Itératif         |
| Tri par insertion    | O(n²)              | Comparatif   | ✅        | Itératif         |
| Tri fusion           | O(n log n)         | Comparatif   | ✅        | Récursif         |
| Tri rapide           | O(n log n)         | Comparatif   | ❌        | Récursif         |
| Tri par tas          | O(n log n)         | Comparatif   | ❌        | Itératif/heapify |
| Tri à peigne         | O(n log n) approx. | Comparatif   | ❌        | Itératif         |

---

## 🧪 Mode console (`main.py`)

L’utilisateur peut :
- Choisir l’algorithme à utiliser.
- Saisir une liste de nombres réels.
- Obtenir :
  - la liste triée
  - le temps d’exécution (en secondes)

### Exemple :

```
=== Les Papyrus de Héron – Outil de Tri ===
1. Tri par sélection
...
Entrez une liste de nombres : 5.2 1.1 3.4

✅ Liste triée : [1.1, 3.4, 5.2]
⏱️ Temps d'exécution : 0.000012 secondes
```

---

## 👁️ Visualisation graphique (`graphical.py + visuals/`)

Visualisation animée des **tris sélectionnés** via Pygame avec structure **POO modulaire** :

| Tri visuel          | Classe associée             | Type        |
|---------------------|-----------------------------|-------------|
| Tri par sélection   | `SelectionSortVisualizer`   | Itératif    |
| Tri rapide          | `QuickSortVisualizer`       | Récursif    |
| Tri fusion          | `MergeSortVisualizer`       | Récursif    |

Chaque classe hérite de `VisualSort` (dans `base.py`) qui gère :
- le dessin des barres (`draw_list`)
- les pauses animées (`pause`)
- la fenêtre graphique (`win`)

Une image (logo) s’affiche au lancement pour renforcer l'identité visuelle du projet.

---

## 📊 Analyse comparative des performances

Temps d'exécution approximatif sur une liste de 100 éléments :

| Algorithme         | Temps moyen |
|--------------------|-------------|
| Tri fusion         | ~0.002 s    |
| Tri rapide         | ~0.002 s    |
| Tri par tas        | ~0.002 s    |
| Tri à peigne       | ~0.002 s    |
| Tri par insertion  | ~0.006 s    |
| Tri à bulles       | ~0.007 s    |
| Tri par sélection  | ~0.007 s    |

🎯 **Conclusion :** Les tris `fusion`, `rapide`, `tas` sont plus performants. Les tris `sélection`, `bulles`, `insertion` sont pédagogiques pour comprendre les bases.

---

## 🎨 Identité visuelle

Un logo a été généré pour représenter :
- Héron d’Alexandrie en train de dérouler un papyrus
- Des barres de tri colorées
- L’ambiance visuelle d’un manuscrit antique

Le slogan :
> *L’ordre naît de l’algorithme.*

est affiché dans l’image d’accueil Pygame.

---

## 🚀 Extensions possibles

- [ ] Ajout d’une interface graphique avec boutons interactifs
- [ ] Visualisation pour tous les tris (pas seulement 3)
- [ ] Export des mesures de performances dans un fichier CSV
- [ ] Intégration dans une app web (Flask ou Streamlit)

---

## 🙌 Remerciements

Merci à Héron d’Alexandrie de nous avoir inspiré cette aventure algorithmique, et à tous ceux qui œuvrent pour transmettre la beauté des mathématiques et de l’informatique.

---