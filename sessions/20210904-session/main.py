import pandas as pd

FILE_PATH = "data/prima-indians-diabetes.csv"

try:
    file = pd.read_csv(FILE_PATH, header=None)
except:
    print("File not found")
    exit()

print(file)
