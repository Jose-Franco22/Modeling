import mujoco
import mujoco.viewer 


# model = mujoco.MjModel.from_xml_path("myo_sim/arm/myoarm.xml") 
# model = mujoco.MjModel.from_xml_path("Loco-Mujoco/skeleton/skeleton_muscle.xml") 
# model = mujoco.MjModel.from_xml_path("C:/Users/ng440/Desktop/SimplifiedModel/Modeling/Loco-Mujoco/skeleton/skeleton_muscle_arm_torso_joints.xml") 
model = mujoco.MjModel.from_xml_path("C:/Users/ng440/Desktop/SimplifiedModel/Modeling/Loco-Mujoco/skeleton/skeleton_muscle_arm_torso.xml") 


data = mujoco.MjData(model)

# with mujoco.viewer.launch_passive(model, data) as viewer:
#     # Change tendon visibility on the viewer's built-in option object
#     for i in range(6):
#         viewer.opt.tendongroup[i] = 0  # Hide tendon groups
    
#     for i in range(6):
#         viewer.opt.sitegroup[i] = 0    # Hide all site groups
#     viewer.opt.sitegroup[5] = 1        # Keep group 5 visible

#     while viewer.is_running():
#         mujoco.mj_step(model, data)

with mujoco.viewer.launch(model, data) as viewer:
    print()