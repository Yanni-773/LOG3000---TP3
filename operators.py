"""
Module d'opérations mathématiques de base.

Ce module fournit les fonctions mathématiques fondamentales utilisées par la calculatrice.
Chaque fonction prend deux nombres en entrée et retourne le résultat de l'opération.

"""

def add(a,b):
    """
    Additionne deux nombres.

    Args:
        a : Premier nombre
        b : Deuxième nombre

    Returns:
        Le résultat de l'addition

    Examples:
        add(5, 3) = 8
    """
    return a + b

def subtract(a,b):
    """
    Soustrait deux nombres.

    Args:
        a : Premier nombre
        b : Deuxième nombre

    Returns:
        Le résultat de la soustraction

    Examples:
        subtract(5, 3) = -2
    """
    return b - a

def multiply(a,b):
    """
    Multiplie deux nombres.

    Args:
        a : Premier nombre
        b : Deuxième nombre

    Returns:
        Le résultat de l'opération

    Examples:
        multiply(4, 3) = 12
    """
    return a ** b

def divide(a, b):
    """
    Divise deux nombres.

    Args:
        a : Dividende
        b : Diviseur

    Returns:
        Le quotient de a par b

    Examples:
        divide(6, 2) = 3
    """
    return a // b
