import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Year"], data["CSIRO Adjusted Sea Level"])

    # Create first line of best fit (1880 → 2050)
    res_all = linregress(data["Year"], data["CSIRO Adjusted Sea Level"])
    x_all = np.arange(1880, 2051)
    y_all = res_all.intercept + res_all.slope * x_all
    plt.plot(x_all, y_all)

    # Create second line of best fit (2000 → 2050)
    data_recent = data[data["Year"] >= 2000]
    res_recent = linregress(data_recent["Year"], data_recent["CSIRO Adjusted Sea Level"])
    x_recent = np.arange(2000, 2051)
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    plt.plot(x_recent, y_recent)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Fix x ticks (the test checks them explicitly)
    plt.xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
