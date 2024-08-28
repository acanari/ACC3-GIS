# -*- coding: utf-8 -*-
"""
This file is part of Project PositViPy.
Copyright (c) 2024 ACC3-gis
This code is licensed under the MIT License.
See the LICENSE file in the project root for license terms.
"""
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Path to the .asc file
file_path = 'directory+file'
output_dir = 'output directory'
# Function to read the .asc file
def read_asc_file(file_path):
    with open(file_path, 'r') as file:
        # Read the header
        ncols = int(file.readline().split()[1])
        nrows = int(file.readline().split()[1])
        xllcorner = float(file.readline().split()[1])
        yllcorner = float(file.readline().split()[1])
        cellsize = float(file.readline().split()[1])
        nodata_value = file.readline().split()[1]  # Could be "Nan"
        
        # Read the data
        data = np.loadtxt(file, skiprows=0)
        
    return ncols, nrows, xllcorner, yllcorner, cellsize, nodata_value, data

# Read the .asc file
ncols, nrows, xllcorner, yllcorner, cellsize, nodata_value, data = read_asc_file(file_path)

# Create the meshgrid for visualization with correct dimensions
x = np.linspace(xllcorner, xllcorner + (ncols - 1) * cellsize, ncols)
y = np.linspace(yllcorner, yllcorner + (nrows - 1) * cellsize, nrows)
X, Y = np.meshgrid(x, y)

# 3D Visualization
fig1 = plt.figure(figsize=(10, 7), dpi=150)  # Increased DPI for higher resolution
ax1 = fig1.add_subplot(111, projection='3d')
surf = ax1.plot_surface(X, Y, data, cmap='viridis', edgecolor='none')
ax1.set_xlabel('X (Distance)')
ax1.set_ylabel('Y (Distance)')
ax1.set_zlabel('Z (Depth)')
ax1.set_title('3D Visualization TheBat test')
fig1.colorbar(surf, ax=ax1, shrink=0.8, aspect=15)

# Adding contour labels for Z values (Depth)
ax1.contour(X, Y, data, zdir='z', offset=np.min(data), cmap='viridis')

# Adjust the view angle of the 3D plot to better visualize depth
ax1.view_init(elev=20, azim=-60)  # Adjust these parameters to change the view

# Save the 3D visualization
output_3d_path = os.path.join(output_dir, '3D_Bathymetry.png')
plt.savefig(output_3d_path)
# Show the 3D visualization
plt.show()

# 2D Visualization
fig2 = plt.figure(figsize=(10, 7), dpi=150)  # Increased DPI for higher resolution
ax2 = fig2.add_subplot(111)
c = ax2.contourf(X, Y, data, cmap='viridis')
ax2.set_xlabel('X (Distance)')
ax2.set_ylabel('Y (Distance)')
ax2.set_title('2D Visualization TheBat test')
fig2.colorbar(c, ax=ax2)

# Save the 2D visualization
output_2d_path = os.path.join(output_dir, '2D_Bathymetry.png')
plt.savefig(output_2d_path)
# Show the 2D visualization
plt.show()


