// Generated by gencpp from file robotiq_ft_sensor/sensor_accessorResponse.msg
// DO NOT EDIT!


#ifndef ROBOTIQ_FT_SENSOR_MESSAGE_SENSOR_ACCESSORRESPONSE_H
#define ROBOTIQ_FT_SENSOR_MESSAGE_SENSOR_ACCESSORRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace robotiq_ft_sensor
{
template <class ContainerAllocator>
struct sensor_accessorResponse_
{
  typedef sensor_accessorResponse_<ContainerAllocator> Type;

  sensor_accessorResponse_()
    : success(false)
    , res()  {
    }
  sensor_accessorResponse_(const ContainerAllocator& _alloc)
    : success(false)
    , res(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _res_type;
  _res_type res;





  typedef boost::shared_ptr< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> const> ConstPtr;

}; // struct sensor_accessorResponse_

typedef ::robotiq_ft_sensor::sensor_accessorResponse_<std::allocator<void> > sensor_accessorResponse;

typedef boost::shared_ptr< ::robotiq_ft_sensor::sensor_accessorResponse > sensor_accessorResponsePtr;
typedef boost::shared_ptr< ::robotiq_ft_sensor::sensor_accessorResponse const> sensor_accessorResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robotiq_ft_sensor

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'robotiq_ft_sensor': ['/home/burak/catkin_ws/src/robotiq/robotiq_ft_sensor/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2adcefa00ba94fe7b359ee9018245fbf";
  }

  static const char* value(const ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2adcefa00ba94fe7ULL;
  static const uint64_t static_value2 = 0xb359ee9018245fbfULL;
};

template<class ContainerAllocator>
struct DataType< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robotiq_ft_sensor/sensor_accessorResponse";
  }

  static const char* value(const ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n\
string res\n\
\n\
";
  }

  static const char* value(const ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
      stream.next(m.res);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct sensor_accessorResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robotiq_ft_sensor::sensor_accessorResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
    s << indent << "res: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.res);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOTIQ_FT_SENSOR_MESSAGE_SENSOR_ACCESSORRESPONSE_H