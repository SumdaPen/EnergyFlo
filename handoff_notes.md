# Handoff Notes

## What's completed
- Built a full prototype allowing CSV uploads, anomaly detection using Isolation Forest, energy output visualization, and automatic generation of alert CSVs.

- Integrated Google Drive for CSV storage and configured Zapier to send alert emails when anomalies are detected.

- Developed a clean Streamlit frontend for easy interaction and clear data display.

## What isn't completed
- ChatGPT integration for advanced summary generation was not completed due to time constraints and the need to prioritize core functionality.

- Real-world CSV parsing wasn’t implemented, as it required more complex preprocessing beyond the simplified two-column CSV used in this prototype.

- Optimizing the Zapier alert speed was not addressed, and the delay (~6 minutes) remains due to limitations in Zapier’s free plan polling intervals.

## Future Improvements
- I would add user authentication and multi-user support for a more secure and scalable app.

- I would replace or improve Zapier with faster webhook-based alerts or direct API notifications.

- I would enhance the data parser to handle more complex, real-world energy datasets.

- I would integrate the ChatGPT API to generate richer, more detailed energy summaries.

## What was learned
- I learned how to integrate a machine learning model into a simple Streamlit frontend for rapid prototyping.

- I learned how to automate cross-platform workflows using Google Drive and Zapier to create an end-to-end automation pipeline.

- I learned the importance of balancing feature goals with time and tool limitations to deliver a working prototype efficiently.

## README

# Energy Insight Prototype

Energy Insight is a prototype web application designed to automate energy monitoring using anomaly detection, visualization, and alert automation. The project allows users to upload solar generation data and receive clear, actionable insights on irregularities in energy output.

---

## Project Overview

This project solves the problem of manual anomaly detection in energy datasets by automating the process using machine learning and automation tools. Energy providers can quickly upload their CSV data, visualize the results, and receive alerts without sifting through large amounts of raw data.

---

## Features

- Upload CSV files containing energy output data
- Detect anomalies using the Isolation Forest machine learning algorithm
- Display energy output graphs with anomaly markers
- Generate simple textual summaries of the energy production and anomalies
- Save anomaly alerts as CSV files to a Google Drive folder
- Trigger automated alerts through Zapier when anomalies are detected
- Provide users with a downloadable CSV of alerts from the app interface

---

## Tool Stack

Frontend: Streamlit for interactive data display and file upload  
Backend: Python for core logic, Pandas for data handling, Matplotlib for visualization  
Machine Learning: Isolation Forest model from scikit-learn for anomaly detection  
Automation: Google Drive for storage and Zapier for workflow automation  
Development Tools: VS Code and Google Drive Sync for file management  

---

## Architecture Overview

The system follows this flow:

1. The user uploads a CSV file containing energy output data.
2. The Streamlit app processes the data using Pandas and the Isolation Forest anomaly detection model.
3. Anomalies and trends are visualized using Matplotlib and presented in the Streamlit interface.
4. Anomalies are exported as a CSV file to a monitored Google Drive folder.
5. Zapier detects the new file in Google Drive and sends an alert (e.g., email).

---

## Project Structure

├── app.py # Main Streamlit application
├── model.py # ML logic for anomaly detection and summary generation
├── requirements.txt # List of Python dependencies
├── handoff_notes.md # Project documentation
├── LICENSE # MIT License


---

## Example CSV Format

The application expects a CSV with the following columns:

| Date       | Solar_Generation_kWh |
|------------|----------------------|
| 2025-01-01 | 320                  |
| 2025-01-02 | 280                  |
| 2025-01-03 | 295                  |

---

## Setup Instructions

Clone the repository

git clone https://github.com/your-username/energy-insight.git
cd energy-insight

Install the required dependencies
Run the Streamlit app locally


Create a folder named `Energy_Alerts` in your Google Drive  
Ensure your local Google Drive syncs with the target folder  
Adjust the save path in `app.py` if your folder location differs  

Configure Zapier to watch the Google Drive folder for new CSV files  
Create a Zap that sends an email, Slack message, or other action when a new alert file appears  

---

## Example Workflow

1. A user uploads a CSV file through the Streamlit interface.
2. The app analyzes the data and highlights anomalies on a line graph.
3. A textual summary of energy output and anomalies is generated.
4. If anomalies are present, they are saved as a CSV in Google Drive.
5. Zapier detects the new CSV file and sends a notification.

---



