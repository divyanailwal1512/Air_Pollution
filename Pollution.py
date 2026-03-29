import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:/Users/hp/Documents/dataset1.xlsx")
print(df)

df.shape
df.info()
df.describe()
df.isnull().sum()

df.sort_values("Date", inplace=True)
print(df.groupby("Date")["AQI"].mean().plot())


print(df.groupby("City")["AQI"].mean().plot(kind="bar"))

print(df.head())


 # Visualization through Matplotlib

# Temperature vs AQI
df.plot(x="Temperature", y="AQI", kind="scatter")
plt.show()

 # Humidity vs AQI
df.plot(x="Humidity", y="AQI", kind="scatter")
plt.show()

# Wind speed vs AQI
df.plot(x="Wind Speed", y="AQI", kind="scatter")
plt.show()
# Defines the AQI trends
plt.plot(df["Date"], df["AQI"])
plt.title("AQI Trend Over Time")
plt.show()

 # Pollution level distribution
df["Pollution_Level"].value_counts().plot(kind="bar")
plt.show()

# Comparison based on city level
df.groupby("City")["AQI"].mean().plot(kind="bar")
plt.show()


 # Analyse the seasonal impact
df.groupby("Season")["AQI"].mean().plot(kind="bar")
plt.show()

Pollutant index impact
df.plot(x="Pollutant_Index", y="AQI", kind="scatter")
plt.show()