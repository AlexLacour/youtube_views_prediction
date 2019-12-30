## Quick Start

__COMMANDES POUR RUN LE PROJET__

Au choix: 
```bash
#tout run proprement (4 à 8 min pour pull les images)
sh start.sh 
```
 ou: 
```bash
# Run tout les dockers (non recommandé)
docker-compose up --build -d 
# importe la BDD
docker exec mongodb mongoimport --db yt_db --collection projet_cs --file data.json --jsonArray
```
pour arreter tout les process, simplement un
```bash
docker-compose down
```

----------------
## Le fonctionnement
 ![architecture](archi.png)
 en noir les requetes, en rouge les réponses
###  1- Une BDD mongo

un simple petit docker mongo, avec la petite nuance des data

###  2- Un front

un script nodeJS qui sert juste à envoyer une requête au scrapper (un URL youtube), et à récuperer la prédiction

###  3- Une partie Machine Learning

Assez basique, elle apprends à prédire à partir des données fournies de la BDD le le nombre de vues de la requette de l'utilisateur agrémentée d'autre informations aquises par le scraper

###  4- Un scraper

Un bon petit scraper qui récupère toute les informations que l'on a trouvé utiles (et réalisable) pour la prédiction.
