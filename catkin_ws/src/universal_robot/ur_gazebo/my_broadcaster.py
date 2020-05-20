#! /usr/bin/env python
 
from tf import TransformBroadcaster
import rospy
from rospy import Time 
 
def main():
    rospy.init_node('my_broadcaster')
    
    b = TransformBroadcaster()
    
    translation = (0.0, 0.0, 0.0)
    rotation = (0.0, 0.0, 0.0, 1.0)
    rate = rospy.Rate(5)  # 5hz
    
    x, y = 0.0, 0.0
    
    while not rospy.is_shutdown():
        if x >= 2:
            x, y = 0.0, 0.0 
        
        x += 0.1
        y += 0.1
        
        translation = (x, y, 0.0)
        
        b.sendTransform((-0.06,0.51,0.03), rotation, Time.now(), 'BodyPart:10', '/new_Frame') 
	b.sendTransform((0.06, 0.47, 0.03), rotation, Time.now(), 'BodyPart:13', '/new_Frame')
        b.sendTransform((-0.06,0.48,0.3), rotation, Time.now(), 'BodyPart:9', '/new_Frame')
	b.sendTransform((0.06, 0.52, 0.3), rotation, Time.now(), 'BodyPart:12', '/new_Frame')
        b.sendTransform((-0.06,0.45,0.65), rotation, Time.now(), 'BodyPart:8', '/new_Frame')
	b.sendTransform((0.05, 0.62, 0.65), rotation, Time.now(), 'BodyPart:11', '/new_Frame')
	b.sendTransform((0, 0.5, 1.35), rotation, Time.now(), 'BodyPart:1', '/new_Frame')
        b.sendTransform((-0.09,0.5,1.32), rotation, Time.now(), 'BodyPart:2', '/new_Frame')
	b.sendTransform((0.1, 0.47, 1.36), rotation, Time.now(), 'BodyPart:5', '/new_Frame')
        b.sendTransform((-0.19,0.5,1.12), rotation, Time.now(), 'BodyPart:3', '/new_Frame')
	b.sendTransform((0.21, 0.47, 1.16), rotation, Time.now(), 'BodyPart:6', '/new_Frame')
        b.sendTransform((-0.39,0.5,1.12), rotation, Time.now(), 'BodyPart:4', '/new_Frame')
	b.sendTransform((0.21, 0.47, 1.16), rotation, Time.now(), 'BodyPart:7', '/new_Frame')
	b.sendTransform((0, 0.45, 1.57), rotation, Time.now(), 'BodyPart:0', '/new_Frame')
        b.sendTransform((-0.03,0.5,1.60), rotation, Time.now(), 'BodyPart:14', '/new_Frame')
	b.sendTransform((0.02, 0.47, 1.62), rotation, Time.now(), 'BodyPart:15', '/new_Frame')
        b.sendTransform((-0.06,0.5,1.63), rotation, Time.now(), 'BodyPart:16', '/new_Frame')
	b.sendTransform((0.05, 0.47, 1.64), rotation, Time.now(), 'BodyPart:17', '/new_Frame')
        b.sendTransform((0, -0.6, 0.9), rotation, Time.now(), 'world', '/new_Frame')
        b.sendTransform((0, 0, 0.6), rotation, Time.now(), 'table', '/new_Frame')

        rate.sleep()
    
 
 
if __name__ == '__main__':
    main()
