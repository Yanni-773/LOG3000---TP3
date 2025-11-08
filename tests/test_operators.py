"""
Tests des opérations mathématiques de la calculatrice.

Ce module contient les tests unitaires pour toutes les opérations
mathématiques définies dans operators.py.

Les tests vérifient :
- Le comportement normal des opérations
- Les cas limites
- La gestion des erreurs
"""

import pytest
from operators import add, subtract, multiply, divide

def test_add():
    """
    Test de l'addition.
    
    Vérifie que la fonction add() :
    - Additionne correctement deux nombres positifs
    - Gère correctement les nombres négatifs
    - Retourne le bon type (int)
    - Gère correctement le zéro
    """
    # Test d'addition de nombres positifs
    assert add(2, 3) == 5, "L'addition de 2 et 3 devrait donner 5"
    
    # Test d'addition avec nombre négatif et positif
    assert add(-1, 1) == 0, "L'addition de -1 et 1 devrait donner 0"
    
    # Test d'addition avec zéro (élément neutre)
    assert add(0, 0) == 0, "L'addition de 0 et 0 devrait donner 0"
    
    # Vérification du type de retour
    assert isinstance(add(2, 3), int), "Le résultat devrait être un entier"

def test_subtract():
    """
    Test de la soustraction.
    
    Vérifie que la fonction subtract() :
    - Soustrait correctement deux nombres (a - b)
    - Gère les nombres négatifs dans différentes combinaisons
    - Gère la soustraction avec des nombres négatifs
    """
    # Test de soustraction de nombres positifs
    assert subtract(3, 2) == 1, "3 - 2 devrait donner 1"
    
    # Test de soustraction avec un négatif et un positif
    assert subtract(-1, 1) == -2, "-1 - 1 devrait donner -2"
    
    # Test de soustraction de deux nombres négatifs
    assert subtract(-3, -2) == -1, "-3 - (-2) devrait donner -1"

def test_multiply():
    """
    Test de la multiplication.
    
    Vérifie que la fonction multiply() :
    - Multiplie correctement deux nombres positifs (a * b)
    - Gère correctement les nombres négatifs (règle des signes)
    - Gère correctement la multiplication par zéro
    - Vérifie la commutativité (a * b = b * a)
    """
    # Test de multiplication de nombres positifs
    assert multiply(2, 3) == 6, "2 * 3 devrait donner 6"
    
    # Test avec un nombre négatif (règle des signes)
    assert multiply(-2, 3) == -6, "-2 * 3 devrait donner -6"
    
    # Test avec deux nombres négatifs
    assert multiply(-2, -3) == 6, "-2 * -3 devrait donner 6 (moins par moins donne plus)"
    
    # Tests avec zéro (élément absorbant)
    assert multiply(2, 0) == 0, "Toute multiplication par 0 devrait donner 0"
    assert multiply(0, 5) == 0, "Toute multiplication par 0 devrait donner 0"

def test_divide():
    """
    Test de la division entière.
    
    Vérifie que la fonction divide() :
    - Effectue une division entière (//) correctement
    - Gère les cas où le résultat n'est pas un nombre entier
    - Lève une exception appropriée pour la division par zéro
    """
    # Test de division exacte
    assert divide(8, 2) == 4, "8 // 2 devrait donner 4"
    
    # Test de division avec reste (troncature vers 0)
    assert divide(8, 3) == 2, "8 // 3 devrait donner 2 (partie entière)"
    
    # Test de division par zéro
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_ui_input_validation():
    """
    Tests spécifiques pour valider le traitement des entrées utilisateur.
    
    Vérifie le comportement avec :
    - Les nombres avec des zéros non significatifs (ex: '02')
    - Les expressions contenant des espaces
    - Les expressions mal formées ou invalides
    """
    from app import calculate
    
    # Test avec des zéros non significatifs
    assert calculate("02+3") == 5, "Les zéros non significatifs devraient être ignorés"
    
    # Test avec des espaces dans l'expression
    assert calculate("  5  +  3  ") == 8, "Les espaces devraient être ignorés"
    
    # Tests des expressions invalides
    with pytest.raises(ValueError, message="Les opérateurs doubles devraient être rejetés"):
        calculate("5++3")
    
    with pytest.raises(ValueError, message="Les expressions incomplètes devraient être rejetées"):
        calculate("5+")
    
    with pytest.raises(ValueError, message="Les expressions commençant par un opérateur devraient être rejetées"):
        calculate("+5")

def test_edge_cases():
    """
    Test des cas limites et particuliers pour toutes les opérations.
    
    Vérifie le comportement avec :
    - De grands nombres pour tester les limites
    - Opérations avec zéro dans différents contextes
    - Cas particuliers de la division entière
    """
    # Tests avec de grands nombres
    assert add(999, 1) == 1000, "Addition proche d'un grand nombre rond"
    assert add(500, 500) == 1000, "Addition de grands nombres égaux"
    
    # Tests avec zéro dans différentes positions
    assert add(0, 5) == 5, "Addition avec zéro à gauche"
    assert add(5, 0) == 5, "Addition avec zéro à droite"
    assert multiply(5, 0) == 0, "Multiplication par zéro à droite"
    assert multiply(0, 5) == 0, "Multiplication par zéro à gauche"
    
    # Tests de division par zéro
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
    
    # Tests de division entière avec des cas particuliers
    assert divide(100, 3) == 33, "Division entière de 100 par 3"
    assert divide(1000, 10) == 100, "Division entière par une puissance de 10"
