# Templates Directory

## Objectif
Ce répertoire contient tous les templates HTML utilisés par Flask pour le rendu des pages web de l'application.

## Fichiers principaux
- `index.html`: Template principal de la calculatrice qui inclut :
  - La structure HTML de base
  - Le formulaire de calcul
  - La grille des boutons de la calculatrice
  - L'affichage des résultats

  Le template `index.html` inclut `/static/style.css` pour l’apparence et contient des fonctions JavaScript intégrées pour gérer les interactions utilisateur.

## Dépendances
- Flask (pour le rendu des templates)
- Jinja2 (moteur de template intégré à Flask)
- Les styles définis dans `/static/style.css`

## Notes pour les développeurs
- Les templates utilisent la syntaxe Jinja2 pour le rendu dynamique
- Toute modification doit maintenir la compatibilité avec les routes Flask dans `app.py`
- S'assurer que les IDs et les classes correspondent à ceux utilisés dans le CSS et le JavaScript