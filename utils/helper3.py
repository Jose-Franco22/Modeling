import mujoco
# import mujoco.viewer 


# model = mujoco.MjModel.from_xml_path("myo_sim/arm/myoarm.xml") 
# model = mujoco.MjModel.from_xml_path("Loco-Mujoco/skeleton/skeleton_muscle.xml") 
model = mujoco.MjModel.from_xml_path("Loco-Mujoco/skeleton/skeleton_muscle_arm.xml") 


data = mujoco.MjData(model)
x =[]

# Print all actuator names
for i in range(model.nu):
    x.append(mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_ACTUATOR, i))


print(x)