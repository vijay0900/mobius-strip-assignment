# Mobius Strip Assignment - Karkhana.io Internship

## Overview
This assignment models a 3D Mobius strip using Python. It includes code to generate the surface based on mathematical equations, and calculates its surface area and edge length. A 3D plot of the strip is also included to visualize the result.

## Code Structure
The solution is organized in a single Python class called `MobiusStrip`, which includes:
- Generating a 3D mesh grid using parametric equations
- Calculating the surface area using numerical integration (via cross products)
- Estimating edge length of the boundary
- A method to plot the Mobius strip using Matplotlib

## Surface Area Calculation
The surface area is estimated using a numerical method:
- I compute the partial derivatives of the (x, y, z) mesh
- Then I take the cross product of those vectors to get local surface elements
- The total surface area is calculated by summing these elements over the entire grid

## Challenges Faced
- Making sure the numerical calculations (gradients and surface areas) were accurate
- Handling edge cases where numerical instability could occur
- Visualizing a Mobius strip in 3D since it’s a non-orientable surface

## Files Included
- `mobius_strip.py`: The complete Python code for the Mobius strip model
- `plot.png`: A 3D plot of the strip generated using Matplotlib
- `README.md`: This file, explaining my approach

