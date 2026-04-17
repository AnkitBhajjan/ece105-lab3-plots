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
