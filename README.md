# smartcity
rattrapage smart city
# button_gui

Ce package contient un nœud button_gui.py

Lors de l'exécution, une fenêtre apparaît avec un bouton, lorsque le bouton a été cliqué un sujet nommé "/button_state" est mis à jour.

## Pour installer ce paquet

clonez-le dans le dossier src de votre espace de travail catkin

```sh
cd ~/catkin_ws/src
git clone https://github.com/Kramoth/button_gui.git
catkin build
source ~/catkin_ws/devel/setup.bash
```
## Pour exécuter ce nœud
Une fois que le fichier d'installation a été sourcé.

```sh
rosrun pastilleweb httpserver.py
```

