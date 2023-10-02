# Utilisez les bases de Python pour l'analyse de marché

## Français

### Introduction

Un programme écrit en Python pour extraire les données du site http://books.toscrape.com/ qui:

- Liste les catégories de la page d'accueil
- Parcourt chaque catégorie pour récupérer les liens des livres
- Extrait les données du livre pour tous les liens et sauvegarde l'image de
  couverture dans un dossier dédié
- Sauvegarde les données sélectionnées dans un fichier csv (pour chaque catégorie)

### Installation

Pré-requis:

- Python >=3.6.0
- Git 2.X

```sh
git clone https://github.com/GromPras/oc-projet_2.git
```

`Ou téléchargez le fichier ZIP depuis https://github.com/GromPras/oc-projet_2/archive/refs/heads/main.zip`

Créez un environement virtuel à l'intérieur du dossier cloné:

```sh
cd oc-projet_2
python3 -m venv {/path/to/new/virtual/environment}
```

Sur Windows, appelez la commande venv comme suit :

```sh
c:\>c:\Python35\python -m venv c:\path\to\myenv
```

Activez l'environement virtuel :

```sh
source {/path/to/new/virtual/environment}/bin/activate
```

Sur Windows, appelez la commande venv comme suit :

```sh
C:\> <venv>\Scripts\activate.bat
```

Installez les packages requis :

```sh
pip install -r requirements.txt
```

Ou sur Windows :

```sh
py -m pip install -r requirements.txt
```

Si vous avez un problème avec la création de l'environnement consultez la documentation : `https://docs.python.org/fr/3/library/venv.html#creating-virtual-environments`

### Post Installation

Exécutez la commande suivante :

```sh
python3 src/main.py
```

## English

### Introduction

An executable python script to scrap data from http://books.toscrape.com/ that:

- List all categories from the home page
- Loops through each category to get the book's links
- Scrap book's data for each link and download the image in a dedicated folder
- Saves desired data in csv files (1 per category)

### Installation

Requirements:

- Python >=3.6.0
- Git 2.X

```sh
git clone https://github.com/GromPras/oc-projet_2.git
```

`Or download the ZIP from https://github.com/GromPras/oc-projet_2/archive/refs/heads/main.zip`

Create a virtual environment inside the cloned folder:

```sh
cd oc-projet_2
python3 -m venv {/path/to/new/virtual/environment}
```

Activate your newly created virtual environment

```sh
source {/path/to/new/virtual/environment}/bin/activate
```

Install required packages

```sh
pip install -r requirements.txt
```

### Post Installation

Run the following command to **scrap**!

```sh
python3 src/main.py
```
