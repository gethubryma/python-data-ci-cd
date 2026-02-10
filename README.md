
# Projet DevOps – Tests Pytest + Coverage + GitHub Actions

## Objectif du projet
Ce projet a pour but de mettre en place une démarche **CI (Intégration Continue)** sur un mini-module Python (`df_ops.py`) :
- écrire des fonctions simples de manipulation de DataFrame (pandas)
- écrire des **tests unitaires** avec **pytest**
- mesurer la **couverture de code** avec **pytest-cov**
- automatiser l’exécution des tests dans **GitHub Actions** à chaque `push` / `pull_request`

---

## Contenu du projet
- `src/df_ops.py` : fonctions de manipulation de DataFrame (moyennes, filtre, contrôle des colonnes…)
- `tests/test_df_ops.py` : tests unitaires pytest
- `.github/workflows/` : workflow CI GitHub Actions (tests automatiques)
- `coverage.xml` : rapport de couverture (généré par pytest-cov)

## Structure du projet

## Structure du projet

```text
NOM_PRENOM/
├── src/
│   ├── __init__.py
│   └── df_ops.py
├── tests/
│   └── test_df_ops.py
├── requirements.txt
└── .github/
    └── workflows/
        └── tests.yml




## Ce que j’ai fait (étapes)

1. Création du module `src/df_ops.py` :
   - création d’un DataFrame (`build_dataframe`)
   - calculs : `mean_age`, `mean_salary`
   - filtre : `filter_by_department`
   - compteur de lignes : `row_count`
   - vérification des colonnes : `_check_columns` (lève une erreur si colonne manquante)

2. Création des tests `tests/test_df_ops.py` avec pytest :
   - tests des résultats (moyennes, filtre, nombre de lignes)
   - test du cas d’erreur (colonne manquante) avec `pytest.raises(ValueError)`

3. Ajout de la couverture de code :
   - affichage des lignes manquantes (`--cov-report=term-missing`)
   - génération du rapport `coverage.xml`

4. Mise en place de GitHub Actions :
   - installation des dépendances
   - exécution automatique de `pytest` + coverage

---

## Installation et prérequis
- Python 3.x
- pandas
- pytest
- pytest-cov

### Installation (Ubuntu/WSL)

```bash
sudo apt update && sudo apt install -y python3-pandas python3-pytest python3-pytest-cov

```


## Commandes utilisées

### 1) Lancer les tests

```bash
pytest
```

 Permet de vérifier que toutes les fonctions du module fonctionnent correctement.

### 2) Lancer les tests avec détails

```bash
pytest -v
```

 Affiche chaque test exécuté (utile pour comprendre ce qui passe/échoue).

### 3) Générer la couverture de code

```bash
pytest --cov=src --cov-report=term-missing
```

 Mesure le % de lignes exécutées par les tests et affiche les lignes manquantes.

### 4) Générer un fichier XML de couverture

```bash
pytest --cov=src --cov-report=xml
```

 Crée `coverage.xml` pour l’exploitation en CI/CD 

---

## Résultat obtenu

* Tous les tests passent (100 %)
* Couverture de code : atteindre une couverture maximale (100% selon les tests)

---

## GitHub Actions (CI)

Le workflow GitHub Actions est placé dans :

```
.github/workflows/
```

Il permet de :

* lancer automatiquement les tests à chaque push / pull request
* installer les dépendances
* générer la couverture

---


