# Calculatrice Web Simple

## Informations d'équipe
- **Cours**: LOG3000
- **Session**: Automne 2025 
- **Numéro d'équipe**: #19
- **Collaborateurs**: 
Yanni Si-Hocine (2215653)
Rami Medjdoubi (2208273)

## Objectif
Ce projet est une calculatrice web simple développée avec Flask. L'application permet aux utilisateurs d'effectuer des opérations mathématiques de base via une interface web intuitive.

## Description
L'application est construite avec :
- **Frontend**: Interface utilisateur HTML/CSS
- **Backend**: Serveur Flask en Python

## Prérequis d'installation
Avant de commencer, assurez-vous d'avoir installé :
- Python (version 3.x recommandée)
- pip (gestionnaire de paquets Python)
- Git
- Un compte GitHub

## Instructions d'installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Yanni-773/LOG3000---TP3.git
   cd LOG3000---TP3
   ```

2. Créez un environnement virtuel Python (recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Pour Linux/MacOS
   # OU
   venv\Scripts\activate     # Pour Windows
   ```

3. Installez les dépendances :
   ```bash
   pip install flask
   ```

4. Lancez l'application :
   ```bash
   python app.py
   ```

5. Ouvrez votre navigateur et accédez à :
   ```
   http://localhost:5000
   ```

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

## Contribution
Pour contribuer au projet :
1. Créez une nouvelle branche pour vos modifications
2. Faites vos changements et committez-les
3. Soumettez une pull request pour révision