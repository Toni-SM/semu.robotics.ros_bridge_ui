import carb
from pxr import Gf
import omni.kit.commands

import omni.add_on.RosControlBridgeSchema as ROSControlSchema
import omni.add_on.RosBridgeSchema as ROSSchema


class ROSControlBridgeCreateFollowJointTrajectory(omni.kit.commands.Command):
    def __init__(
        self,
        path: str = "/ROSControl_FollowJointTrajectory",
        parent=None,
        enabled: bool = True,
        controller_name: str = "/robot_controller",
        action_namespace: str = "/follow_joint_trajectory",
        articulation_prim_rel=None,
    ):
        # condensed way to copy all input arguments into self with an underscore prefix
        for name, value in vars().items():
            if name != "self":
                setattr(self, f"_{name}", value)
        self._prim = None

    def do(self) -> bool:
        success, self._prim = omni.kit.commands.execute(
            "RosBridgeCreatePrim",
            path=self._path,
            parent=self._parent,
            enabled=self._enabled,
            scehma_type=ROSControlSchema.RosControlFollowJointTrajectory,
        )
        if success and self._prim:
            rel_paths = self._prim.CreateArticulationPrimRel()
            if self._articulation_prim_rel is not None:
                if len(self._articulation_prim_rel) == 1:
                    rel_paths.AddTarget(self._articulation_prim_rel[0])
                else:
                    carb.log_warn("only one articulation prim rel target can be specified")
            self._prim.CreateControllerNameAttr(self._controller_name)
            self._prim.CreateActionNamespaceAttr(self._action_namespace)
        return self._prim

    def undo(self):
        pass


class ROSControlBridgeCreateGripperCommand(omni.kit.commands.Command):
    def __init__(
        self,
        path: str = "/ROSControl_GripperCommand",
        parent=None,
        enabled: bool = True,
        controller_name: str = "/gripper_controller",
        action_namespace: str = "/gripper_command",
        articulation_prim_rel=None,
    ):
        # condensed way to copy all input arguments into self with an underscore prefix
        for name, value in vars().items():
            if name != "self":
                setattr(self, f"_{name}", value)
        self._prim = None

    def do(self) -> bool:
        success, self._prim = omni.kit.commands.execute(
            "RosBridgeCreatePrim",
            path=self._path,
            parent=self._parent,
            enabled=self._enabled,
            scehma_type=ROSControlSchema.RosControlGripperCommand,
        )
        if success and self._prim:
            rel_paths = self._prim.CreateArticulationPrimRel()
            if self._articulation_prim_rel is not None:
                if len(self._articulation_prim_rel) == 1:
                    rel_paths.AddTarget(self._articulation_prim_rel[0])
                else:
                    carb.log_warn("only one articulation prim rel target can be specified")
            self._prim.CreateControllerNameAttr(self._controller_name)
            self._prim.CreateActionNamespaceAttr(self._action_namespace)
        return self._prim

    def undo(self):
        pass


class ROSBridgeCreateCompressedCamera(omni.kit.commands.Command):
    def __init__(
        self,
        path: str = "/ROS_CompressedCamera",
        parent=None,
        enabled: bool = True,
        queue_size: int = 10,
        frame_id: str = "sim_camera",
        rgb_enabled: bool = False,
        rgb_topic: str = "/rgb_compressed",
        depth_enabled: bool = False,
        depth_topic: str = "/depth_compressed",
        camera_prim_rel=None,
        resolution: Gf.Vec2i = Gf.Vec2i(1280, 720),
    ):
        # condensed way to copy all input arguments into self with an underscore prefix
        for name, value in vars().items():
            if name != "self":
                setattr(self, f"_{name}", value)
        self._prim = None

    def do(self) -> bool:
        success, self._prim = omni.kit.commands.execute(
            "RosBridgeCreatePrim",
            path=self._path,
            parent=self._parent,
            enabled=self._enabled,
            scehma_type=ROSSchema.RosCompressedCamera,
        )
        if success and self._prim:
            rel_paths = self._prim.CreateCameraPrimRel()
            if self._camera_prim_rel is not None:
                if len(self._camera_prim_rel) == 1:
                    rel_paths.AddTarget(self._camera_prim_rel[0])
                else:
                    carb.log_warn("only one camera prim rel target can be specified")
            self._prim.CreateResolutionAttr(self._resolution)
            self._prim.CreateRgbPubTopicAttr(self._rgb_topic)
            self._prim.CreateDepthPubTopicAttr(self._depth_topic)
            self._prim.CreateFrameIdAttr(self._frame_id)
            self._prim.CreateRgbEnabledAttr(self._rgb_enabled)
            self._prim.CreateDepthEnabledAttr(self._depth_enabled)
            self._prim.CreateQueueSizeAttr(self._queue_size)
        return self._prim


class ROSBridgeCreateAttribute(omni.kit.commands.Command):
    def __init__(
        self,
        path: str = "/ROS_Attribute",
        parent=None,
        enabled: bool = True,
        prims_service_topic: str = "/get_prims",
        attributes_service_topic: str = "/get_attributes",
        get_attr_service_topic: str = "/get_attribute",
        set_attr_service_topic: str = "/set_attribute"
    ):
        # condensed way to copy all input arguments into self with an underscore prefix
        for name, value in vars().items():
            if name != "self":
                setattr(self, f"_{name}", value)
        self._prim = None

    def do(self) -> bool:
        success, self._prim = omni.kit.commands.execute(
            "RosBridgeCreatePrim",
            path=self._path,
            parent=self._parent,
            enabled=self._enabled,
            scehma_type=ROSSchema.RosAttribute,
        )
        if success and self._prim:
            self._prim.CreatePrimsSrvTopicAttr(self._prims_service_topic)
            self._prim.CreateAttributesSrvTopicAttr(self._attributes_service_topic)
            self._prim.CreateGetAttrSrvTopicAttr(self._get_attr_service_topic)
            self._prim.CreateSetAttrSrvTopicAttr(self._set_attr_service_topic)
        return self._prim


omni.kit.commands.register_all_commands_in_module(__name__)
