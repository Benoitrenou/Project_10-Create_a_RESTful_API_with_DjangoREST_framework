# projet_10

Ce projet est une API développée pour SoftDesk afin de faciliter le suivi des projets et problèmes rencontrés dans leurs développements
L'utilisateur peut ainsi envoyer des requêtes à cette API afin d'obtenir des informations sur :
  - les projets auxquels il est contributeur, 
  - les autres contributeurs du projet,
  - les problèmes liés à ces projets,
  - les commentaires laissés sur ces problèmes.

Cette application a été construite via Django Rest Framework dans sa version 3.13.1.

Afin de faire fonctionner cette application en local, veuillez suivres les indications suivantes

## Clônage du projet

Tout d'abord, clônez en local le dépôt distant via la commande suivante dans votre terminal :

    $ git clone https://github.com/Benoitrenou/projet_10.git

## Création de l'environnement virtuel

Pour créer un environnement virtuel, depuis votre terminal de commande, effectuez les commandes suivantes :

### Sous Linux/ MAC OS

    $ python -m venv <environment_name>
    exemple : python -m venv venvAPI
    
### Sous Windows:
    
    $ virtualenv <environment_name>
    exemple : virtualenv venvAPI 
    
## Activation de l'environnement virtuel 

### Sous Linux / MAC OS:

    $ source <environment_name>/bin/activate
    exemple : source venvAPI/bin/activate
   
### Sous Windows:

    $ source <environment_name>/Scripts/activate
    exemple : source venvAPI/Scripts/activate
    
## Installation des packages : 

Afin que les packages nécessaires au fonctionnement de l'application soient installés sur l'environnement virtuel, entrez la commande suivante :

    $ pip install -r requirements.txt

## Lancement de l'application

Enfin pour lancer l'API, dans le terminal depuis le répertoire du projet :

    $ python manage.py runserver
    
## Accès à la documentation

Vous pouvez retrouver toute la documentation de l'API [à cette adresse](https://documenter.getpostman.com/view/17414272/UVXnFtu4)

## Générer un rapport Flake8

Pour générer un rapport Flake8 dans le terminal, placez vous dans le dossier de travail parent du projet, et utilisez la commande :

    $ flake8 ..projet_10 --exclude venv,__pychache__,settings.py
