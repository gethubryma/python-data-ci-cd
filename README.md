
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

---

## Ce que j’ai fait (étapes)
1. Création du module `df_ops.py` avec des fonctions :
   - `build_dataframe()`
   - `mean_age()`
   - `mean_salary()`
   - `filter_by_department()`
   - `row_count()`
   - `_check_columns()` (vérifie la présence des colonnes et lève une erreur sinon)

2. Écriture des tests avec **pytest** (`tests/test_df_ops.py`) :
   - tests des valeurs de retour (moyennes, nombre de lignes, filtre)
   - test du cas d’erreur (colonne manquante) avec `pytest.raises(ValueError)`

3. Ajout de la couverture de code (**pytest-cov**) :
   - exécution locale
   - génération de `coverage.xml`

4. Mise en place de la CI sur GitHub Actions :
   - installation des dépendances
   - exécution de `pytest`
   - génération du rapport de coverage

---

## Installation et prérequis
- Python 3.x
- pandas
- pytest
- pytest-cov

### Installation (Ubuntu/WSL)

```bash
python3 -m pip install --user pandas pytest pytest-cov
```

---

## Commandes utilisées

### 1) Lancer les tests

```bash
pytest
```

✅ Permet de vérifier que toutes les fonctions du module fonctionnent correctement.

### 2) Lancer les tests avec détails

```bash
pytest -v
```

✅ Affiche chaque test exécuté (utile pour comprendre ce qui passe/échoue).

### 3) Générer la couverture de code

```bash
pytest --cov=src --cov-report=term-missing
```

✅ Mesure le % de lignes exécutées par les tests et affiche les lignes manquantes.

### 4) Générer un fichier XML de couverture

```bash
pytest --cov=src --cov-report=xml
```

✅ Crée `coverage.xml` pour l’exploitation en CI/CD (ex: Codecov).

---

## Résultat obtenu

* Tous les tests passent :

  * `4 passed`
* Couverture de code :

  * objectif : atteindre une couverture maximale
  * après ajout du test qui déclenche l’erreur de colonne manquante, la couverture augmente (ex: de 95% vers 100% selon les tests)

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

## Conclusion

Ce projet montre une démarche DevOps simple :

* écrire du code + écrire des tests
* vérifier automatiquement via CI
* mesurer la qualité via coverage

C’est une base réutilisable pour des projets plus grands (DataOps / MLOps).

```

