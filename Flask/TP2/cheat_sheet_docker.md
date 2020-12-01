# TP 2 - Cheat sheet docker

## Docker lance des processus dans des conteneurs isolés. Un conteneur est un processus qui se lance dans un hôte.

- build : La commande **docker build** construit une image Docker à partir du Dockerfile et un contexte. Un contexte est un ensemble de fichiers situés dans le PATH (chemin où se trouve l'image) ou URL (url vers l'image).

**docker build -t NAMEDEIMAGE PATH**

- run : La commande **docker run** permet de lancer l'image.

**docker run --name NAMECONTAINER --detach (-d) --expose (-p) 5000:5000**

- exec : La commande **docker exec** permet d'executer une commande dans le conteneur (ex : conteneur avec une image Ubuntu => faire une commande)

**docker exec --interactive (-i) NAMECONTAINER|IDCONTAINER --detach (-d) bash**

- port : Un port permet de mapper le port local avec le port virtuel

- Utilité du requirements.txt : Le requirements.txt permet de récupérer la liste des paquets installés
