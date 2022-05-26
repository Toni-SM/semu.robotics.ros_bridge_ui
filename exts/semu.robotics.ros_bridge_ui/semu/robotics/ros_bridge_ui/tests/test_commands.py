# NOTE:
#   omni.kit.test - std python's unittest module with additional wrapping to add suport for async/await tests
#   For most things refer to unittest docs: https://docs.python.org/3/library/unittest.html
import omni.kit.test
import omni.kit.usd
import gc

# Import extension python module we are testing with absolute import path, as if we are external user (other extension)
import omni.kit.commands


# Having a test class dervived from omni.kit.test.AsyncTestCase declared on the root of module will make it auto-discoverable by omni.kit.test
class TestRosBridgeCommands(omni.kit.test.AsyncTestCaseFailOnLogError):
    # Before running each test
    async def setUp(self):
        await omni.usd.get_context().new_stage_async()
        self._timeline = omni.timeline.get_timeline_interface()
        self._stage = omni.usd.get_context().get_stage()

    # After running each test
    async def tearDown(self):
        self._stage = None
        self._timeline = None
        gc.collect()

    # Run all commands
    async def test_ros_command(self):
        print("test_ros_command - ROSBridgeCreateAttribute")
        result, prim = omni.kit.commands.execute("ROSBridgeCreateAttribute", 
                                                 path="/ROS_Attribute")
        
        print("test_ros_command - ROSControlBridgeCreateFollowJointTrajectory")
        result, prim = omni.kit.commands.execute("ROSControlBridgeCreateFollowJointTrajectory", 
                                                  path="/ROSControl_FollowJointTrajectory")
        
        print("test_ros_command - ROSControlBridgeCreateGripperCommand")
        result, prim = omni.kit.commands.execute("ROSControlBridgeCreateGripperCommand", 
                                                  path="/ROSControl_GripperCommand")
        
        self._timeline.play()
        await omni.kit.app.get_app().next_update_async()
        await omni.kit.app.get_app().next_update_async()
