#!/usr/bin/python
#
# Send joint values to UR5 using messages
#

from trajectory_msgs.msg import JointTrajectory
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectoryPoint
import rospy


def main():

    rospy.init_node('send_joints')
    pub = rospy.Publisher('/trajectory_controller/command',
                          JointTrajectory,
                          queue_size=10)

    # Create the topic message
    traj = JointTrajectory()
    traj.header = Header()
    # Joint names for UR5
    traj.joint_names = ['shoulder_pan_joint', 'shoulder_lift_joint',
                        'elbow_joint', 'wrist_1_joint', 'wrist_2_joint',
                        'wrist_3_joint']

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        traj.header.stamp = rospy.Time.now()
        pts = JointTrajectoryPoint()
        pts.positions = [0.180397344042591, -0.46159712847377854,  0.34107758901149676,-1.8290689486244203, -0.45481156632822817, 1.9918058620776087]
        pts.time_from_start = rospy.Duration(2.0)

        # Set the points to the trajectory
        traj.points = []
        traj.points.append(pts)
        # Publish the message
        pub.publish(traj)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print ("Program interrupted before completion")
