# README

## Projet d'Entreprise IMT Atlantique 2023
### Groupe : Réalisation d'une visionneuse numérique 9.5mm pour la Cinémathèque de Bretagne

---

### camera.py

Ce script (`camera.py`) est conçu pour fonctionner avec la caméra Raspberry Pi HQ Camera v1.0. Cette caméra, dotée d'un capteur Sony IMX477R rétroéclairé de 12,3 mégapixels, offre des spécifications impressionnantes à un prix abordable. Voici quelques détails sur la caméra :

- Capteur Sony IMX477R rétroéclairé, 12,3 mégapixels, diagonale de 7,9 mm
- Pixels de 1,55 μm × 1,55 μm
- Sortie : RAW12/10/8, COMP8
- Distance de mise au point arrière : Ajustable (12,5 mm–22,4 mm)
- Normes de l'objectif : Monture C, Monture CS (adaptateur C-CS inclus)
- Filtre coupe-infrarouge : Intégré
- Longueur du câble ruban : 200 mm
- Montage sur trépied : 1/4”-20

#### Configuration de la caméra :
1. Assurez-vous d'avoir la caméra Raspberry Pi HQ connectée.
2. Ouvrez la configuration Raspberry Pi en exécutant `sudo raspi-config`.
3. Activez "Camera" dans la configuration et redémarrez votre Raspberry Pi.

#### Ajustement de la mise au point :
Si vous souhaitez ajuster la mise au point de la caméra, installez l'outil V4L2 Test Bench avec la commande :
```bash
sudo apt-get install qv4l2
```
Chargez le module dans le kernel :
```bash
sudo modprobe bcm2835-qv4l2
```
Exécutez l'outil :
```bash
qv4l2
```

Cet outil vous permettra d'obtenir une vue en temps réel de votre caméra, ce qui facilitera l'ajustement de la mise au point, de l'éclairage, du contraste, etc.

#### Capture d'images avec Raspistill :
Utilisez Raspistill pour capturer des images haute résolution. Exemple :
```bash
raspistill -o test.jpg
```

#### Remarques finales :
- Il est recommandé d'explorer les nombreuses options offertes par Raspistill pour personnaliser la capture d'images.

---

### dc_motor.py

Ce script (`dc_motor.py`) contrôle le moteur destiné à faire défiler les trames de film dans la visionneuse numérique. Le moteur est piloté par un circuit L293D et peut être configuré pour différentes actions.

#### Configuration du moteur :
1. Assurez-vous d'avoir les bibliothèques nécessaires installées avec `sudo apt-get install python3-rpi.gpio`.
2. Connectez le moteur selon les spécifications du circuit L293D.

#### Utilisation du script :
- Le script surveille l'état d'un bouton GPIO (Broche 2) pour déclencher une action.

#### Exemple d'utilisation :
- Exécutez le script et appuyez sur le bouton GPIO pour observer le message "Button was pushed!".

#### Remarques finales :
- Explorez les possibilités offertes par le script pour personnaliser les actions du moteur selon les besoins du projet.

---

**Note :** Assurez-vous que votre Raspberry Pi est correctement configurée et que toutes les dépendances nécessaires sont installées avant d'exécuter les scripts. Vous pouvez adapter les configurations matérielles dans les scripts en fonction des besoins spécifiques de votre projet.