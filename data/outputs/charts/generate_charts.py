from src.visualization import Visualization
import pandas as pd

# Load loss data from CSV file
loss_data_path = 'data/inputs/portfolio_loss_data.csv'  # Update if the file path differs
losses = pd.read_csv(loss_data_path)["Losses"]

# Generate and save the loss distribution chart
Visualization.plot_loss_distribution(losses)

print("Loss distribution chart has been saved in 'data/outputs/charts/portfolio_loss_distribution.png'")
