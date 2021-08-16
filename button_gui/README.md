# button_gui

This package contains one node button_gui.py

When running, a window appears with a button, when the button has been clicked a topic named "/button_state" is updated.

## To install this package

clone it into the src folder in your catkin workspace

```sh
cd ~/catkin_ws/src
git clone https://github.com/Kramoth/button_gui.git
catkin build
source ~/catkin_ws/devel/setup.bash
```
## To run this node
Once the setup file has been sourced.

```sh
rosrun button_gui button_gui
```
