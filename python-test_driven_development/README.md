📘 Python - Test-Driven Development

🧠 Description

Ce projet met en pratique la méthode de Test-Driven Development (TDD) en Python. L’objectif est de concevoir un petit système de quiz, en écrivant d’abord les tests et la documentation avant d’implémenter le code.

Le but est de renforcer une démarche de codage rigoureuse et centrée sur la validation des comportements attendus, en anticipant tous les cas possibles, y compris les cas limites.

⸻

🎯 Objectifs pédagogiques

À l’issue de ce projet, vous serez capable de :
	•	Expliquer l’intérêt des tests en Python
	•	Rédiger des docstrings utilisables comme tests automatiques avec doctest
	•	Documenter correctement vos modules et fonctions
	•	Écrire des tests couvrant les cas normaux et les cas limites
	•	Utiliser les options de base de doctest
	•	Comprendre et appliquer le Test-Driven Development

⸻

🧰 Technologies & Outils
	•	Python 3.8.5
	•	doctest pour les tests
	•	Éditeurs autorisés : vi, vim, emacs
	•	Norme de style : pycodestyle (v2.7.*)
	•	Environnement : Ubuntu 20.04 LTS

⸻

🧪 Structure des tests
	•	Tous les tests se trouvent dans le dossier tests/
	•	Les fichiers de test ont l’extension .txt
	•	Les tests s’exécutent avec la commande :
    ```python3 -m doctest ./tests/*```
    •	Les modules et fonctions sont obligatoirement documentés

⸻

📁 Organisation du projet
.
├── my_module.py            # Exemple de module Python
├── tests/
│   └── test_my_module.txt  # Fichiers de test Doctest
├── README.md               # Ce fichier

🧼 Contraintes
	•	Tous les fichiers doivent être exécutables (chmod +x)
	•	Chaque fichier doit se terminer par une ligne vide
	•	La première ligne doit être : #!/usr/bin/python3
	•	Respect strict de la norme PEP8 (via pycodestyle)
	•	Les fichiers seront testés avec wc pour vérifier leur longueur

⸻

📚 Ressources utiles
	•	doctest – Test interactive Python examples
	•	Unit Testing in Python
	•	PEP 257 – Docstring Conventions

⸻

⚠️ Recommandations
	•	N’implémentez rien sans avoir écrit les tests au préalable !
	•	Travaillez en groupe sur les tests et les cas limites, jamais sur l’implémentation
	•	Ne faites jamais confiance à l’utilisateur
	•	Pensez toujours aux edge cases (entrée vide, mauvaise saisie, etc.)

⸻

✅ Bonnes pratiques
	•	Écrivez une documentation claire pour chaque module et fonction
	•	Rédigez des tests lisibles et exhaustifs
	•	Utilisez des noms de fonctions explicites
	•	Testez souvent pendant le développement

⸻

🚀 Happy TDD coding!