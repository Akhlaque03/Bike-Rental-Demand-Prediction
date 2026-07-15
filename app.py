import pandas as pd
import streamlit as st
import joblib

# Page Configuration
st.set_page_config(
    page_title = "Bike Rental Demand Prediction",
    page_icon = "🚲",
    layout = 'wide'
)

# Load Model
model = joblib.load("catboost_final_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")



# Side bar inputs
st.sidebar.header("Scenario Inputs")

hr = st.sidebar.slider(
    "Hours",
    0,
    23,
    8
)

mnth = st.sidebar.slider(
    "Month",
    1,
    12,
    6
)

weekday = st.sidebar.slider(
    "Week Day",
    0,
    6,
    3
)

temp = st.sidebar.slider(
    "Temperature",
    0.02,
    1.0,
    0.5
)

atemp = st.sidebar.slider(
    "Feels Like Temp",
    0.0,
    1.0,
    0.4848
)

hum = st.sidebar.slider(
    "Humidity",
    0.29,
    1.0,
    0.63
)

windspeed = st.sidebar.slider(
    "Wind Speed",
    0.0,
    0.4775,
    0.194
)

season = st.sidebar.selectbox(
    "Season",
    ["springer", "summer", "winter"]
)

yr = st.sidebar.selectbox(
    "Year",
    [2011, 2012]
)

holiday = st.sidebar.selectbox(
    "Holiday",
    ["Yes", "No"]
)

workingday = st.sidebar.selectbox(
    "Working Day",
    ["No work", "Working Day"]
)

weathersit = st.sidebar.selectbox(
    "Weather",
    ["Clear", "Mist", "Light Snow", "Heavy Rain"]
)

rush_hour = st.sidebar.selectbox(
    "Rush Hour",
    ["Non Rush Hour", "Rush Hour"]
)

# Prediction Button
predict_button = st.sidebar.button("Predict Rental Demand")


# Header
st.title("🚲 Bike Rental Demand Prediction")
st.caption(
    "Predict bike rental demand based on weather, time, and seasonal conditions."
)

# Model Comparison Before Hyperparameter Tuning
comparison_df = pd.DataFrame({
    "Model": [
        "CatBoost",
        "XGBoost",
        "LightGBM",
        "Random Forest",
        "Decision Tree",
        "Gradient Boosting",
        "KNN Regressor",
        "Linear Regression",
        "SVM Regressor"
    ],
    "MAE": [
        23.8946,
        24.1474,
        25.3265,
        24.5053,
        34.1010,
        45.2310,
        53.2738,
        86.1662,
        76.9182
    ],
    "MSE": [
        1473.8083,
        1543.5446,
        1634.4686,
        1694.6802,
        3373.8022,
        4344.1558,
        6164.7317,
        13110.2863,
        14078.6922
    ],
    "RMSE": [
        38.3902,
        39.2880,
        40.4286,
        41.1665,
        58.0844,
        65.9102,
        78.5158,
        114.5002,
        118.6537
    ],
    "R2_Score": [
        0.9535,
        0.9513,
        0.9484,
        0.9465,
        0.8935,
        0.8628,
        0.8053,
        0.5860,
        0.5554
    ]
})


# Model Performance After Hyperparameter Tuning
tuning_comparison_df = pd.DataFrame({
    "Model": [
        "CatBoost (Tuned)",
        "XGBoost (Tuned)",
        "LightGBM (Tuned)",
        "CatBoost (Original)",
        "XGBoost (Original)",
        "LightGBM (Original)",
        "Random Forest (Tuned)",
        "Random Forest (Original)"
    ],
    "MAE": [
        21.9912,
        22.5425,
        22.5871,
        23.8946,
        24.1474,
        25.3265,
        24.4813,
        24.5053
    ],
    "MSE": [
        1280.1439,
        1378.5630,
        1381.9522,
        1473.8083,
        1543.5446,
        1634.4686,
        1689.1659,
        1694.6802
    ],
    "RMSE": [
        35.7791,
        37.1290,
        37.1746,
        38.3902,
        39.2880,
        40.4286,
        41.0995,
        41.1665
    ],
    "R2_Score": [
        0.9596,
        0.9565,
        0.9564,
        0.9535,
        0.9513,
        0.9484,
        0.9467,
        0.9465
    ]
})



