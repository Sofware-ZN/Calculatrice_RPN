# RPN API (Notation Polonaise Inversée)

Cette API REST permet de gérer une calculatrice RPN en mode client/serveur via FastAPI.

## Fonctionnalités
- Créer une pile
- Ajouter un élément à la pile
- Récupérer une pile
- Supprimer une pile
- Appliquer une opération arithmétique : `+`, `-`, `*`, `/`

## Lancement

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
