import pandas as pd
from scipy.stats import linregress

df = pd.read_csv("players_stats_by_season_full_details.csv")

df_filtered = df[(df["League"] == "NBA") & (df["Stage"] == "Regular_Season")]

player_season_counts = df_filtered.groupby("Player")["Season"].nunique()
most_seasons_player = player_season_counts.idxmax()

vc_data = df_filtered[df_filtered["Player"] == most_seasons_player].copy()

vc_data["Season_Year"] = vc_data["Season"].str.split(" - ").str[0].astype(int)

vc_data["3P_Accuracy"] = vc_data["3PM"] / vc_data["3PA"]
vc_data["3P_Accuracy"].fillna(0, inplace=True)  # Replace NaNs with 0 if attempts were 0

slope, intercept, r_value, p_value, std_err = linregress(vc_data["Season_Year"], vc_data["3P_Accuracy"])

vc_data["3P_Fit"] = slope * vc_data["Season_Year"] + intercept

print(vc_data[["Season", "3PM", "3PA", "3P_Accuracy", "3P_Fit"]].head())