# DEFAULT VALUES
prediction = None

# Prediction Button
if predict_button:

    input_data = {
    "hr": hr,
    "weekday": weekday,
    "temp": temp,
    "atemp": atemp,
    "hum": hum,
    "windspeed": windspeed,

    "season_springer": 1 if season == "springer" else 0,
    "season_summer": 1 if season == "summer" else 0,
    "season_winter": 1 if season == "winter" else 0,

    "yr_2012": 1 if yr == 2012 else 0,

    "holiday_Yes": 1 if holiday == "Yes" else 0,

    "workingday_Working Day": 1 if workingday == "Working Day" else 0,

    "weathersit_Heavy Rain": 1 if weathersit == "Heavy Rain" else 0,
    "weathersit_Light Snow": 1 if weathersit == "Light Snow" else 0,
    "weathersit_Mist": 1 if weathersit == "Mist" else 0,

    "rush_hour_Rush Hour": 1 if rush_hour == "Rush Hour" else 0,

    "mnth_2.0": 1 if mnth == 2 else 0,
    "mnth_3.0": 1 if mnth == 3 else 0,
    "mnth_4.0": 1 if mnth == 4 else 0,
    "mnth_5.0": 1 if mnth == 5 else 0,
    "mnth_6.0": 1 if mnth == 6 else 0,
    "mnth_7.0": 1 if mnth == 7 else 0,
    "mnth_8.0": 1 if mnth == 8 else 0,
    "mnth_9.0": 1 if mnth == 9 else 0,
    "mnth_10.0": 1 if mnth == 10 else 0,
    "mnth_11.0": 1 if mnth == 11 else 0,
    "mnth_12.0": 1 if mnth == 12 else 0
    }


    input_df = pd.DataFrame([input_data])

    input_df = input_df[feature_columns]

    prediction = model.predict(input_df)[0]
    


# TOP SECTION
# =========================

left, right = st.columns([1.2, 1])

with left:

    st.subheader("Prediction")

    if prediction is not None:

        st.success(f"🚲 {prediction:.0f} Bikes/Hour")
        st.warning("Model Used : CatBoost Regressor")

    else:

        st.info(
            "Adjust bike rental conditions from sidebar and click Predict Rental Demand."
        )


with right:

    st.subheader("Deployed Model")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Best Model",
            "CatBoost (Tuned)"
        )

    with col2:
        st.metric(
            "R² Score",
            "0.9596"
        )

    with col3:
        st.metric(
            "RMSE",
            "35.7791"
        )


    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "MAE",
            "21.9912"
        )

    with col5:
        st.metric(
            "MSE",
            "1280.1439"
        )

    with col6:
        st.metric(
            "Model Type",
            "Regression"
        )


st.divider()


# Model Performance Before Hyperparameter Tuning
# st.subheader("Baseline Model Comparison")

# st.dataframe(
#     comparison_df.sort_values(
#         by='R2_Score',
#         ascending=False
#     ),
#     use_container_width=True
# )

# Model Performance After Hyperparameter Tuning
st.subheader("Model Performance After Hyperparameter Tuning")

# st.dataframe(
#     tuning_comparison_df.sort_values(
#         by='R2_Score',
#         ascending=False
#     ),
#     use_container_width=True
# )

# SELECTED Bike Rental SCENARIO
st.subheader("Selected Bike Rental Scenario")
scenario_df = pd.DataFrame({
    "Feature": [
        "Hours",
        "Month",
        "Week Day",
        "Temperature",
        "Feels Like Temp",
        "Humidity",
        "Wind Speed",
        "Season",
        "Year",
        "Holiday",
        "Working Day",
        "Weather",
        "Rush Hour"
    ],
    "Value": [
    str(hr),
    str(mnth),
    str(weekday),
    str(temp),
    str(atemp),
    str(hum),
    str(windspeed),
    str(season),
    str(yr),
    str(holiday),
    str(workingday),
    str(weathersit),
    str(rush_hour)
]
})

# st.dataframe(
#     scenario_df.astype(str),
#     use_container_width=True
# )

st.write(scenario_df)
