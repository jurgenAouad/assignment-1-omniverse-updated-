in this updated assignment 1 part,
- create_base:  
  - Defines `/Base` Xform + Cylinder  
  - Rotate via `AddRotateXYZOp()`

- create_lower_arm:
  - Defines `/LowerArm` Xform + Cube  
  - Scale via `AddScaleOp()` or `XformCommonAPI.SetScale()`

- create_upper_arm: 
  - Defines `/UpperArm` Xform + Cube  
  - `AddRotateXYZOp()` and `AddScaleOp()`

- create_gripper: 
  - Defines `/Gripper` Xform + Sphere  

- final_robot:
  - Wraps each part in `/Robot`, positions with `AddTranslateOp()`, writes `robot.usda`
