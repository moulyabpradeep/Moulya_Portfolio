import streamlit as st
import pandas as pd

st.set_page_config(page_title="Projects", layout="wide")

# Inject light blue background using custom CSS
st.markdown("""
    <style>
        body {
            background-color: #e6f2ff;
        }
        .stApp {
            background-color: #e6f2ff;
        }
        table {
            width: 100%;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        a {
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📁 Projects")
st.markdown("---")

# Define project categories and data
project_categories = {
    "🧠 NLP Projects": {
        "NLP_Data_Cleaning": "https://github.com/moulyabpradeep/NLP_Data_Cleaning",
        "Movie_reviews_Sentiment_Analysis": "https://github.com/moulyabpradeep/Movie_reviews_Sentiment_Analysis",
        "NLP_Project_LargeText_to_Voice_to_Speech_to_lipSync": "https://github.com/moulyabpradeep/NLP_Project_LargeText_to_Voice_to_Speech_to_lipSync",
        "NLP_Movie_Reviews": "https://github.com/moulyabpradeep/NLP_Movie_Reviews",
        "ConestogaChatbot": "https://github.com/moulyabpradeep/ConestogaChatbot"
    },
    "🧠 Computer Vision Projects": {
        "ComputerVision_Video_Object_Detect_Segment": "https://github.com/moulyabpradeep/ComputerVision_Video_Object_Detect_Segment",
        "ComputerVision_Image_Object_Detect_Segment": "https://github.com/moulyabpradeep/ComputerVision_Image_Object_Detect_Segment"
    },
    "📈 Time Series / Forecasting Projects": {
        "Stock_Price_Predictions_Nvidia_ARIMA": "https://github.com/moulyabpradeep/Stock_Price_Predictions_Nvidia_ARIMA",
        "Nvidia_Stock_Predictions_Kfold_cross_val": "https://github.com/moulyabpradeep/Nvidia_Stock_Predictions_Kfold_cross_val",
        "PricePredictions_DeepLearning_RNN_LSTM": "https://github.com/moulyabpradeep/PricePredictions_DeepLearning_RNN_LSTM",
        "TimeSeries_Dataset_Forecasting": "https://github.com/moulyabpradeep/TimeSeries_Dataset_Forecasting"
    },
    "📊 Classification / Clustering Projects": {
        "DBSCAN-Clustering": "https://github.com/moulyabpradeep/DBSCAN-Clustering",
        "Big_mart_Churn": "https://github.com/moulyabpradeep/Big_mart_Churn",
        "Heart_disease_Prediction": "https://github.com/moulyabpradeep/Heart_disease_Prediction",
        "BrainStrokePrediction": "https://github.com/moulyabpradeep/BrainStrokePrediction",
        "insurance": "https://github.com/moulyabpradeep/insurance",
        "TraceRent_AI": "https://github.com/moulyabpradeep/TraceRent_AI"
    },
    "🌐 Web Development / Platform Projects": {
        "webdev-demos": "https://github.com/moulyabpradeep/webdev-demos",
        "webdev2": "https://github.com/moulyabpradeep/webdev2",
        "SENG8080-3-field_project": "https://github.com/moulyabpradeep/SENG8080-3-field_project",
        "OnlineTestTakingPlatform": "https://github.com/moulyabpradeep/OnlineTestTakingPlatform",
        "folder-management": "https://github.com/moulyabpradeep/folder-management",
        "OnlineCustomerEnrollment": "https://github.com/moulyabpradeep/OnlineCustomerEnrollment"
    }
}

# Display as sectioned tables
for category, projects in project_categories.items():
    st.subheader(category)
    df = pd.DataFrame({"Project Name": list(projects.keys()), "GitHub Link": list(projects.values())})
    df["Project Name"] = df.apply(lambda row: f'<a href="{row["GitHub Link"]}" target="_blank">{row["Project Name"]}</a>', axis=1)
    st.markdown(df[["Project Name"]].to_html(escape=False, index=False), unsafe_allow_html=True)
    st.markdown("---")
