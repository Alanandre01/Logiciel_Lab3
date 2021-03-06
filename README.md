# Lab 3 - Création d’un interface Python

## Auteur

Laboratoire créé par Alan Brucher

## Installation

Pour installer le projet, utilisez le bouton "Open with Visual Studio" situé dans "Code".

**Verifiez que vous utilisez Python 3.10 et que vous êtes en Debug x64**

Dans les propriétés du projet C++, remplacer VC++ Directories->Include et VC++ Directories->Directories pour avoir le bon path.

Si ce n'est pas déjà fait, modifier ces propriétés

- General -> Target Name = Lab3_Cpp
- General -> Configuration Type = Dynamic Library (.dll)
- Advanced -> Target File extension = .pyd

Compiler le projet.

Ouvrez "Lab3_Python.py" dans le dossier du même nom et modifier aussi le path du Debug à la ligne 7.

Lancer le projet en insérant ceci (avec le bon path) dans l'invite de commandes:

```bash
python C:\Users\...\Lab3_Python\Lab3_Python.py
```

Dès l'apparition de la fenêtre, appuyez sur le bouton "Select video file" et selectionnez la vidéo "Exemple.avi":

Utilisez les autres boutons pour effectuer le contrôle de la vidéo:

- Play/Pause - Lancer ou mettre en pause la vidéo
- Stop - Arrêter la vidéo
- Back to start - Retourner au début de la vidéo
- Quit - Fermer la fenêtre 

## Sources 

Librairie Keyboard: https://github.com/boppreh/keyboard#api

https://stackoverflow.com/questions/24072790/how-to-detect-key-presses

PyObject* to String: https://docs.python.org/3/c-api/unicode.html

String to LPCWSTR: https://www.codegrepper.com/code-examples/cpp/c%2B%2B+convert+const+char%2A+to+LPCWSTR

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
