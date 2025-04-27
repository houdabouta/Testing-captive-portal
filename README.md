# Testing Captive Portal

## Description du projet
Ce projet est un script Python qui permet de :
- Ouvrir un navigateur (Google Chrome)
- Charger des URLs de portails captifs pour différents SSID
- Attendre que la page affiche "CONNEXION WI-FI" (ou expirer après 15 secondes)
- Prendre une capture d'écran
- Sauvegarder la capture avec le nom du SSID

Utile pour vérifier que chaque page du portail captif s'affiche correctement.

---

## Prérequis

- Python 3.x installé (testé avec Python 3.11)
- Google Chrome installé
- Chromedriver téléchargé manuellement et placé dans `/usr/local/bin`
- Environnement macOS (script adapté pour Mac)

---

## Étapes d'installation

1. **Créer et activer un environnement virtuel Python (recommandé) :**

```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Créer un fichier `requirements.txt`** contenant :

```text
selenium
```

3. **Installer les paquets nécessaires :**

```bash
pip install -r requirements.txt
```

4. **Télécharger manuellement le bon Chromedriver :**

- Accéder à : https://googlechromelabs.github.io/chrome-for-testing/
- Sélectionner la version correspondant à votre navigateur Chrome (ex : 135.0.7049.115)
- Télécharger la version `mac-x64` ou `mac-arm64` selon votre modèle de Mac
- Extraire et déplacer `chromedriver` dans `/usr/local/bin/` :

```bash
sudo mv /chemin/vers/chromedriver /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```

5. **Vérifier l'installation de Chromedriver :**

```bash
chromedriver --version
```
(Doit afficher quelque chose comme ChromeDriver 135.x)

---

## Exécution du script

Avant de lancer le script :

- **Mettre à jour manuellement la variable `base_url`** dans le fichier `testing_ssid_display.py`.
- Par défaut, elle est définie ainsi :
  
```python
base_url = "https://VOTRE_SPLASH_PAGE_URI_ICI"
```

- Vous devez remplacer `"https://VOTRE_SPLASH_PAGE_URI_ICI"` par l'URI d'une **Splash Page** choisie dans la section **Locations** de votre espace d'administration Cloudi-Fi.

Exécuter ensuite :

```bash
python testing_ssid_display.py
```

Le script va :
- Tester tous les SSID (EDU_CAMPUS, EDU_ADMIN, EDU_INVITE)
- Construire automatiquement les URLs avec les SSIDs
- Sauvegarder des captures d'écran sous forme de fichiers `EDU_CAMPUS_screenshot.png`, etc.
- Continuer même si une page ne se charge pas complètement

---

## Remarques importantes

- Pour exécuter le navigateur en arrière-plan, décommentez l'option `headless` dans le script.
- Vérifiez toujours que la version de Chromedriver correspond à votre version de Chrome.
- Les captures d'écran sont enregistrées dans le même dossier que le script.
- Si une page n'affiche pas "CONNEXION WI-FI", le script prend quand même une capture et passe au SSID suivant.

---

## Résolution de problèmes

- Si vous voyez `OSError: [Errno 8] Exec format error`, cela signifie que le mauvais fichier chromedriver a été utilisé.
- Téléchargez toujours chromedriver manuellement sous macOS, sans passer par `webdriver-manager`.
- En cas de mise à jour de Chrome, téléchargez un nouveau chromedriver adapté.
- Si la page met trop de temps à charger, le script attendra 15 secondes avant de passer au SSID suivant.