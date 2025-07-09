import io
import os
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from model import detect_anomalies, generate_summary, save_alerts_csv

st.set_page_config(page_title="Energy Insight Prototype", page_icon="⚡", layout="wide")
st.title("⚡ Energy Insight Prototype (Week 4)")

uploaded_file = st.file_uploader("Upload your energy CSV", type=["csv"])
st.markdown("CSV must contain `Date` and `Solar_Generation_kWh` columns.")

if uploaded_file:
    # Read and rename columns for consistency
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])
    df.rename(columns={"Date": "date", "Solar_Generation_kWh": "output_kwh"}, inplace=True)
    df = df.sort_values("date").reset_index(drop=True)
    df = detect_anomalies(df)

    st.subheader("Energy Output")
    fig, ax = plt.subplots()
    ax.plot(df["date"], df["output_kwh"], linewidth=1.5)
    ax.scatter(df.loc[df["anomaly"], "date"], df.loc[df["anomaly"], "output_kwh"],
               s=60, color="red", label="Anomaly")
    ax.set_xlabel("Date")
    ax.set_ylabel("kWh")
    ax.set_title("Energy Output with Detected Anomalies")
    ax.legend()
    st.pyplot(fig)

    st.subheader("Weekly Summary")
    st.markdown(generate_summary(df))

    st.subheader("Anomaly Alerts")
    alerts = df[df['anomaly'] == True][["date", "output_kwh"]]
    st.dataframe(alerts, use_container_width=True)

    # Export for Zapier
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"alerts_{today}.csv"
    alerts.to_csv(f"G:/My Drive/Energy_Alerts/{filename}", index=False)

    # Optional download
    csv_bytes = save_alerts_csv(alerts)
    st.download_button("Download alerts_today.csv", data=csv_bytes,
                       file_name="alerts_today.csv", mime="text/csv")
else:
    st.warning("Upload a CSV to begin.")