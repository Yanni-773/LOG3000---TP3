# Calculatrice Web Simple

## Informations d'équipe
- **Cours**: LOG3000
- **Session**: Automne 2025 
- **Numéro d'équipe**: #19
- **Collaborateurs**: 
  - Yanni Si-Hocine (2215653)
  - Rami Medjdoubi (2208273)

## But et Portée du Projet
Cette calculatrice web est une application simple mais robuste qui permet aux utilisateurs d'effectuer des opérations mathématiques de base via une interface web intuitive. Elle est conçue pour être :
- Facile à utiliser
- Fiable dans ses calculs
- Facilement extensible pour de nouvelles fonctionnalités
- Un exemple de bonnes pratiques de développement web

### Fonctionnalités principales
- Opérations mathématiques de base (addition, soustraction, multiplication, division)
- Interface utilisateur responsive
- Gestion des erreurs de calcul
- Validation des entrées utilisateur

## Architecture Technique
L'application est construite avec :
- **Frontend**: 
  - HTML5 pour la structure
  - CSS3 pour le style et la mise en page responsive
- **Backend**: 
  - Python 3.x
  - Framework Flask pour le serveur web
  - Module `operators.py` pour la logique métier

## Guide d'Installation

### Prérequis
- Python (version 3.8 ou supérieure)
- pip (gestionnaire de paquets Python)
- Git
- Un compte GitHub
- Un navigateur web moderne

### Dépendances Python
Les dépendances sont listées dans `requirements.txt` :
- Flask (framework web)
- pytest (pour l'exécution des tests)
- pytest-cov (pour la couverture des tests)

### Étapes d'installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Yanni-773/LOG3000---TP3.git
   cd LOG3000---TP3
   ```

2. Créez et activez un environnement virtuel Python :
   ```bash
   # Création
   python -m venv venv

   # Activation
   # Pour Windows PowerShell :
   venv\Scripts\activate
   
   # Pour Linux/MacOS :
   source venv/bin/activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Vérifiez l'installation :
   ```bash
   python -c "import flask; print(flask.__version__)"
   ```

## Guide d'utilisation

### Lancement de l'application
1. Activez l'environnement virtuel (si ce n'est pas déjà fait)
2. Lancez le serveur :
   ```bash
   python app.py
   ```
3. Ouvrez votre navigateur à l'adresse : `http://localhost:5000`

### Utilisation de la calculatrice
1. Entrez un premier nombre
2. Sélectionnez l'opération désirée
3. Entrez le second nombre
4. Cliquez sur "=" pour obtenir le résultat

L'interface utilisateur utilise :
- `static/style.css` pour la mise en page et le style
- Fonctions JavaScript intégrées :
  - `appendToDisplay()` : Ajoute les chiffres et opérateurs à l'affichage
  - `clearDisplay()` : Efface l'affichage (bouton C)

### Gestion des erreurs courantes
- Division par zéro : Un message d'erreur approprié sera affiché
- Entrées non numériques : L'application validera les entrées
- Erreurs de serveur : Un message d'erreur explicite sera montré

## Tests

### Exécution des tests
Les tests sont organisés dans le dossier `tests/` avec des fichiers nommés `test_*.py`. 

Pour exécuter les tests :
```bash
# Exécuter tous les tests avec détails
python -m pytest -v

# Exécuter les tests avec couverture
python -m pytest --cov=.

# Exécuter un fichier de test spécifique
python -m pytest tests/test_operators.py -v
```

### Types de tests
- Tests unitaires : Validation des opérations mathématiques
- Tests d'intégration : Validation des routes Flask
- Tests de l'interface utilisateur : Validation du comportement frontend

## Flux de Contribution

### Branches
- `main` : Code de production stable
- `develop` : Branche de développement principale
- `feature/*` : Nouvelles fonctionnalités
- `bugfix/*` : Corrections de bugs
- `hotfix/*` : Corrections urgentes en production

### Process de contribution
1. Créez une nouvelle branche depuis `develop`
2. Développez et testez votre fonctionnalité
3. Créez une Pull Request vers `develop`
4. Attendez la revue de code
5. Après approbation, le code sera fusionné

### Gestion des issues
- Utilisez les templates d'issues fournis
- Étiquetez correctement (bug, enhancement, etc.)
- Référencez les issues dans les commits (#numero-issue)

## Structure du projet
```
.
├── app.py              # Application principale Flask
├── operators.py        # Logique des opérations mathématiques
├── static/
│   └── style.css      # Styles CSS
└── templates/
    └── index.html     # Interface utilisateur
```

## Documentation supplémentaire
- Voir `/static/README.md` pour la documentation frontend
- Voir `/templates/README.md` pour la documentation des templates
- Les docstrings Python fournissent la documentation détaillée des fonctions