#!/usr/bin/env python  
import roslib
import rospy
import tf
import geometry_msgs.msg
import numpy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Quaternion, Pose, Point, Vector3
from std_msgs.msg import Header, ColorRGBA

def makeArrow(id,position,frame_id,color):
    (start,end)=(Point(),Point())
    start.x = position[0]
    start.y = position[1]
    start.z = position[2]
    end.x=0
    end.y=0
    end.z=0

    marker = Marker(
                type=Marker.ARROW,
                id=id,
                lifetime=rospy.Duration(0.05),
                scale=Vector3(0.02, 0.05, 0.01),
                header=Header(frame_id=frame_id),
                color=color)
		
    marker.points.append(start)
    marker.points.append(end)

    #print str(marker)
    return marker

def makeRectangle(id, point1, point2, frame_id, color):
    marker = Marker(
                type=Marker.CUBE,
                id=id,
                lifetime=rospy.Duration(0.05),
                color=color)
    rect_pose = Pose()
    rect_pose.position.x = (point1.x - point2.x) / 2.0 + point2.x
    rect_pose.position.y = (point1.y - point2.y) / 2.0 + point2.y
    rect_pose.position.z = (point1.z - point2.z) / 2.0 + point2.z
    marker.pose = rect_pose
    marker.scale.x = numpy.fabs(point1.x - point2.x)
    marker.scale.y = numpy.fabs(point1.y - point2.y)
    marker.scale.z = 0.05
    marker.header.frame_id = frame_id
    return marker

def makeTable(id, frame_id,scale,pose,file_name):
    marker = Marker(
                type=Marker.MESH_RESOURCE,
                id=id,
                header=Header(frame_id=frame_id)
    )
    marker.scale = scale
    marker.pose = pose
    marker.mesh_resource = file_name
    marker.mesh_use_embedded_materials = True
    return marker

if __name__ == '__main__':
     rospy.init_node('my_tf_listener')
     listener = tf.TransformListener()
     rate = rospy.Rate(100)

#list of how bodyparts are connected when they are broadcasted

     l = [["BodyPart:1", "BodyPart:2",ColorRGBA(1, 0.145, 0.058, 0.8)], ["BodyPart:1", "BodyPart:5",ColorRGBA(1, 0.407, 0.058, 0.8)],
          ["BodyPart:2", "BodyPart:3",ColorRGBA(1, 0.698, 0.058, 0.8)], ["BodyPart:5", "BodyPart:6",ColorRGBA(0.560, 1, 0.058, 0.8)],
          ["BodyPart:3", "BodyPart:4",ColorRGBA(0.949, 1, 0.058, 0.8)], ["BodyPart:6", "BodyPart:7",ColorRGBA(0.058, 1, 0.274, 0.8)],
          ["BodyPart:1", "BodyPart:8",ColorRGBA(0.058, 1, 0.478, 0.8)], ["BodyPart:1", "BodyPart:11",ColorRGBA(0.058, 1, 0.992, 0.8)],
          ["BodyPart:8", "BodyPart:9",ColorRGBA(0.058, 1, 0.337, 0.8)], ["BodyPart:11", "BodyPart:12",ColorRGBA(0.058, 0.588, 1, 0.8)],
          ["BodyPart:9", "BodyPart:10",ColorRGBA(0.058, 1, 0.827, 0.8)], ["BodyPart:12", "BodyPart:13",ColorRGBA(0.058, 0.207, 1, 0.8)],
          ["BodyPart:1", "BodyPart:0",ColorRGBA(0.058, 0.207, 1, 0.8)], ["BodyPart:0", "BodyPart:14",ColorRGBA(0.4, 0.109, 0.729, 0.8)],
          ["BodyPart:0", "BodyPart:15",ColorRGBA(1, 0.121, 0.909, 0.8)], ["BodyPart:14", "BodyPart:16",ColorRGBA(0.666, 0.305, 0.792, 0.8)],
          ["BodyPart:15", "BodyPart:17",ColorRGBA(0.956, 0.164, 0.462, 0.8)]
         ]
     while not rospy.is_shutdown():
         try:
             time = rospy.Time()
             marker_publisher = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=1000)
             markerArray = MarkerArray()

#create rectangular surface by giving two points
             rectangle = makeRectangle(1, Point(-0.75,-0.32,0), Point(0.75,0.32,0),"table",ColorRGBA(0.666, 0.305, 0.792, 1.0))
             markerArray.markers.append(rectangle)
             P = Pose(Point(1.62,0.7,-1.58),Quaternion(0,0,0,1))
             scale = Vector3(2.6,2.6,2.6)
             mesh_file2 = "package://ur_description/meshes/complete_table.dae"

#create yable by giving pose and scale
             #mesh = makeTable(2,"new_Frame",scale,P,mesh_file2)
             #markerArray.markers.append(mesh)
             frame_id = 3

#adds bodypart markers to marker array to be published
   
             for i in l:
                #listener.waitForTransform(i[0], i[1], time, rospy.Duration(1.0))
                try:
                    (trans,rot) = listener.lookupTransform(i[0], i[1], time)
                    marker = makeArrow(frame_id,trans,i[0],i[2])
                    markerArray.markers.append(marker)
                    frame_id += 1
                except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
                    #print(e)
                    continue

         
	     marker_publisher.publish(markerArray)
             #rate.sleep()
         except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
             continue
