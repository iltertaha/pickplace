#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Quaternion, Pose, Point, Vector3
from std_msgs.msg import Header, ColorRGBA

def makeSphere(frame_id, number):
    marker = Marker(
                type=Marker.SPHERE,
                id=number,
                lifetime=rospy.Duration(0.5),
                pose=Pose(Point(0, 0, 0), Quaternion(0, 0, 0, 1)),
                scale=Vector3(0.06, 0.06, 0.06),
                header=Header(frame_id=frame_id),
                color=ColorRGBA(1.0, 0.0, 0.0, 0.8)
		)
    return marker

def showMarkers(marker_publisher):
    markerArray = MarkerArray()
    for i in range(1, 4):
      name = "BodyPart:" + str(i)
      marker = makeSphere(name,i)
      markerArray.markers.append(marker)
    marker_publisher.publish(markerArray)


def wait_for_time():                                              
    """Wait for simulated time to begin.                          
    """                                                           
    while rospy.Time().now().to_sec() == 0:                       
        pass

def main():
  rospy.init_node('my_node')
  wait_for_time()
  rate = rospy.Rate(5)  # 5hz
  while not rospy.is_shutdown():
      marker_publisher = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=1000)                                                          
      showMarkers(marker_publisher) 
      #rate.sleep()

if __name__ == '__main__':
  main()
