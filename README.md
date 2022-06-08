# Remote Procedure Invocation  Design Pattern
### par Nicolas Gretten et Florian Grosdidier

Ceci est un exemple du design pattern RPI avec le protocole REST en python.

Deux Microservices (une API gestion d'utilisateurs et une API de gestion d'adresse) communique ensemble:
- on crée une adresse
- on crée un user en lui donnant un ID d'une adresse
- sur les requêtes GET de l'API User, les adresses correspondant à l'id de l'adresse seront récupérer depuis l'API address et ajouter à la réponse

### Prérequis
Docker et Docker compose.

port 8000 et 8001 de libre.
### Installation

Cloner le dépôt Git.

et utiliser les commandes suivantes :
 ``` bash
 cd userAPI && docker-compose up -d && cd ..
 ```

``` bash
 cd addressAPI && docker-compose up -d && cd ..
 ```

Pour rebuild les images:

``` bash
 cd addressAPI && docker build -t addressapi_address-api . && cd ..
 ```

``` bash
 cd userAPI && docker build -t userapi_user-api . && cd ..
 ```
