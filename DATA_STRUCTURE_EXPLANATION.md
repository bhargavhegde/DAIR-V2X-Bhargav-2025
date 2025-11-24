# DAIR-V2X Data Structure Explanation

## 📁 Complete Directory Structure

```
/home/bhargav/Desktop/oppa/DAIR-V2X/
│
├── data/
│   ├── DAIR-V2X/                                    ← SYMLINK LOCATION (what script uses)
│   │   └── cooperative-vehicle-infrastructure ────┐
│   │                                               │ SYMLINK
│   ├── DAIR-V2X-C_full/                           │ (points to)
│   │   └── cooperative-vehicle-infrastructure/    │
│   │       (EMPTY - 4KB placeholder)              │
│   │                                               │
│   └── downloaded data/                            │
│       ├── cooperative-vehicle-infrastructure ────┘ ← PHYSICAL DATA (29GB)
│       │   ├── infrastructure-side/
│       │   │   ├── velodyne/      (point clouds)
│       │   │   ├── image/         (images - currently empty)
│       │   │   ├── calib/         (calibration files)
│       │   │   ├── label/         (labels)
│       │   │   └── data_info.json
│       │   │
│       │   ├── vehicle-side/
│       │   │   ├── velodyne/      (point clouds)
│       │   │   ├── image/         (images - 2.6GB)
│       │   │   ├── calib/         (calibration files)
│       │   │   ├── label/         (labels)
│       │   │   └── data_info.json
│       │   │
│       │   └── cooperative/
│       │       ├── label_world/   (cooperative labels)
│       │       └── data_info.json
│       │
│       ├── cooperative-vehicle-infrastructure-vehicle-side-image/
│       │   (EMPTY - files were moved to main folder)
│       │
│       ├── cooperative-vehicle-infrastructure-infrastructure-side-velodyne/
│       │   (EMPTY - files were moved to main folder)
│       │
│       └── cooperative-vehicle-infrastructure-vehicle-side-velodyne/
│           (EMPTY - files were moved to main folder)
│
└── v2x/
    └── scripts/
        └── eval_lidar_late_fusion_pointpillars.sh
            Uses: ../data/DAIR-V2X/cooperative-vehicle-infrastructure
```

## 🔗 Data Flow (How Script Accesses Data)

```
1. Script Location:
   v2x/scripts/eval_lidar_late_fusion_pointpillars.sh
   
2. Script uses relative path:
   DATA="../data/DAIR-V2X/cooperative-vehicle-infrastructure"
   
3. Resolves to absolute path:
   /home/bhargav/Desktop/oppa/DAIR-V2X/data/DAIR-V2X/cooperative-vehicle-infrastructure
   
4. This is a SYMLINK that points to:
   /home/bhargav/Desktop/oppa/DAIR-V2X/data/downloaded data/cooperative-vehicle-infrastructure
   
5. Physical data location (where files actually are):
   /home/bhargav/Desktop/oppa/DAIR-V2X/data/downloaded data/cooperative-vehicle-infrastructure/
   ├── infrastructure-side/  (with velodyne, calib, label, data_info.json)
   ├── vehicle-side/         (with velodyne, image, calib, label, data_info.json)
   └── cooperative/           (with label_world, data_info.json)
```

## ✅ What's Correct

1. **Physical Data Location**: 
   - `data/downloaded data/cooperative-vehicle-infrastructure/` (29GB)
   - Contains all actual files (point clouds, images, labels, etc.)

2. **Symlink**:
   - `data/DAIR-V2X/cooperative-vehicle-infrastructure` → points to physical data
   - This is the CORRECT setup per documentation

3. **Script Access**:
   - Script uses `../data/DAIR-V2X/cooperative-vehicle-infrastructure`
   - Resolves through symlink to actual data
   - ✅ Working correctly (inference is running)

## ❓ About Empty Folders

**Why are these folders empty?**
- `cooperative-vehicle-infrastructure-vehicle-side-image/` - EMPTY
- `cooperative-vehicle-infrastructure-infrastructure-side-velodyne/` - EMPTY  
- `cooperative-vehicle-infrastructure-vehicle-side-velodyne/` - EMPTY

**Explanation:**
- These were separate zip files you extracted
- The `organize_dataset.sh` script MOVED all files from these folders into the main `cooperative-vehicle-infrastructure/` folder
- After moving, these folders became empty
- **Safe to delete** - they're just leftovers

## ❓ About DAIR-V2X-C_full

**What is it?**
- `data/DAIR-V2X-C_full/cooperative-vehicle-infrastructure/` - EMPTY (4KB)
- This appears to be a placeholder or incomplete download
- **NOT being used** - the script uses the symlink, not this folder

## 🎯 Summary

**Current Setup (CORRECT):**
- ✅ Physical data: `data/downloaded data/cooperative-vehicle-infrastructure/` (29GB)
- ✅ Symlink: `data/DAIR-V2X/cooperative-vehicle-infrastructure` → points to physical data
- ✅ Script accesses: `../data/DAIR-V2X/cooperative-vehicle-infrastructure` → resolves via symlink
- ✅ Everything working (inference running successfully)

**What you can clean up:**
- Empty folders in `data/downloaded data/` (the `-vehicle-side-image`, `-infrastructure-side-velodyne`, etc.)
- Empty `data/DAIR-V2X-C_full/` folder (if you want)

**The data is in the RIGHT place!** The symlink setup is exactly what the documentation recommends.

