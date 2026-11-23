# Gestionnaire de tâches

Application Django permettant de créer, consulter, modifier et supprimer des tâches.

## Prérequis

- Python 3.12 ou supérieur
- `pip`

## Installation

Depuis le dossier du projet :

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
```

Si l'exécution de scripts PowerShell est bloquée, activez temporairement l'environnement avec :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## Lancement

```powershell
python manage.py runserver
```

Puis ouvrez <http://127.0.0.1:8000/> dans votre navigateur.

Pour arrêter le serveur, utilisez `Ctrl+C`.

## Tests

```powershell
python manage.py test
```

## Administration

Pour accéder à l'administration Django, créez d'abord un compte administrateur :

```powershell
python manage.py createsuperuser
```
