"""
This sample project is referenced from the CONDA  user guide:
https://conda.io/projects/conda/en/latest/user-guide/tasks/creating-projects.html
"""

import pandas as pd

def main():
    """
    Answer the question:

    What percentage of U.S. residents live in highly walkable neighborhoods?

    "15.26" is the threshold on the index for a highly walkable area.
    """
    csv_file = "./data/EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv"
    highly_walkable = 15.26

    df = pd.read_csv(csv_file)

    total_population = df["TotPop"].sum()
    highly_walkable_pop = df[df["NatWalkInd"] >= highly_walkable]["TotPop"].sum()

    percentage = (highly_walkable_pop / total_population) * 100.0

    print(
        f"{percentage:.2f}% of U.S. residents live in highly" "walkable neighborhoods."
    )

if __name__ == "__main__":
    main()