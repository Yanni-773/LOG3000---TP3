"""
Application principale de la calculatrice web.

Ce module implémente une calculatrice web simple utilisant Flask. Il fournit une interface
pour effectuer des opérations mathématiques de base (addition, soustraction, multiplication, division)
via une interface web.

Dépendances:
    - Flask : Pour le serveur web et le routage
    - operators : Module contenant les opérations mathématiques de base
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire associant les symboles d'opération aux fonctions correspondantes
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Parse et évalue une expression mathématique simple.

    Cette fonction analyse une chaîne de caractères contenant une expression mathématique
    de la forme "nombre1 opérateur nombre2" et retourne le résultat du calcul.

    Args:
        expr (str): L'expression à évaluer (ex: "5 + 3", "10 * 2")

    Returns:
        float: Le résultat de l'opération mathématique

    Raises:
        ValueError: Si l'expression est invalide (vide, mal formatée, opérandes non numériques,
                   plusieurs opérateurs, etc.)

    Examples:
        calculate("5 + 3") = 8
        calculate("10 * 2") = 20
    """
    # Validation de l'entrée
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Suppression des espaces pour faciliter le parsing
    s = expr.replace(" ", "")

    # Recherche de l'opérateur dans l'expression
    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            # Vérifie qu'il n'y a qu'un seul opérateur
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Vérifie que l'opérateur est bien placé (pas au début ni à la fin)
    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    # Extraction des opérandes
    left = s[:op_pos]
    right = s[op_pos+1:]

    # Conversion des opérandes en nombres
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application.

    Gère l'affichage de la calculatrice et le traitement des calculs.
    - GET : Affiche la calculatrice
    - POST : Traite l'expression mathématique soumise et affiche le résultat

    Returns:
        str: Page HTML rendue avec le template index.html
    """
    result = ""
    if request.method == 'POST':
        # Récupération de l'expression depuis le formulaire
        expression = request.form.get('display', '')
        try:
            # Calcul du résultat
            result = calculate(expression)
        except Exception as e:
            # En cas d'erreur, affichage d'un message explicite
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)