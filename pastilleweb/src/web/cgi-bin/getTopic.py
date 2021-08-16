#!/usr/bin/env python 

import rospy
from std_msgs.msg import Bool



rospy.init_node("listener",anonymous=True)

 
#sub_once = rospy.Subscriber("button_state",Bool,callback)

msg = rospy.wait_for_message("button_state",Bool)

#print (msg.data)
msg = ("""{"valeur": %r}""" % msg.data).lower()

print ("Content-type:application/json\n")
print (msg)

