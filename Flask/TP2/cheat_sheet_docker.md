# TP 2 - Cheat sheet docker

## Docker lance des processus dans des conteneurs isolés. Un conteneur est un processus qui se lance dans un hôte.

- build : La commande **docker build** construit une image Docker à partir du Dockerfile et un contexte. Un contexte est un ensemble de fichiers situés dans le PATH (chemin où se trouve l'image) ou URL (url vers l'image).

**docker build -t NAMEDEIMAGE:VERSION_PATH**

- run : La commande **docker run** permet de lancer l'image.

**docker run --name NAMECONTAINER --detach (-d) --expose (-p) 5000:5000 IMAGEID**

- exec : La commande **docker exec** permet d'executer une commande dans le conteneur (ex : conteneur avec une image Ubuntu => faire une commande)

**docker exec --interactive (-i) NAMECONTAINER|IDCONTAINER bash**

- port : Un port permet de mapper le port local avec le port virtuel

- Utilité du requirements.txt : Le requirements.txt permet de récupérer la liste des paquets installés

## Deploiement sur Heroku

- Installer le client heroku avec la commande suivante : 

**sudo snap install --classic heroku**

- Connexion heroku : **sudo heroku login**

- Connexion container registry : **sudo heroku container:login** 

Si on veut build et push l'image 

- **sudo heroku container:push <process-type (web, worker?)>**

Si on a déjà une image buildé

- **sudo docker tag IMAGEID registry.heroku.com/<appnameheroku>/<process-type>**


- Poussé l'image docker dans le registry : **sudo docker push registry.heroku.com/<appnameheroku>/<process-type>**

- **sudo heroku container:push web -a <appnameheroku>**

- **sudo heroku container:release web -a <appnameheroku>**