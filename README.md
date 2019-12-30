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
pour relancer, vous pouvez aussi (le luxe!):
```bash
sh restart.sh 
```
----------------
## Le fonctionnement
 ![architecture](archi.png)
 en noir les requetes, en rouge les réponses
----------------

###  1- Une BDD mongo

Un simple petit docker mongo, qui écoute sur son port 27017 (vous pouvez essayer de visualiser directement les data via ROBO3T si vous vous sentez aventureux).
Les données sont donc en format JSON:
```JSON
{
 "likes":11661,
 "dislikes":442,
 "ld_ratio":26.3227990971,
 "date":"2017-11-12T15:00:02.000Z",
 "genre":24,
 "is_title_all_caps":false,
 "views":301920
}
```

----------------

###  2- Un front

Un script nodeJS qui sert juste à envoyer une requête au scrapper (un URL youtube), et à récuperer la prédiction. On a essayé de faire fonctionner angular (avec cli) dans un docker node mais npm boudait. (permissions non accordée, puis les node_modules ne se faisait pas au bon endroit dans le docker malgrés le WORKDIR ...)

----------------

*Les deux dockers suivants sont construits sur l'image python:3.7.2-slim, (alpine ne fonctionnait pas mais on voulait tout de même une version assez légère, avec python3 ).*

*Pour faire des modifications sur ces dockers, il suffit d'ajouter les nouvelles libs utilisées dans le requirements.txt du conteneur, et modifier (ou ajouter) les scripts python.*

###  3- Une partie Machine Learning

Elle utilise la LinearRegression de scikit learn. Elle permet en théorie de prédire, à partir des données fournies de la BDD, le nombre de vues de la requette de l'utilisateur agrémentée d'autre informations aquises par le scraper.
Elle reçoit le JSON créé par le scraper, pull le JSON du mongo, fait un fit, puis revoie au front le résultat.

###  4- Un scraper

Un bon petit scraper qui récupère toute les informations que l'on a trouvé utiles (et réalisable) pour la prédiction. Il reçoit un URL youtube, scrap des informations liées à la vidée, et envoie le JSON à la partie ML.
