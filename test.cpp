    struct BoneEntry {
      String BoneName;
      String ParentBoneName;
      U32 BoneAttributes;

      F32 BoneLength;

      // Bone Displacement
      F32 BoneDisplacementX;
      F32 BoneDisplacementY;
      F32 BoneDisplacementZ;

      // Bone Orientation
      F32 BoneOrientationW;
      F32 BoneOrientationX;
      F32 BoneOrientationY;
      F32 BoneOrientationZ;

      // Could be not present, see bone attributes
      U32 BoneLinkCount;
      F32 BoneLinkLength;

      // Bone Start Joint, could be not present
      F32 StartJointCenterU;
      F32 StartJointCenterV;
      F32 StartJointScaleU;
      F32 StartJointScaleV;

      F32 EndJointCenterU;
      F32 EndJointCenterV;
      F32 EndJointScaleU;
      F32 EndJointScaleV;

      // Bone Rotation Constraints
      F32 RotationConstraintXMax;
      F32 RotationConstraintXMin;
      F32 RotationConstraintYMax;
      F32 RotationConstraintYMin;
      F32 RotationConstraintZMax;
      F32 RotationConstraintZMin;
    };