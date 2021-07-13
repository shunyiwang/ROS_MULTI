#include <ros/ros.h>
#include "riki_base.h"

int main(int argc, char** argv )
{
    ros::init(argc, argv, "riki_base_node");
    RikiBase riki;
    ros::spin();
    return 0;
}
