import matplotlib as mpl
from matplotlib import pyplot as plt

import pandas as pd

df = pd.read_csv("Bike_sharing_data.csv")
# print(df.temp)

# סטטיסטיקה - משתנה בדיד - שכיחות ערך בעמודה ושכיחות מנורמנלת - 30 פעם, 30 פעם מתוך X שורות
# print(df.mnth.value_counts(normalize=True))
# print(df.mnth.value_counts())

# ממשיכים עם סטטיסטיקה - משתנה רציף - נחתוך ל - X טווחים
# כל טווח נרשם כערך תחתון ועליון שלו ומספר המופעים
# ומנורמל
print(pd.cut(df.temp, bins=5).value_counts())
print(pd.cut(df.temp, bins=5).value_counts(normalize=True))

# matplotlib.inline
# plt.hist(df.temp, bins=5)

# הפקודה describe - מחשבת מדדים על עמודה
print(df.cnt.describe())
print(pd.cut((df.cnt), bins=5).value_counts())
print(df.casual.describe())