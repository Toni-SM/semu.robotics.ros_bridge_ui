## ROS Bridge UI (add-on) for NVIDIA Omniverse Isaac Sim

> This extension enables the **menu and commands** of the of the ROS interfaces for the **ROS add-ons extensions**. The components are compatible with both [ROS](https://www.ros.org/) and [ROS2](https://www.ros.org/)

<br>

### Table of Contents

- [Prerequisites](#prerequisites)
- [Add the extension to NVIDIA Omniverse Isaac Sim and enable it](#extension)
- [Menu items](#menu)
- [Supported commands](#commands)

<br>

<a name="prerequisites"></a>
### Prerequisites

This extension requires the following extensions to be present in the Isaac Sim extension path:

- [omni.usd.schema.add_on](https://github.com/Toni-SM/omni.usd.schema.add_on): USD add-on schemas

<br>

<a name="extension"></a>
### Add the extension to NVIDIA Omniverse Isaac Sim and enable it

1. Add the the extension by following the steps described in [Extension Search Paths](https://docs.omniverse.nvidia.com/py/kit/docs/guide/extensions.html#extension-search-paths) or simply download and unzip the latest [release](https://github.com/Toni-SM/omni.add_on.ros_bridge_ui/releases) in one of the extension folders such as ```PATH_TO_OMNIVERSE_APP/exts```

    Git url (git+https) as extension search path: 
    
    ```
    git+https://github.com/Toni-SM/omni.add_on.ros_bridge_ui.git?branch=main&dir=exts
    ```

2. Enable the extension by following the steps described in [Extension Enabling/Disabling](https://docs.omniverse.nvidia.com/py/kit/docs/guide/extensions.html#extension-enabling-disabling)

<br>

<a name="menu"></a>
### Menu items

The following items will be created under the *Create > Isaac* menu once the extension is activated

* *Create > Isaac > ROS*

  * *Compressed Camera*

  * *Attribute*

* *Create > Isaac > ROS Control*

  * *Follow Joint Trajectory*

  * *Gripper Command*

Menu items (preview)

<p align="center">
  <img src="https://user-images.githubusercontent.com/22400377/139479274-6783f4c2-e948-4aac-858d-aac6a8cf9928.png" width="60%">
</p>

<br>

<a name="commands"></a>
### Supported commands

The following commands are supported:

* **Compressed Camera:** [CompressedImage](https://docs.ros.org/en/api/sensor_msgs/html/msg/CompressedImage.html) message type (ROS publisher)

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

* **Attribute:** Get or set prim attributes (ROS service)

    ```python
    class ROSBridgeCreateAttribute(
        path: str = "/ROS_Attribute",
        parent = None,
        enabled: bool = True,
        prims_service_topic: str = "/get_prims",
        attributes_service_topic: str = "/get_attributes",
        get_attr_service_topic: str = "/get_attribute",
        set_attr_service_topic: str = "/set_attribute"
    )
    ```

* **Follow Joint Trajectory:** [FollowJointTrajectory](http://docs.ros.org/en/api/control_msgs/html/action/FollowJointTrajectory.html) action type (ROS action)
    
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
* **Gripper Command:** [GripperCommand](http://docs.ros.org/en/api/control_msgs/html/action/GripperCommand.html) action type (ROS action)

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
