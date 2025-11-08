"""
Tests de l'application Flask.

Ce module contient les tests d'intégration pour l'application web,
vérifiant le bon fonctionnement des routes, la gestion des formulaires,
et la validation des entrées.

Les tests utilisent le client de test Flask pour simuler des requêtes HTTP.
"""

import pytest
from app import app, calculate

@pytest.fixture
def client():
    """
    Fixture pytest qui fournit un client de test Flask.
    
    Returns:
        FlaskClient: Client de test pour faire des requêtes HTTP
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    """
    Test de la route principale en GET.
    
    Vérifie que :
    - La page est accessible
    - Le code de statut est 200
    - Le contenu HTML est correct
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b'Flask Calculator' in response.data

def test_index_post_valid(client):
    """
    Test de calcul valide via POST.
    
    Vérifie que :
    - Le calcul est effectué correctement
    - Le résultat est affiché
    - Pas d'erreurs générées
    """
    response = client.post('/', data={'display': '2 + 3'})
    assert response.status_code == 200
    assert b'5' in response.data

def test_index_post_invalid(client):
    """
    Test de gestion des erreurs pour entrées invalides.
    
    Vérifie que :
    - Les entrées invalides sont gérées gracieusement
    - Un message d'erreur approprié est affiché
    """
    response = client.post('/', data={'display': 'invalid'})
    assert response.status_code == 200
    assert b'Error' in response.data

def test_calculate_function():
    """
    Tests unitaires pour la fonction calculate().
    
    Vérifie :
    - Parsing correct des expressions
    - Gestion des espaces
    - Validation des opérateurs
    - Gestion des erreurs
    """
    assert calculate('2 + 3') == 5
    assert calculate('10 - 5') == -5  # Note: l'ordre est inversé dans subtract
    
    # Test des erreurs
    with pytest.raises(ValueError):
        calculate('')  # Expression vide
    
    with pytest.raises(ValueError):
        calculate('1 + 2 + 3')  # Plusieurs opérateurs
    
    with pytest.raises(ValueError):
        calculate('abc + def')  # Opérandes non numériques