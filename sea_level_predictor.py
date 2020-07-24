import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import sys

def draw_plot():
  # Read data from file
  sealvl = pd.read_csv('epa-sea-level.csv')
  sys.exit()
  # Create scatter plot


  # Create first line of best fit


  # Create second line of best fit


  # Add labels and title

  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()