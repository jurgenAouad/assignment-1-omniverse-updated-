from pxr import Usd, UsdGeom

# 1. Path 
file_path = "C:/Users/test/Documents/Assignment1/usda/base.usda"

# 2. Create a new stage 
stage = Usd.Stage.CreateNew(file_path)

# 3. Define the Xform
base_xform = UsdGeom.Xform.Define(stage, "/Base")

# 4. Add rotate
rotateOp = base_xform.AddRotateXYZOp()
rotateOp.Set((90.0, 0.0, 0.0))

# 6. Under that Xform, define a Cylinder
cyl = UsdGeom.Cylinder.Define(stage, "/Base/Cylinder")
cyl.GetHeightAttr().Set(0.2)
cyl.GetRadiusAttr().Set(0.5)

# 7. Save 
stage.GetRootLayer().Save()


