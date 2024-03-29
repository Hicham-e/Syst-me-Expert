# Syteme expert pour la gestion de diagnostics de dysfonctionnements informatiques

## Description
Ce programme permet de diagnostiquer les dysfonctionnements informatiques en se basant sur les symptômes observés. Il offre deux sessions: une pour les utilisateurs pour sélectionner les symptômes et recevoir un diagnostic, et une autre pour les experts pour ajouter et supprimer des symptômes et des diagnostics.

## Fonctionnalités
- Ajout et suppression de symptômes
- La session expert est sécurisée par un username et mot de passe (admin - admin)
- Enregistrement des données dans un fichier `data.txt`
- Chargement des données à partir du fichier `data.txt`
- Inférence du diagnostic pour un symptôme donné
- Interface utilisateur conviviale avec des boutons colorés pour faciliter la navigation

## Utilisation
**Installez d'abord Tkinter en utilisant 'pip install tk'

L'utilisateur peut choisir les symptômes observés depuis une liste déroulante et cliquer sur le bouton "Diagnostiquer" pour obtenir le diagnostic. Les experts peuvent supprimer un symptôme et son diagnostic ou ajouter de nouveaux symptômes en entrant le nom du symptôme et le diagnostic correspondant dans une fenêtre dédiée.

## Fichier `data.txt`
Le fichier `data.txt` est utilisé pour stocker les symptômes et leurs diagnostics. Chaque ligne du fichier contient un symptôme suivi de son diagnostic, séparés par `:`.

