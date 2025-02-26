import pandas as pd
from scipy.stats import linregress

# Load dataset
df = pd.read_csv("players_stats_by_season_full_details.csv")

# Filter for NBA Regular Season data
df_filtered = df[(df["League"] == "NBA") & (df["Stage"] == "Regular_Season")]

# Find the player with the most seasons played
player_season_counts = df_filtered.groupby("Player")["Season"].nunique()
most_seasons_player = player_season_counts.idxmax()

# Filter data for Vince Carter
vc_data = df_filtered[df_filtered["Player"] == most_seasons_player].copy()

# Convert Season to numerical values (extract starting year)
vc_data["Season_Year"] = vc_data["Season"].str.split(" - ").str[0].astype(int)

# Calculate three-point accuracy (3PM / 3PA), handling division by zero
vc_data["3P_Accuracy"] = vc_data["3PM"] / vc_data["3PA"]
vc_data["3P_Accuracy"].fillna(0, inplace=True)  # Replace NaNs with 0 if attempts were 0

# Perform linear regression on three-point accuracy over seasons
slope, intercept, r_value, p_value, std_err = linregress(vc_data["Season_Year"], vc_data["3P_Accuracy"])

# Generate line of best fit values
vc_data["3P_Fit"] = slope * vc_data["Season_Year"] + intercept

# Display the calculated values
print(vc_data[["Season", "3PM", "3PA", "3P_Accuracy", "3P_Fit"]].head())
