NBA Regular Season Data Analysis

Project Overview

This project looks at NBA regular season stats using Python and SciPy. The goal is to find interesting patterns in player performance and shooting trends.

Data Source

The data comes from Kaggle:Players Stats by Season - Full Details

What This Project Does

1. Data Filtering

Focuses only on NBA regular season games.

Finds the player who played the most seasons.

2. Three-Point Shooting Analysis

Calculates three-point accuracy for that player over the years.

Uses linear regression to see how their accuracy changed.

Fills in missing data for 2002-2003 and 2015-2016 using interpolation.

3. Shooting Stats Analysis

Finds average, variance, skew, and kurtosis for:

Field Goals Made (FGM) (successful shots)

Field Goals Attempted (FGA) (total shots taken)

Runs t-tests to compare FGM and FGA.

How to Use This Project

Requirements

You need Python and these packages:

pip install pandas numpy scipy matplotlib

Running the Code

To run the analysis as a script:

python analysis.py

If using Jupyter Notebook:

jupyter notebook

Files in This Project

analysis.py / analysis.ipynb – The main code for the analysis.

README.md – This file explaining the project.

chat_log.txt – A record of AI assistance used in the project.

Key Findings

Vince Carter played the most regular seasons (19 years).

His three-point accuracy changed over time but followed a pattern.

The stats show a strong connection between shots taken and shots made.

Limitations

Some data might be incomplete or inconsistent.

The project doesn’t consider factors like team strategies or rule changes.

