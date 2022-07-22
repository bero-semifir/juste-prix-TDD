# Juste prix en TDD

Cette application est un juste prix développé avec la méthodologie TDD

## Installer les dépendances

`pip install -r requirements.txt`

### liste des dépendances

- [Pytest](https://docs.pytest.org/en/7.1.x/): librairie de test
- [Pytest-cov](https://pypi.org/project/pytest-cov/): plugin pytest pour générer la couverture de test

## Lancer les tests

Lancer les test: `pytest`

Lancer les tests avec coverage: `pytest --cov=src .\tests\`  
--cov indique le chemin des fichiers à tester
.\tests indique le dossier des tests

Avec coverage en XML (exploitable par SonarQube ou les extensions): `pytest --cov-report xml --cov=src .\tests`
Avec coverage en HTML (Lisible dans un navigateur): `pytest --cov-report html --cov=src .\tests`

> Pytest-cov supporte d'[autres formats et options](https://pytest-cov.readthedocs.io/en/latest/reporting.html?highlight=report#reporting) de rapport si necessaire

## Rappel des règles TDD

### Red Green Refactor

- Red: On écris le test (description de ce qui est attendu pour la fonction)
- Green: On écris le minimum de code necessaire pour faire passer le test
- Refactor: Notre test couvre la fonctionnalité, on peut effectuer les modification en toute sécuritée... Sauf si le test repasse au Red

Un bug entraine une rédaction de test

![Red, green, refactor](https://miro.medium.com/max/1400/1*tZSwCigaTaJdovyWlp5uBQ.jpeg)

## Extension VSCode pour aider le test

Nom : Coverage Gutters
ID : ryanluker.vscode-coverage-gutters
Description : Display test coverage generated by lcov or xml - works with many languages
Version : 2.10.1
Serveur de publication : ryanluker
Lien de la Place de marché pour VS : https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters

Elle lit le fichier coverage.xml cf: [Lancer les tests](#lancer-les-tests) et affiche dans la goutière (à coté des numéro de ligne) si une instruction est couverte ou non par un test.
