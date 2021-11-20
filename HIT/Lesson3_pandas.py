import pandas as pd

df = pd.read_csv("Bike_sharing_data.csv")
# print(df.info)

print(df.mnth.value_counts(normalize=True))
print(df.mnth.value_counts())