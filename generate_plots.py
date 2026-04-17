"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np


def generate_data(seed):
    """Generate simulated temperature sensor data and timestamps.
    
    Creates synthetic temperature readings from two sensors using a 
    seeded random number generator. Sensor A has a mean of 25°C with 
    standard deviation of 3°C, while Sensor B has a mean of 27°C with 
    standard deviation of 4.5°C. Timestamps are uniformly distributed 
    across a 10-second interval.
    
    Parameters
    ----------
    seed : int
        Random seed for reproducible data generation. Typically the last 
        4 digits of your Drexel ID.
    
    Returns
    -------
    sensor_a : ndarray
        Temperature readings from Sensor A, shape (200,).
    sensor_b : ndarray
        Temperature readings from Sensor B, shape (200,).
    timestamps : ndarray
        Timestamps in seconds, shape (200,).
    """
    rng = np.random.default_rng(seed)
    
    # Generate temperature readings
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    
    # Generate timestamps
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)
    
    return sensor_a, sensor_b, timestamps


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot temperature sensor data as a scatter plot.
    
    Draws scatter points for both sensors as a function of time on the 
    given Axes object. Sensor A points are blue and Sensor B points are 
    orange with transparency to show overlapping points.
    
    Parameters
    ----------
    sensor_a : ndarray
        Temperature readings from Sensor A, shape (n,).
    sensor_b : ndarray
        Temperature readings from Sensor B, shape (n,).
    timestamps : ndarray
        Timestamps in seconds, shape (n,).
    ax : matplotlib.axes.Axes
        Axes object on which to draw the scatter plot.
    
    Returns
    -------
    None
        Modifies the Axes object in place.
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A', alpha=0.6)
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B', alpha=0.6)
    
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Readings from Two Sensors')
    ax.legend()
    ax.grid(True, alpha=0.3)


def plot_histogram(sensor_a, sensor_b, ax):
    """Plot overlaid histograms of temperature distributions from both sensors.
    
    Draws transparent overlaid histograms for Sensor A (blue) and Sensor B 
    (orange) distributions. Vertical dashed lines indicate the mean 
    temperature for each sensor.
    
    Parameters
    ----------
    sensor_a : ndarray
        Temperature readings from Sensor A, shape (n,).
    sensor_b : ndarray
        Temperature readings from Sensor B, shape (n,).
    ax : matplotlib.axes.Axes
        Axes object on which to draw the histogram.
    
    Returns
    -------
    None
        Modifies the Axes object in place.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, color='blue', label='Sensor A')
    ax.hist(sensor_b, bins=30, alpha=0.5, color='orange', label='Sensor B')
    
    # Add vertical dashed lines at each sensor's mean
    mean_a = sensor_a.mean()
    mean_b = sensor_b.mean()
    ax.axvline(mean_a, color='blue', linestyle='--', linewidth=2, label=f'Mean A: {mean_a:.2f}°C')
    ax.axvline(mean_b, color='orange', linestyle='--', linewidth=2, label=f'Mean B: {mean_b:.2f}°C')
    
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Temperature Distribution: Sensor A vs Sensor B')
    ax.legend()
    ax.grid(True, alpha=0.3)