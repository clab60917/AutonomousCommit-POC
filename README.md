# Autonomous-Comit-POC
# Automatisation des commits sur GitHub

Ce projet est un exemple simple d'automatisation des commits sur GitHub pour afficher des carrés verts sur le graphique de profil. Ce script Python crée un nombre aléatoire de commits (1 à 3) chaque jour à une heure prédéterminée. Les commits sont effectués dans un fichier texte nommé `commits.txt`.

**Attention :** Ce projet est destiné à des fins éducatives et de démonstration seulement. Il n'est pas recommandé de l'utiliser pour des projets réels, car il crée des commits inutiles.

## Fonctionnement

Le script `comit_auto_poc.py` crée ou met à jour un fichier `commit.txt` en y ajoutant une ligne avec la date et l'heure actuelles. Ensuite, il effectue un commit avec les modifications et le pousse sur le dépôt GitHub. 🚀

Le script est configuré pour s'exécuter automatiquement à l'aide d'une tâche cron sur un serveur VPS Linux.

## Configuration

Pour configurer et utiliser ce script, suivez ces étapes :

1. Clonez ce dépôt sur votre serveur VPS.
```bash
https://github.com/clab60917/Autonomous-Comit-POC
cd Autonomous-Comit-POC
```
2. Assurez-vous que Python 3 est installé sur votre VPS.
```bash
sudo apt install python3
```
3. '' git est installé sur votre VPS.
```bash
sudo apt-get update
sudo apt-get install git
```
4. Configurez Git avec votre compte :
```bash
git config --global user.name "Votre nom"
git config --global user.email "votre-email@example.com"
```
5. Generez une clef SSH pour votre VPS :
```bash
ssh-keygen -t ed25519 -C "votre-email@example.com"
```
6. Affichez la clef et copiez là sûr : https://github.com/settings/keys
```bash
cat ~/.ssh/id_ed25519.pub
```
7. Installez la dépendance `GitPython` en exécutant : `pip3 install gitpython`.
8. Configurez l'accès SSH à votre compte GitHub sur votre VPS.
9. Modifiez l'URL du dépôt distant pour utiliser le protocole SSH.
10. Configurez une tâche cron pour exécuter le script à l'heure souhaitée.
```bash
crontab -e
0 15 * * * /usr/bin/python3 /chemin/absolu/vers/commit_automatique.py

```


## Remarque

Ce projet est un Proof of Concept (POC) pour démontrer l'automatisation des commits sur GitHub. L'utilisation de ce script pour "tricher" en affichant une activité constante sur votre profil GitHub n'est pas recommandée et pourrait être mal perçue par d'autres utilisateurs ou employeurs potentiels.
