# Quickstart

**FastAPI Quickstart** 
* se renseigner sur FastAPI et faire une petite application qui renvoie `hello word`, expliquer ce qu'est une route. Expliquer la difference entre les fonction classique et les fonctions `async`. 
* expliquer la différence entre uvicorn et gunicorn
* Que fait la class `BaseModel` et comment l'utilise t'on?
* charger un dump d'un model ML et faite une route prediction (vous pouvez vous appuyer sur le dataset fournit aux TP de la semaine derniere ou bien prendre les data de votre choix. 

## Route

**Definition :** Une route permet d'accéder à des données par des liens

## Différence entre les fonctions classique et les fonctions "async" 

Une fonction asynchrone permet de ne pas bloquer l'application et des faire des opérations en parallèle. On utilise une fonction asynchrone quand on fait appel à une librairie externe (API, base de données) s'il n'y a pas d'appel à une librairie externe on n'utilise pas l'asynchrone.

## Expliquer la différence entre uvicon et gunicorn

Uvicorn est un serveur

## Que fait la class `BaseModel` et comment l'utilise t'on?

BaseModel permet de créer un modèle et faire un ORM

