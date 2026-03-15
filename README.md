# ✈️ Flight Delay Prediction and Analysis

Tech Challenge – FIAP  
Machine Learning Engineering

---

# 📌 Project Overview

Flight delays are a common challenge in the aviation industry, impacting passengers, airlines, and airport operations. Understanding the factors that contribute to delays can help improve operational efficiency and passenger experience.

This project analyzes historical flight data to identify patterns related to flight delays and develops Machine Learning models capable of predicting whether a flight will experience a significant delay.

The project also applies unsupervised learning techniques to identify operational patterns across airports and routes, and presents insights through an interactive Power BI dashboard.

---

# 🎯 Project Objectives

The main objectives of this project are:

- Perform **Exploratory Data Analysis (EDA)** to understand delay patterns
- Identify operational factors related to flight delays
- Develop **Machine Learning models** to predict flight delays
- Apply **unsupervised learning techniques** to identify airport patterns
- Build an **interactive Power BI dashboard**
- Structure the project following **professional Data Science and ML Engineering practices**

---

# 🧰 Technologies Used

Python  
Pandas  
NumPy  
Matplotlib  
Seaborn  
Scikit-learn  
XGBoost  
Google Colab  
Power BI  
GitHub  

---

# 📁 Project Structure


FLIGHTS-ML

dashboard
flight_delay_dashboard.pbix

data
raw
processed

models
logistic_model.pkl
random_forest.pkl

notebooks
flight_delay_analysis.ipynb

outputs
figures
tables

src
data_processing.py
feature_engineering.py
model_training.py

.gitignore
LICENSE
README.md
requirements.txt


---

# 📂 Folder Description

**data/raw**  
Stores the original dataset used in the project.

**data/processed**  
Stores cleaned and transformed datasets ready for modeling and dashboard usage.

**notebooks**  
Contains the main analysis notebook developed in Google Colab.

**src**  
Contains reusable Python scripts for data processing, feature engineering, and model training.

**models**  
Stores trained machine learning models.

**outputs/figures**  
Stores charts and visualizations generated during analysis.

**outputs/tables**  
Stores aggregated tables used for the dashboard.

**dashboard**  
Contains the Power BI dashboard file.

---

# 📊 Dataset

The dataset contains historical flight information including operational metrics such as scheduling, airlines, airports, and delays.

Key variables include:

| Variable | Description |
|--------|-------------|
| YEAR | Year of flight |
| MONTH | Month of flight |
| DAY | Day of flight |
| DAY_OF_WEEK | Day of week |
| AIRLINE | Airline code |
| ORIGIN_AIRPORT | Departure airport |
| DESTINATION_AIRPORT | Arrival airport |
| SCHEDULED_DEPARTURE | Scheduled departure time |
| DEPARTURE_DELAY | Departure delay in minutes |
| ARRIVAL_DELAY | Arrival delay in minutes |
| DISTANCE | Flight distance |
| CANCELLED | Indicates if the flight was cancelled |
| DIVERTED | Indicates if the flight was diverted |

These variables allow us to analyze operational performance and train predictive models.

---

# 🔎 Project Methodology

The project follows a standard Machine Learning workflow:

1️⃣ Data Loading  
2️⃣ Data Understanding  
3️⃣ Data Cleaning and Preprocessing  
4️⃣ Exploratory Data Analysis (EDA)  
5️⃣ Feature Engineering  
6️⃣ Supervised Machine Learning Models  
7️⃣ Unsupervised Learning Analysis  
8️⃣ Model Evaluation  
9️⃣ Dashboard Development  

---

# 📈 Exploratory Data Analysis

EDA was performed to understand operational behavior and identify patterns associated with flight delays.

Key analyses include:

- Distribution of arrival delays
- Delay patterns by airline
- Delay patterns by airport
- Delay patterns by day of week
- Delay patterns by time of day
- Cancellation rates by airline
- Identification of problematic flight routes

Generated visualizations are stored in:


outputs/figures


---

# 🧠 Feature Engineering

Several features were created to improve predictive performance:

- Time-of-day categories (morning, afternoon, evening, night)
- Weekend indicator
- Route identifier (origin + destination)
- Distance categories
- Scheduled flight duration categories

Special care was taken to **avoid data leakage**, ensuring that variables generated after flight completion were not used in the prediction model.

---

# 🤖 Supervised Learning Models

The supervised learning task consists of predicting whether a flight will experience a **significant delay**.

Target variable:


is_delayed


Definition:


Arrival Delay > 15 minutes


Models implemented:

- Logistic Regression (baseline)
- Random Forest Classifier

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC

Model comparison helps determine which algorithm performs best for delay prediction.

---

# 🔬 Unsupervised Learning

Unsupervised learning was applied to identify patterns among airports.

Airports were grouped using clustering techniques based on:

- Average delay
- Delay rate
- Cancellation rate
- Flight volume
- Average distance

Algorithms used:

- K-Means Clustering
- Principal Component Analysis (PCA) for visualization

This analysis allows the identification of airports with similar operational behaviors.

---

# 📊 Power BI Dashboard

An interactive dashboard was developed using **Power BI** to present the main insights from the analysis.

Dashboard features include:

- Flight delay overview
- Delay rate by airline
- Delay rate by airport
- Route performance analysis
- Temporal delay patterns (day of week and hour)

Dashboard file:


dashboard/flight_delay_dashboard.pbix


---

# 📊 Results

The analysis identified several operational factors associated with flight delays, including:

- Airlines with higher delay rates
- Airports with operational congestion
- Time-of-day effects on delays
- High-risk flight routes

Machine Learning models demonstrated the ability to predict delay likelihood using operational scheduling features.

---

# ⚠️ Limitations

Some limitations of this study include:

- Lack of detailed weather information
- Absence of real-time operational constraints
- Potential bias from historical data distribution

Future improvements could include integrating weather data and air traffic control information.

---

# 🚀 Future Improvements

Possible improvements for this project include:

- Incorporating weather data
- Building a dedicated model for flight cancellations
- Deploying the model as an API
- Developing a real-time delay prediction system
- Expanding the dashboard with predictive insights

---

# ▶️ How to Run the Project

Clone the repository:


git clone https://github.com/your-repository/flights-ml.git


Install dependencies:


pip install -r requirements.txt


Open the notebook:


notebooks/flight_delay_analysis.ipynb


Run the notebook to reproduce the entire analysis pipeline.

---

# 📌 Author

Project developed as part of the **FIAP Machine Learning Engineering Tech Challenge**.