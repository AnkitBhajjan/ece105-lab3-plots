# ECE105 Lab 3: Sensor Data Plots

A Python script that generates synthetic temperature sensor data and creates publication-quality visualizations.

## Installation

1. Activate the `ece105` conda environment:
   ```
   conda activate ece105
   ```

2. Install the required dependencies:
   ```
   conda install numpy matplotlib
   ```
   or
   ```
   mamba install numpy matplotlib
   ```

## Usage

Run the script from the command line:
```
python generate_plots.py
```

## Example Output

The script generates a single PNG file `sensor_analysis.png` containing three subplots:

1. **Scatter Plot**: Temperature readings from Sensor A (blue) and Sensor B (orange) plotted against time in seconds, showing the temporal distribution of measurements.

2. **Histogram**: Overlaid histograms of temperature distributions for both sensors with vertical lines indicating the mean temperature for each sensor.

3. **Box Plot**: Side-by-side box plots comparing the temperature distributions of both sensors, with a horizontal line showing the overall mean temperature across both sensors.

## AI Tools Used and Disclosure

[Placeholder: Describe any AI tools or assistance used in developing this project.]