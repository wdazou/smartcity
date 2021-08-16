
# button_gui

Ce package contient un nœud button_gui.py

Lors de l'exécution, une fenêtre apparaît avec un bouton, lorsque le bouton a été cliqué un topic nommé "/button_state" est mis à jour.

A chaque fois que on appuie sur le button gui il envoie un true ou false et la pastille sera changer par consequence.

Vous pouvez voir le resultat du pastille dans src/web/index.html

## Pour installer ce paquet

copiez-les dans le dossier src de votre espace de travail catkin

```sh
git clone https://github.com/wdazou/smartcity
cp -r smartcity/pastilleweb ~/catkin_ws/src
cp -r smartcity/button_gui ~/catkin_ws/src
cd ~/catkin_ws
catkin build
source ~/catkin_ws/devel/setup.bash

```
dans le cas où le copie marche pas remplace smartcity par 'smartcity-main'
## Pour exécuter ce nœud
Une fois que le fichier d'installation a été sourcé.

```sh
rosrun button_gui button_node.py
rosrun pastilleweb httpserver.py
```

