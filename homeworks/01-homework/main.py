import pandas as pd
import matplotlib.pyplot as plt

# Forest fires db - https://archive.ics.uci.edu/ml/datasets/Forest+Fires
# Billboard Hot-100 songs from 1970-2017 - https://data.world/typhon/billboard-hot-100-songs-from-1970-2017
# Historical Tropical Storm - https://data.world/dhs/historical-tropical-storm

file_path = "../../data/Historical_Tropical_Storm_Tracks.csv"

file = pd.read_csv(file_path)

rows = file.head()

file_shape = file.shape

dtypes = file.dtypes

description = file.describe()

# Forest fires db
# groups_mean = file.groupby(["day"]).mean()
# Billboard Hot-100 songs from 1970-2017
# groups_mean = file.groupby(["date"]).mean()
# Historical Tropical Storm
groups_mean = file.groupby(["YEAR"]).mean()

groups_mean.hist()
plt.show()

groups_mean.boxplot()
plt.show()

groups_mean.plot(kind='density', subplots=True, layout=(4, 3))
plt.show()
