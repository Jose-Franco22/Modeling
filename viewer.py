import mujoco
from mujoco.viewer import launch    


model = mujoco.MjModel.from_xml_path("myo_sim/arm/myoarm.xml") 
# model = mujoco.MjModel.from_xml_path("Loco-Mujoco/skeleton/skeleton_muscle.xml") 
# model = mujoco.MjModel.from_xml_path("New\skeleton\skeleton_muscle.xml") 


data = mujoco.MjData(model)

    

# Simulation duration
# Launch the viewer
with launch(model, data) as viewer:
    print(".")
    