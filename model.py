import os
from datetime import datetime
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df: pd.DataFrame, contamination: float = 0.05) -> pd.DataFrame:
    clf = IsolationForest(contamination=contamination, random_state=42)
    preds = clf.fit_predict(df[["output_kwh"]])
    df = df.copy()
    df["anomaly"] = preds == -1
    return df

def generate_summary(df: pd.DataFrame) -> str:
    total = df["output_kwh"].sum()
    n_anom = df["anomaly"].sum()
    if n_anom == 0:
        return f"Total output: **{total:.0f} kWh**. No anomalies detected."
    else:
        dates = df[df["anomaly"]]["date"].dt.strftime('%b %d').tolist()[:3]
        return f"Total output: **{total:.0f} kWh**. Anomalies detected: **{n_anom}**. Notable dates: {', '.join(dates)}."

def save_alerts_csv(alerts_df: pd.DataFrame) -> bytes:
    return alerts_df.to_csv(index=False).encode("utf-8")