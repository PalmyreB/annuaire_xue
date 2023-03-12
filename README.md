# Annuaire XUE

## Présentation

Ce dépôt contient un annuaire qui permet de recommander des contacts intéressants, sous la forme d'une application Django. Ce projet est né au sein de l'association X-Urgence écologique (XUE).

## Prérequis

- [Python](https://www.python.org/downloads/)
- [Django](https://docs.djangoproject.com/en/4.1/topics/install/)

## Installation du projet

1. Cloner le projet

   ```sh
   git clone https://github.com/PalmyreB/annuaire_xue.git
   ```

2. Se rendre dans le dossier du projet

   ```sh
   cd annuaire_xue
   ```

3. Créer un environnement virtuel

   ```sh
   python -m venv venv
   ```

4. Activer l'environnement virtuel

   ```sh
   source venv/Scripts/activate
   ```

5. Installer les _requirements_

   ```sh
   pip install -r requirements.txt
   ```

6. Créer un fichier nommé `.env` avec la clé secrète communiquée par un administrateur (à défaut, pour des tests locaux, une clé arbitraire – ne pas mettre les accolades dans cette commande)

   ```sh
   echo -e "SECRET_KEY={votre clé secrète}\nSECRET_KEY_FALLBACKS=" > .env
   ```

7. Lancer les migrations

   ```sh
   python manage.py migrate
   ```

8. Créer un profil de super-utilisateur

   ```sh
   python manage.py createsuperuser
   ```

## Lancer le projet

Avec l'environnement virtuel actuel, lancer la commande suivante depuis la racine

```sh
python manage.py runserver
```

Se rendre à l'adresse <http://127.0.0.1:8000/entrees/>.

La connexion se fait sur la page <http://127.0.0.1:8000/admin/>.

## Contribuer au projet

Vous pouvez :

- corriger le code, l'améliorer, traiter un ticket sur la page des _issues_ et créer une PR,
- faire remonter les dysfonctionnements ou les suggestions d'amélioration en créant des _issues_.

## Ressources

- [Documentation Django](https://docs.djangoproject.com/en/4.1/)
- [Django Material](https://github.com/viewflow/django-material/)

## À faire

### Projet

- [ ] Passage à PostgreSQL ?
- [ ] Wiki GitHub pour expliquer aux admins les manips ?
- [ ] Hébergement (application + base de données)
- [ ] Méthode de gestion de projet : tâches en tant qu'issues ?

### Code

- [ ] CSS : améliorer les styles ? remplacer Django Material par [AdminLTE](https://adminlte.io/) ou autre ?
- [ ] Formulaires contacts recommandés
  - [x] Bouton « + » (formulaires groupés)
  - [ ] Bouton « - » pour supprimer des formulaires contacts recommandés (pour le moment, case à cocher « Supprimer »)
  - [ ] Une page par formulaire (une pour le contact principal et une par contact recommandé) pour éviter les bugs actuels
- [ ] Page avec tous les contacts et des filtres, notamment par domaine de compétence
  - [ ] Faciliter le contact des référents
- [ ] Modus operandi
- [ ] Bouton pour s'inscrire soi-même en tant que contact recommandé
  - Remplit et grise les champs redondants (nom, etc.)
- [ ] Amélioration de l'interface admin pour chercher et modifier/supprimer rapidement des contacts
- [ ] Gestion des doublons
  - Même référent : message « Il semble que vous ayez déjà inscrit ce contact. Voulez-vous remplacer des informations, en créer un nouveau ou annuler ? » + affichage du contact existant
  - Référent différent : affichage du contact existant, proposition de l'ajouter quand même ; une seule ligne dans les tableaux, avec tous les noms des référents
- [ ] Gestion de l'inscription d'un contact recommandé comme contact référent
  - On peut le garder comme contact recommandé, pour conserver ce pourquoi d'autres personnes le recommandent, amis faire un lien vers sa fiche de contact référent
- [ ] Fiches pour les contacts, qui reprennent leurs informations et font un lien vers leurs contacts recommandés / référents
- [ ] Comptes pour protéger la consultation de l'annuaire ? (autre solution : mot de passe)
  - [ ] Permettre aux utilisateurs de modifier leurs infos persos
  - [ ] Permettre aux utilisateurs de retrouver leur liste de contacts recommandés, de les modifier et de les supprimer
- [ ] Bug sur le champ « Domaines de compétence » à l'ajout de formulaires de contacts recommandés
- [ ] Bug sur le formulaire avec plusieurs contacts recommandés, lorsque l'on essaie de valider le formulaire sans tous les champs requis
- [ ] Factorisation de left-panel et right-panel ?
