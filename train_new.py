import xarray as xr
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib
from sklearn.metrics import r2_score

dataset = xr.open_mfdataset("data/*.nc", combine="by_coords")
dataset = dataset.sel(
    time=slice("2023-09-01", "2023-12-31"),
    latitude=slice(-25, 20),
    longitude=slice(55, 85)
)

df = dataset[["uo", "vo"]].compute().to_dataframe().reset_index()
df = df.dropna(subset=["uo", "vo"])

df = df.sort_values(by=["latitude", "longitude", "time"]) #Sorting the data by latitude, longitude and time to ensure that the next day values are correctly aligned

""" print(df.head(4)) """

df_next_day = df.copy()
df_next_day['time'] = df_next_day["time"] - pd.Timedelta(days=1) #Shifting the time column by one day to align the next day values with the current day values
df_next_day = df_next_day.rename(columns={"uo": "uo_next", "vo": "vo_next"})

df_merged = df.merge(df_next_day, on=["time", "latitude", "longitude"], how="inner")
df_merged = df_merged.dropna()
df_merged = df_merged.astype({"latitude": "float32", "longitude": "float32", "uo": "float32", "vo": "float32"})
df_merged = df_merged.head(100000)

""" print(df_merged.head(4)) """

model = RandomForestRegressor(n_estimators=100, n_jobs=-1)

features = df_merged[["latitude", "longitude", "uo", "vo"]]
labels = df_merged[["uo_next", "vo_next"]]

split_point = int(0.8 * len(features)) #The first 80% of the data is used for training and the remaining 20% is used for testing. Split is done to avoid leakage, because the data is sorted by time, so the next day values are correctly aligned with the current day values.

X_train = features.iloc[:split_point]
y_train = labels.iloc[:split_point]
X_test = features.iloc[split_point:]
y_test = labels.iloc[split_point:]

model.fit(X_train, y_train)
joblib.dump(model, "new_ocean_current_model.pkl")

# Evaluation
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)

print(f"R² Score: {score:.4f}")

row = df_merged.iloc[0]

X = [[row["latitude"], row["longitude"], row["uo"], row["vo"]]]

pred = model.predict(X)

print("Predicted:", pred)
print("Actual:", row["uo_next"], row["vo_next"])
