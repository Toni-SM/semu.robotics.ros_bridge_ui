import carb
import weakref
import omni.kit.commands

from omni.kit.menu.utils import add_menu_items, remove_menu_items, MenuItemDescription
from omni.isaac.ros_bridge_ui import RosBridgeMenu as BridgeMenu


class RosBridgeMenu:
    def __init__(self):
        self._menus = []

        menu_items_ros = [
            MenuItemDescription(name="Attribute", onclick_fn=lambda a=weakref.proxy(self): a.add_attribute())
        ]

        menu_items_ros_control = [
            MenuItemDescription(name="Follow Joint Trajectory", onclick_fn=lambda a=weakref.proxy(self): a.add_follow_joint_trajectory()),
            MenuItemDescription(name="Gripper Command", onclick_fn=lambda a=weakref.proxy(self): a.add_gripper_command()),
        ]

        self._menu_items = [
            MenuItemDescription(name="Isaac", sub_menu=[MenuItemDescription(name="ROS", sub_menu=menu_items_ros)]),
            MenuItemDescription(name="Isaac", sub_menu=[MenuItemDescription(name="ROS Control", sub_menu=menu_items_ros_control)])
        ]
        add_menu_items(self._menu_items, "Create")

    def add_attribute(self):
        result, prim = omni.kit.commands.execute(
            "ROSBridgeCreateAttribute", 
            path="/ROS_Attribute", parent=BridgeMenu._get_stage_and_path(self)
        )

    def add_follow_joint_trajectory(self):
        result, prim = omni.kit.commands.execute(
            "ROSControlBridgeCreateFollowJointTrajectory", 
            path="/ROSControl_FollowJointTrajectory", parent=BridgeMenu._get_stage_and_path(self)
        )

    def add_gripper_command(self):
        result, prim = omni.kit.commands.execute(
            "ROSControlBridgeCreateGripperCommand", 
            path="/ROSControl_GripperCommand", parent=BridgeMenu._get_stage_and_path(self)
        )

    def shutdown(self):
        remove_menu_items(self._menu_items, "Create")
        self._menus = None
