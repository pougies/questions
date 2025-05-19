# Test Technique – Messagerie Django
## Contexte
Vous travaillez sur une application de messagerie avec deux modèles principaux : Message et Thread.
On s'est inspiré d'un comportement comme celui de WhatsApp, Messenger, etc...

Le code source est dans le dossier `django-messages`.

Vous devez choisir un seul des deux tickets suivants. 

Objectif : diagnostiquer, proposer une solution et en discuter.

## Ticket 1 – Bug : Disparition de messages
### Problème
Quand un utilisateur est supprimé, tous ses messages le sont aussi. Le client souhaite que les messages restent visibles.

### User Story

En tant qu’utilisateur, je veux pouvoir lire les messages envoyés par un utilisateur, même après la suppression de son compte.

### Attendu

- Identifier l’origine du bug.
- Peut-on restaurer les messages supprimés ? Si oui, comment ? Sinon, que faire pour éviter ce genre de perte ?
- Ce comportement existe-t-il ailleurs dans le code ?

## Ticket 2 – Fonctionnalité : Lu / Non lu
### Contexte

Un client souhaite avoir un suivi de lecture des messages dans les threads, similaire à WhatsApp.

### User Stories

- En tant qu’utilisateur, lorsque je lis un thread de messages, je veux que tous les messages du thread soient marqués comme "lus" pour moi.
- En tant qu’utilisateur, je veux pouvoir voir, pour chaque message, quels utilisateurs l’ont lu.

### Attendu

- Proposer un modèle de données adapté pour suivre les lectures de messages.
- Discuter sur l'implémentation API afin d'enregistrer les lectures.
- Discuter sur l'implémentation API afin de consulter cette information.

