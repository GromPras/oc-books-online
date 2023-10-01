# Utilisez les bases de Python pour l'analyse de marché

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
