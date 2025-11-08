# Tests de la Calculatrice Web

Ce répertoire contient l'ensemble des tests automatisés pour la calculatrice web. Les tests sont organisés par composant et couvrent à la fois le backend et le frontend de l'application.

## Organisation des Tests

- `test_operators.py` : Tests des opérations mathématiques de base
  - Addition
  - Soustraction
  - Multiplication
  - Division
  - Cas d'erreur (division par zéro, etc.)

- `test_app.py` : Tests de l'application Flask
  - Routes
  - Gestion des requêtes
  - Validation des entrées
  - Gestion des erreurs

## Exécution des Tests

### Prérequis
```bash
pip install pytest pytest-cov
```

### Commandes de test

1. Exécuter tous les tests :
```bash
python -m pytest
```

2. Exécuter avec détails :
```bash
python -m pytest -v
```

3. Voir la couverture de code :
```bash
python -m pytest --cov=.
```

4. Générer un rapport de couverture HTML :
```bash
python -m pytest --cov=. --cov-report=html
```

## Conventions de Test

1. **Nommage**
   - Les fichiers de test doivent commencer par `test_`
   - Les fonctions de test doivent commencer par `test_`
   - Les noms doivent être descriptifs du cas testé

2. **Documentation**
   - Chaque fichier de test doit avoir un docstring expliquant son objectif
   - Chaque fonction de test doit avoir un docstring décrivant :
     - Le cas testé
     - Les entrées utilisées
     - Le résultat attendu

3. **Organisation**
   - Utiliser des fixtures pytest quand approprié
   - Grouper les tests reliés dans des classes
   - Séparer les données de test du code de test

## Suivi des Problèmes

Lorsqu'un test échoue :
1. Créer une Issue GitHub avec le tag "bug"
2. Inclure dans la description :
   - Le nom du test échoué
   - La sortie de pytest
   - Les étapes de reproduction
   - Le comportement attendu vs observé

## Couverture Actuelle des Tests

Les tests couvrent :
- Toutes les opérations mathématiques
- La validation des entrées
- Les cas limites et d'erreur
- L'interface web
- Le format des résultats