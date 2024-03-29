# Annuaire XUE

## Présentation

Ce dépôt contient un annuaire qui permet de recommander des contacts intéressants, sous la forme d'une application Django. Ce projet est né au sein de l'association X-Urgence écologique (XUE).

## Prérequis

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/)
- [Django](https://docs.djangoproject.com/en/4.1/topics/install/)

## Installation du projet

### Pour Windows

1. Cloner le projet en lançant cette commande dans la console (cmd ou Git Bash)

   ```sh
   git clone https://github.com/PalmyreB/annuaire_xue.git
   ```

2. Se rendre dans le dossier du projet

   ```sh
   cd annuaire_xue
   ```

3. Créer un environnement virtuel

   ```sh
   py -m venv venv
   ```

4. Activer l'environnement virtuel

   ```sh
   # Dans l'invite de commandes (cmd) :
   venv\Scripts\activate.bat
   # Dans Git Bash :
   source venv/Scripts/activate
   ```

5. Installer les _requirements_

   ```sh
   pip install -r requirements.txt
   ```

6. Créer un fichier nommé `.env` avec la clé secrète communiquée par un administrateur (à défaut, pour des tests locaux, une clé arbitraire – ne pas mettre les accolades dans cette commande)

   ```sh
   echo SECRET_KEY={votre clé secrète} > .env
   echo SECRET_KEY_FALLBACKS= >> .env
   ```

7. Lancer les migrations

   ```sh
   py manage.py migrate
   ```

8. Créer un profil de super-utilisateur

   ```sh
   py manage.py createsuperuser
   ```

### Pour Linux

Seules les étapes 4. et 6. sont modifiées de la façon suivante :

1. Pour activer l'environnement virtuel il faut utiliser

   ```sh
   source venv/bin/activate
   ```

2. Créer le fichier .env avec nano et y coller les champs SECRET_KEY et SECRET_KEY_FALLBACKS (Ctrl+Shift+V)

   ```sh
   nano .env
   ```

### Via PyCharm

1. Installer PyCharm et python

2. Lancer PyCharm et créer un nouveau projet depuis un VCS

3. Choisir Git et donner comme URL : <https://github.com/PalmyreB/annuaire_xue.git>

4. Créer un venv dans PyCharm (Ctrl+Alt+S si le logiciel ne le propose pas puis aller dans Interpréteur) en donnant le chemin vers votre python

5. Installer les prérequis dans la console PyCharm

   ```sh
   pip install -r requirements.txt
   ```

6. Créer un nouveau fichier .env et y ajouter les champs SECRET_KEY et SECRET_KEY_FALLBACKS communiqués par un admin

7. Ajouter .idea/ au fichier .gitignore

8. Lancer les migrations

   ```sh
   python manage.py migrate
   ```

9. Créer un profil de super-utilisateur

   ```sh
   python manage.py createsuperuser
   ```

## Lancer le projet

Avec l'environnement virtuel actuel, lancer la commande suivante depuis la racine

```sh
py manage.py runserver
```

Se rendre à l'adresse <http://127.0.0.1:8000/>.

La connexion se fait sur la page <http://127.0.0.1:8000/accounts/login/>.

L'interface d'administration se trouve à l'adresse <http://127.0.0.1:8000/admin/>.

> ⚠️ Attention, le profil de super-utilisateur créé à l'initialisation du projet n'est pas associé à un contact référent par défaut, et ne permet donc pas d'accéder à toutes les pages. Lors du premier lancement, s'inscrire sur <127.0.0.1:8000/accounts/register/>. Pour pouvoir utiliser le compte de super-utilisateur comme un autre compte, il est possible de le lier à un contact référent.

## Contribuer au projet

Vous pouvez :

- corriger le code, l'améliorer, traiter un ticket sur la page des _issues_ et créer une PR,
- faire remonter les dysfonctionnements ou les suggestions d'amélioration en créant des _issues_.

## Ressources

- [Documentation Django](https://docs.djangoproject.com/en/4.1/)
- [Django Viewflow](https://github.com/viewflow/viewflow/)
