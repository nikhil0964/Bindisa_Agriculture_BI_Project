import os

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

df = pd.read_csv(os.path.join(DATA_DIR, "bindisa_agriculture_yearly_data.csv"))

features = [
    "Year",
    "Region",
    "Crop",
    "Season",
    "Area_Hectares",
    "Rainfall_mm",
    "Temperature_C",
    "Fertilizer_Cost",
    "Pesticide_Cost",
    "Irrigation_Cost",
    "Labor_Cost",
    "Storage_Transport_Cost",
]

target = "Yield_Tonnes_Per_Hectare"

X = df[features]
y = df[target]

categorical_features = ["Region", "Crop", "Season"]
numeric_features = [column for column in features if column not in categorical_features]

preprocessor = ColumnTransformer(
    transformers=[
        ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("numeric", "passthrough", numeric_features),
    ]
)

model = RandomForestRegressor(
    n_estimators=250,
    max_depth=12,
    min_samples_leaf=2,
    random_state=42,
)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model),
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
)

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

sample_prediction_data = pd.DataFrame(
    [
        {
            "Year": 2027,
            "Region": "Madhya Pradesh",
            "Crop": "Wheat",
            "Season": "Rabi",
            "Area_Hectares": 420,
            "Rainfall_mm": 820,
            "Temperature_C": 28.5,
            "Fertilizer_Cost": 3100000,
            "Pesticide_Cost": 1450000,
            "Irrigation_Cost": 2300000,
            "Labor_Cost": 4200000,
            "Storage_Transport_Cost": 620000,
        }
    ]
)

predicted_yield = pipeline.predict(sample_prediction_data)[0]

print("Machine Learning Yield Prediction")
print("-" * 45)
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")
print(f"Predicted Yield for sample 2027 wheat crop: {predicted_yield:.2f} tonnes/hectare")

