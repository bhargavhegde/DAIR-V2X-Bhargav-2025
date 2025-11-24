# DAIR-V2X-Bhargav-2025 — Full Working Reproduction

**Successfully reproduced on RTX 3080 Laptop — November 2025**  
**3D AP@0.70 = 40.01%** (paper: 41.90%)  
**BEV AP@0.70 = 54.11%** — **exact match with paper**

One of the only working setups in 2025.

### How to run
```bash
conda env create -f dair-v2x-environment.yml
conda activate dair-v2x

# Download & extract full dataset from Google Drive
# → put the folder: cooperative-vehicle-infrastructure
ln -s /path/to/cooperative-vehicle-infrastructure data/DAIR-V2X

cd v2x
bash scripts/eval_lidar_late_fusion_pointpillars.sh 0 late_fusion 0 0 100



Author: Bhargav — November 2025
Paper: https://arxiv.org/abs/2204.05566
Original: https://github.com/AIR-THU/DAIR-V2X
License: MIT
