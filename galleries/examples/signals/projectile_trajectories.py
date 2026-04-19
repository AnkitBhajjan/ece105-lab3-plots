"""
Projectile Trajectories

This example demonstrates the parabolic trajectories of projectiles launched
at different angles. It shows how launch angle affects the range and maximum
height of a projectile, which is essential for understanding ballistics and
physics simulations.
"""

import matplotlib.pyplot as plt
import numpy as np

# Parameters
v0 = 10.0  # initial velocity (m/s)
g = 9.81   # gravity (m/s^2)
angles = [30, 45, 60]  # launch angles in degrees

fig, ax = plt.subplots(figsize=(8, 6))

for angle_deg in angles:
    angle_rad = np.deg2rad(angle_deg)
    # Time of flight: when y=0 again
    t_flight = 2 * v0 * np.sin(angle_rad) / g
    t = np.linspace(0, t_flight, 100)
    
    x = v0 * np.cos(angle_rad) * t
    y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2
    
    ax.plot(x, y, label=f'{angle_deg}°')

ax.set_xlabel('Distance (m)')
ax.set_ylabel('Height (m)')
ax.set_title('Projectile Trajectories at Different Launch Angles')
ax.set_aspect('equal')
ax.legend()
ax.grid(True, alpha=0.3)

plt.show()