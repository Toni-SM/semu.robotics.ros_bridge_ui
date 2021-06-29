# omni.add_on.ros_bridge_ui
ROS Bridge UI (add-on) for NVIDIA Omniverse Isaac Sim

> This extension enables the **menu and commands** of the **ROS interfaces that are used for general purpose and robot control**

The components are compatible with both [ROS](https://www.ros.org/) and [ROS2](https://www.ros.org/). 

They can be created from the following menus:

* *Create > Isaac > ROS*
  * *Compressed Camera*
* *Create > Isaac > ROS Control*
  * *Follow Joint Trajectory*
  * *Gripper Command*

<br>

### Table of Contents

- [Prerequisites](#prerequisites)
- [Add the extension to NVIDIA Omniverse Isaac Sim and enable it](#extension)
- [Supported commands](#commands)

<br>

<a name="prerequisites"></a>
### Prerequisites

This extension requires the following extensions to be present in the Isaac Sim's extension path:

* [omni.usd.schema.add_on](https://github.com/Toni-SM/omni.usd.schema.add_on): USD add-on schemas

<br>

<a name="extension"></a>
### Add the extension to NVIDIA Omniverse Isaac Sim and enable it

1. Download the latest [release](https://github.com/Toni-SM/omni.add_on.ros_bridge_ui/releases), or any release according to your Isaac Sim version, and unzip it into the Isaac Sim's extension path (```/isaac-sim/exts``` for containers or ```~/.local/share/ov/pkg/isaac_sim-2021.1.0/exts``` for native workstations)
2. Enable the extension in the menu *Window > Extensions* under the same name

<br>

<a name="commands"></a>
### Supported commands

The following commands are supported:

* **Compressed Camera:** [CompressedImage](https://docs.ros.org/en/api/sensor_msgs/html/msg/CompressedImage.html) message type 

    ```python
    class ROSBridgeCreateCompressedCamera(
        path: str = "/ROS_CompressedCamera",
        parent = None,
        enabled: bool = True,
        queue_size: int = 10,
        frame_id: str = "sim_camera",
        rgb_enabled: bool = False,
        rgb_topic: str = "/rgb_compressed",
        depth_enabled: bool = False,
        depth_topic: str = "/depth_compressed",
        camera_prim_rel = None,
        resolution: Gf.Vec2i = Gf.Vec2i(1280, 720)
    )
    ```

* **Follow Joint Trajectory:** [FollowJointTrajectory](http://docs.ros.org/en/api/control_msgs/html/action/FollowJointTrajectory.html) action service
    
    ```python
    class ROSControlBridgeCreateFollowJointTrajectory(
        path: str = "/ROSControl_FollowJointTrajectory",
        parent = None,
        enabled: bool = True,
        controller_name: str = "/robot_controller",
        action_namespace: str = "/follow_joint_trajectory",
        articulation_prim_rel = None
    )
    ```
* **Gripper Command:** [GripperCommand](http://docs.ros.org/en/api/control_msgs/html/action/GripperCommand.html) action service

    ```python
    class ROSControlBridgeCreateGripperCommand(
        path: str = "/ROSControl_GripperCommand",
        parent = None,
        enabled: bool = True,
        controller_name: str = "/gripper_controller",
        action_namespace: str = "/gripper_command",
        articulation_prim_rel = None
    )
    ```
