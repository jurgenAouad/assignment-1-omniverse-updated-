# final_robot.py

from pxr import Usd, UsdGeom

BASE_DIR = "C:/Users/test/Documents/Assignment1/usda"

# Map prim names to their USD filenames
PART_FILES = {
    "Base":      "base.usda",
    "LowerArm":  "lower_arm.usda",
    "UpperArm":  "upper_arm.usda",
    "Gripper":   "gripper.usda",
}

# 1) Create robot stage
stage = Usd.Stage.CreateNew(f"{BASE_DIR}/robot.usda")
robot = UsdGeom.Xform.Define(stage, "/Robot")

def addRef(name, parent, translate=(0.0, 0.0, 0.0)):
    
    prim_path = parent.GetPath().AppendChild(name)
    wrapper = UsdGeom.Xform.Define(stage, prim_path)

    
    file_name = PART_FILES[name]
    wrapper.GetPrim().GetReferences().AddReference(
        f"{BASE_DIR}/{file_name}",
        f"/{name}"
    )

    translateOp = wrapper.AddTranslateOp()
    translateOp.Set(translate)

    return wrapper

# 2) adjust positions
addRef("Base",     robot, translate=(0.0, 0.0, 0.0))
addRef("LowerArm", robot, translate=(0.0, 0.6, 0.0))
addRef("UpperArm", robot, translate=(-2.8, 1.1, 0.0))
addRef("Gripper",  robot, translate=(0.9, 2.1, 0.0))

# 3) Save 
stage.GetRootLayer().Save()
