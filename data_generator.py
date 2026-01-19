import numpy as np
import pandas as pd

np.random.seed(42)

N = 1000

data = {
    "pH": np.random.uniform(5.5, 9.5, N),
    "TDS": np.random.uniform(100, 2000, N),
    "Hardness": np.random.uniform(50, 600, N),
    "Turbidity": np.random.uniform(0, 10, N),
    "Nitrate": np.random.uniform(0, 80, N),
    "Chloride": np.random.uniform(50, 500, N),
}

df = pd.DataFrame(data)

def label_water(row):
    unsafe_count = 0
    moderate_count = 0

    if row["pH"] < 6.5 or row["pH"] > 8.5:
        moderate_count += 1
        if row["pH"] < 6 or row["pH"] > 9:
            unsafe_count += 1

    if row["TDS"] > 500:
        moderate_count += 1
        if row["TDS"] > 1200:
            unsafe_count += 1

    if row["Hardness"] > 300:
        moderate_count += 1
        if row["Hardness"] > 500:
            unsafe_count += 1

    if row["Turbidity"] > 5:
        moderate_count += 1
        if row["Turbidity"] > 8:
            unsafe_count += 1

    if row["Nitrate"] > 10:
        moderate_count += 1
        if row["Nitrate"] > 45:
            unsafe_count += 1

    if row["Chloride"] > 250:
        moderate_count += 1
        if row["Chloride"] > 400:
            unsafe_count += 1

    if unsafe_count >= 1:
        return "Unsafe"
    elif moderate_count >= 2:
        return "Moderate"
    else:
        return "Safe"

df["Quality"] = df.apply(label_water, axis=1)

df.to_csv("water_quality_data.csv", index=False)

print("Dataset generated successfully.")