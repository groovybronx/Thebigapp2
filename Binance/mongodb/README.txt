# Gestionnaire Simple de MongoDB

Ce projet est un gestionnaire simple de bases de données MongoDB, permettant de créer, supprimer, et explorer les bases de données, ainsi que d'ajouter et supprimer des documents dans les collections.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés :

* [Docker](https://www.docker.com/)
* [Node.js](https://nodejs.org/) et [npm](https://www.npmjs.com/)

## Installation

1.  **Clonez le dépôt :**

    ```bash
    git clone <URL_DU_DÉPÔT>
    cd <NOM_DU_RÉPERTOIRE>
    ```

2.  **Installez les dépendances :**

    ```bash
    npm install
    ```

3.  **Configuration de l'environnement Docker :**

    Assurez-vous que Docker est en cours d'exécution.

4.  **Démarrage de l'application :**

    Utilisez Docker Compose pour démarrer l'application et la base de données MongoDB :

    ```bash
    docker-compose up --build
    ```

    Cela va construire les images Docker et démarrer les conteneurs.

5.  **Accès à l'application :**

    Ouvrez votre navigateur et accédez à `http://localhost:3000/data`.

## Utilisation

* **Création d'une base de données :**
    * Entrez le nom de la base de données dans le champ prévu à cet effet et cliquez sur "Créer".
* **Liste des bases de données :**
    * La liste des bases de données disponibles s'affiche.
    * Cliquez sur le nom d'une base de données pour explorer ses collections et documents.
* **Suppression d'une base de données :**
    * Cliquez sur le bouton "Supprimer" à côté du nom de la base de données.
* **Gestion des collections et documents :**
    * Sur la page d'une base de données sélectionnée, les collections sont listées avec leurs documents.
    * Utilisez le formulaire pour ajouter de nouveaux documents à une collection.
    * Cliquez sur le bouton "Supprimer" à côté d'un document pour le supprimer.
* **Retour à la liste des bases de données :**
    * Cliquez sur le bouton "Retour à la liste des bases de données" pour revenir à la page principale.

## Structure du projet

* `app.js` : Le point d'entrée de l'application Node.js.
* `models/data.js` : Le modèle de données pour les documents de la collection.
* `routes/data.js` : Les routes Express pour l'application.
* `views/index.ejs` : La vue principale pour la liste des bases de données.
* `views/database.ejs` : La vue pour la gestion d'une base de données sélectionnée.
* `package.json` : Les dépendances du projet.
* `Dockerfile` : La configuration Docker pour l'application.
* `docker-compose.yml` : La configuration Docker Compose pour l'application et MongoDB.

## Dépendances

* `express` : Framework web pour Node.js.
* `mongoose` : Bibliothèque pour interagir avec MongoDB.
* `body-parser` : Middleware pour analyser les corps de requête.
* `ejs` : Moteur de template pour les vues.
* `bootstrap` : Framework CSS pour le style de l'application.

## Docker

* L'application utilise Docker pour faciliter le déploiement et la gestion de l'environnement.
* Le fichier `docker-compose.yml` définit les services pour l'application et MongoDB.
* Les données MongoDB sont stockées dans un volume Docker pour persister les données entre les redémarrages.

## Améliorations futures

* Ajouter des fonctionnalités de filtrage et de tri pour les documents.
* Implémenter l'authentification et l'autorisation.
* Améliorer l'interface utilisateur avec des fonctionnalités supplémentaires.
* Ajouter des tests unitaires et d'intégration.