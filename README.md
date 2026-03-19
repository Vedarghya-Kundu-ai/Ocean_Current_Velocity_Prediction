# 🌊 Ocean Current Forecasting using Machine Learning

## 📌 Overview
This project focuses on forecasting ocean surface currents using historical oceanographic data. The model learns spatial and temporal relationships in ocean velocity to estimate future current behavior.

The implementation emphasizes **correct time-series modeling**, ensuring realistic predictions by avoiding data leakage and preserving temporal order.

---

## 🚀 Key Features

- 🌊 **Surface Current Prediction**: Predicts **surface-level ocean currents** using eastward (`uo`) and northward (`vo`) velocity components  
- 🧠 **Time-Aware Modeling**: Preserves temporal order and models next-step dynamics instead of using random sampling  
- 🔒 **No Data Leakage**: Uses sequential train-test split for realistic evaluation  
- 🌍 **Geospatial Learning**: Incorporates latitude and longitude to capture spatial variations  
- 📊 **Real-World Dataset**: Trained on Copernicus Marine (CMEMS) ocean physics data  
- ⚙️ **Efficient Data Handling**: Processes multi-dimensional data using xarray and pandas  
- 📉 **Memory-Conscious Design**: Uses controlled dataset slicing and optimized model configuration  
- 📈 **High Predictive Performance**: Achieves R² ≈ 0.92  
- 🧪 **Validated Predictions**: Predictions closely match actual next-day observations  

---

## 🧠 Problem Formulation

The task is modeled as:

(latitude, longitude, uo, vo at time t)
                ↓
(latitude, longitude, uo_next, vo_next at time t+1)

Where:
- `uo` → Eastward sea water velocity (m/s)  
- `vo` → Northward sea water velocity (m/s)  

---

## 🌍 Region of Application

The model is trained and applicable within:

- **Latitude:** -25° to 20°  
- **Longitude:** 55° to 85°  

This region corresponds to the **Northern and Central Indian Ocean**, including:
- Arabian Sea  
- Bay of Bengal  
- Waters around the Indian subcontinent  

⚠️ Predictions are reliable only within this geographic range.

---

## 📊 Dataset

- Source: Copernicus Marine Environment Monitoring Service (CMEMS)  
- Variables:
  - `uo` (zonal / eastward velocity)  
  - `vo` (meridional / northward velocity)  
- Temporal resolution: Daily  
- Depth: Surface layer (~0.49 m)  

---

## ⚙️ Tech Stack

- Python  
- xarray  
- pandas  
- scikit-learn  
- joblib  

---

## 🔄 Data Processing Pipeline

1. Load dataset using xarray  
2. Select region of interest  
3. Convert to pandas DataFrame  
4. Remove missing values  
5. Sort data by latitude, longitude, and time  
6. Create next-day labels using time shifting  
7. Merge datasets to align current and next-day values  

---

## ⚠️ Key Design Decisions

### 1. Time-Based Splitting (No Data Leakage)

Instead of random splitting:

- First 80% → Training  
- Last 20% → Testing  

This ensures:
- realistic evaluation  
- no future data leakage  

---

### 2. Avoiding Random Sampling

Random sampling (`.sample()`) was avoided because it breaks temporal relationships.

Instead:
- sequential slicing (`.head()`) was used when limiting dataset size  

---

### 3. Memory Optimization

Due to system limitations:
- dataset size was reduced using sequential slicing  
- model complexity was controlled  

---

## 🤖 Model

- Algorithm: Random Forest Regressor  
- Configuration:
  - `n_estimators`: 50–100  
  - `n_jobs`: 1 (memory-safe)  
  - `max_depth`: limited (optional optimization)  

---

## 📈 Performance

- Metric: R² Score  
- Achieved: **~0.92**

### Interpretation

The model explains ~92% of variance in ocean currents, which is expected due to strong short-term temporal continuity.

---

## 🧪 Validation

Model predictions were compared with actual values:

Predicted: [-0.071, 0.038]  
Actual:    [-0.070, 0.041]  

This confirms:
- correct temporal alignment  
- meaningful learning  

---

## 🚧 Limitations

- Uses only single-day input (no multi-day history)  
- Trained on a subset due to memory constraints  
- Limited spatial coverage  
- Does not capture long-term seasonal patterns  

---

## 🔮 Future Improvements (Realistic)

- Add short-term temporal features (past 3–5 days)  
- Use more efficient models (e.g., gradient boosting)  
- Train on larger datasets with optimized pipelines  
- Build a simple inference pipeline for real-time prediction  

---

## 💬 Key Learnings

- Importance of **time-aware splitting in ML**  
- Handling **large geospatial datasets**  
- Avoiding **data leakage in temporal problems**  
- Making **engineering trade-offs under constraints**  

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt

pip install -r requirements.txt
