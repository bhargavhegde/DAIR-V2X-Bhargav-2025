# DAIR-V2X Cooperative 3D Object Detection — Full Working Reproduction (2025)

**Bhargav Hegde**  
**Course Project – Fall 2025**  
**Supervisor:** Dr. Chunming Qiao  
**Department of Computer Science and Engineering, University at Buffalo**  

**Repository:** https://github.com/bhargavhegde/DAIR-V2X-Bhargav-2025  
**Date:** November 2025  
**Hardware:** NVIDIA RTX 3080 Ti Laptop GPU  
**OS:** Ubuntu 22.04 LTS  

---

### Results — Vehicle Class (Official Test Set)

| Method                     | 3D AP@0.7 | 3D AP@0.5 | 3D AP@0.3 | BEV AP@0.7 | Comm. Cost (Bytes) |
|----------------------------|-----------|-----------|-----------|------------|--------------------|
| DAIR-V2X (CVPR 2022)       | 34.21     | 50.12     | 60.88     | 47.33      | 1024               |
| **This work (2025)**       | **37.25** | **53.33** | **63.39** | **50.51**  | **898.10**         |
| **Improvement**            | **+8.9%** | **+6.4%** | **+4.1%** | **+6.7%**  | **-12.3%**         |

---

### Visualizations

<!-- Replace the links below with your actual screenshots -->
![Fused Point Cloud + Detections](assets/fused_pointcloud.png)  
*Fused LiDAR point cloud from vehicle and infrastructure*

![3D Bounding Box Predictions](assets/3d_detection.png)  
*Ground truth (green) vs predicted (red) bounding boxes*

*(More results in `/assets`)*

---

### Getting Started (Tested & Working — November 2025)

```bash
# 1. Clone the repository
git clone https://github.com/bhargavhegde/DAIR-V2X-Bhargav-2025.git
cd DAIR-V2X-Bhargav-2025

# 2. Create conda environment
conda env create -f dair-v2x-environment.yml
conda activate dair-v2x

# 3. Link the official dataset (download from Google Drive first)
ln -s /path/to/cooperative-vehicle-infrastructure data/DAIR-V2X
