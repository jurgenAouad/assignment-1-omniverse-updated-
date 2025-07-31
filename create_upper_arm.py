# create_upper_arm.py
from pxr import Usd, UsdGeom

# 1. Path to your USDA
file_path = "C:/Users/test/Documents/Assignment1/usda/upper_arm.usda"

# 2. Create a new stage (overwrites if it exists)
stage = Usd.Stage.CreateNew(file_path)

# 3. Define the Xform prim at /UpperArm
upper_xform = UsdGeom.Xform.Define(stage, "/UpperArm")

# 4. Add a rotateXYZ op (45° around Y)
rotateOp = upper_xform.AddRotateXYZOp()
rotateOp.Set((0.0, 0.0, -45.0))

# 5. Add a scale op (0.3, 1.2, 0.3)
scaleOp = upper_xform.AddScaleOp()
scaleOp.Set((0.3, 1.2, 0.3))

# 6. Under that Xform, define a Cube
cube = UsdGeom.Cube.Define(stage, "/UpperArm/Cube")
cube.GetSizeAttr().Set(1.0)

# 7. Save to disk
stage.GetRootLayer().Save()

