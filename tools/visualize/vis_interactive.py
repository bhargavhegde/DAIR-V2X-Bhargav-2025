"""
FINAL WORKING Interactive Viewer
→ Press SPACEBAR → next frame (smooth, no crash!)
→ Press 'q' or ESC → quit
→ Starts at frame 871
"""
import os
import os.path as osp
import numpy as np
import pickle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ============== SETTINGS ==============
RESULT_PATH = "/home/bhargav/Desktop/oppa/DAIR-V2X/cache/vic-late-lidar/result"
START_FRAME_ID = 871
SCORE_THRESH = 0.35          # set 0.0 to show all
# ======================================

# List all frames
frame_files = sorted([f for f in os.listdir(RESULT_PATH) if f.endswith('.pkl') and f[0].isdigit()])
frame_ids = [int(f.split('.')[0]) for f in frame_files]
print(f"Found {len(frame_ids)} frames. Starting from {START_FRAME_ID}")

try:
    current_idx = frame_ids.index(START_FRAME_ID)
except ValueError:
    current_idx = 0
    print(f"Frame {START_FRAME_ID} not found → starting from {frame_ids[0]}")

# Global variables
fig = None
ax = None
current_idx_global = current_idx

def box7d_to_corners(b):
    x,y,z,l,w,h,ry = b
    xc = [l/2,l/2,-l/2,-l/2,l/2,l/2,-l/2,-l/2]
    yc = [w/2,-w/2,-w/2,w/2,w/2,-w/2,-w/2,w/2]
    zc = [0,0,0,0,h,h,h,h]
    c = np.array([xc,yc,zc]).T
    R = np.array([[np.cos(ry),-np.sin(ry),0],[np.sin(ry),np.cos(ry),0],[0,0,1]])
    return (R @ c.T).T + [x,y,z]

def draw_box(corners, color='red', alpha=0.4):
    faces = [[0,1,2,3],[4,5,6,7],[0,1,5,4],[1,2,6,5],[2,3,7,6],[3,0,4,7]]
    for f in faces:
        ax.add_collection3d(Poly3DCollection([corners[f]], alpha=alpha, facecolor=color, edgecolor='k', linewidths=2))
    for i,j in [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]]:
        ax.plot(corners[[i,j],0], corners[[i,j],1], corners[[i,j],2], 'k', lw=2)

def update_frame():
    global ax, current_idx_global
    ax.clear()

    frame_id = frame_ids[current_idx_global]
    pkl_path = osp.join(RESULT_PATH, f"{frame_id:06d}.pkl")
    data = pickle.load(open(pkl_path, 'rb'))

    # Predictions
    pred_corners = np.array(data["boxes_3d"])
    if "scores" in data:
        scores = np.array(data["scores"])
        mask = scores >= SCORE_THRESH
        pred_corners = pred_corners[mask]
        print(f"Frame {frame_id}: {len(pred_corners)} predictions (≥{SCORE_THRESH})")
    else:
        print(f"Frame {frame_id}: {len(pred_corners)} predictions")

    # GT
    gt = data["label"]
    if gt.ndim == 2 and gt.shape[1] == 7:
        gt_corners = np.array([box7d_to_corners(b) for b in gt])
    else:
        gt_corners = gt.reshape(-1, 8, 3)

    # Draw
    for c in gt_corners:      draw_box(c, 'blue', 0.7)
    for c in pred_corners:    draw_box(c, 'red', 0.4)

    # Zoom & labels
    all_pts = np.vstack([pred_corners.reshape(-1,3), gt_corners.reshape(-1,3)])
    center = all_pts.mean(axis=0)
    extent = all_pts.ptp(axis=0).max()
    m = extent * 0.3
    ax.set_xlim(center[0]-extent/2-m, center[0]+extent/2+m)
    ax.set_ylim(center[1]-extent/2-m, center[1]+extent/2+m)
    ax.set_zlim(0, center[2]+15)
    ax.set_xlabel('X (m)'); ax.set_ylabel('Y (m)'); ax.set_zlabel('Z (m)')
    ax.set_title(f'Frame {frame_id} | RED=Pred | BLUE=GT | SPACE=Next | q=Quit')
    ax.view_init(elev=25, azim=-65)
    fig.canvas.draw_idle()

def on_key(event):
    global current_idx_global
    if event.key in [' ', 'space']:
        current_idx_global = (current_idx_global + 1) % len(frame_ids)
        update_frame()
    elif event.key in ['q', 'escape']:
        plt.close('all')

# Initial plot
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')
update_frame()
fig.canvas.mpl_connect('key_press_event', on_key)
plt.show()
