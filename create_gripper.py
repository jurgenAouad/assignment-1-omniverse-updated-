# create_gripper.py
from pxr import Usd, UsdGeom

file_path = "C:/Users/test/Documents/Assignment1/usda/gripper.usda"
stage     = Usd.Stage.CreateNew(file_path)

# Make a small cube as the gripper
cube = UsdGeom.Cube.Define(stage, "/Gripper/Cube")
cube.GetSizeAttr().Set(0.2)

stage.GetRootLayer().Save()
