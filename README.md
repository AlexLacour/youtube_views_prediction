## Quick Start

__COMMANDES POUR RUN LE PROJET__

```bash
#tout run proprement (4 à 8 min pour pull les images)
sh start.sh 

# Run tout les dockers (non recommandé car la base mongo sera vide)
docker-compose up

#arreter tout les process, simplement un 
docker-compose down
```
----------------
## titre Le fonctionnement

### titre  1- Une BDD mongo

un simple petit docker mongo, avec la petite nuance des data

### titre  2- Un front

un script nodeJS qui sert juste à envoyer une requête au scrapper (un URL youtube), et à récuperer la prédiction

### titre  3- Une partie Machine Learning

Assez basique, elle apprends à prédire à partir des données fournies de la BDD le le nombre de vues de la requette de l'utilisateur agrémentée d'autre informations aquises par le scraper

### titre  4- Un scrapper

Un bon petit scraper qui récupère toute les informations que l'on a trouvé utiles (et réalisable) pour la prédiction.
