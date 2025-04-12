import streamlit as st

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
    </style>
""", unsafe_allow_html=True)

st.title("📁 Projects")

st.markdown("---")

st.header("🧠 NLP Projects")
nlp_projects = {
    "NLP_Data_Cleaning": "https://github.com/moulyabpradeep/NLP_Data_Cleaning",
    "Movie_reviews_Sentiment_Analysis": "https://github.com/moulyabpradeep/Movie_reviews_Sentiment_Analysis",
    "NLP_Project_LargeText_to_Voice_to_Speech_to_lipSync": "https://github.com/moulyabpradeep/NLP_Project_LargeText_to_Voice_to_Speech_to_lipSync",
    "NLP_Movie_Reviews": "https://github.com/moulyabpradeep/NLP_Movie_Reviews",
    "ConestogaChatbot": "https://github.com/moulyabpradeep/ConestogaChatbot"
}
for name, link in nlp_projects.items():
    st.markdown(f"### [{name}]({link})")
    st.markdown("---")

st.header("🧠 Computer Vision Projects")
cv_projects = {
    "ComputerVision_Video_Object_Detect_Segment": "https://github.com/moulyabpradeep/ComputerVision_Video_Object_Detect_Segment",
    "ComputerVision_Image_Object_Detect_Segment": "https://github.com/moulyabpradeep/ComputerVision_Image_Object_Detect_Segment"
}
for name, link in cv_projects.items():
    st.markdown(f"### [{name}]({link})")
    st.markdown("---")

st.header("📈 Time Series / Forecasting Projects")
time_series_projects = {
    "Stock_Price_Predictions_Nvidia_ARIMA": "https://github.com/moulyabpradeep/Stock_Price_Predictions_Nvidia_ARIMA",
    "Nvidia_Stock_Predictions_Kfold_cross_val": "https://github.com/moulyabpradeep/Nvidia_Stock_Predictions_Kfold_cross_val",
    "PricePredictions_DeepLearning_RNN_LSTM": "https://github.com/moulyabpradeep/PricePredictions_DeepLearning_RNN_LSTM",
    "TimeSeries_Dataset_Forecasting": "https://github.com/moulyabpradeep/TimeSeries_Dataset_Forecasting"
}
for name, link in time_series_projects.items():
    st.markdown(f"### [{name}]({link})")
    st.markdown("---")

st.header("📊 Classification / Clustering Projects")
ml_projects = {
    "DBSCAN-Clustering": "https://github.com/moulyabpradeep/DBSCAN-Clustering",
    "Big_mart_Churn": "https://github.com/moulyabpradeep/Big_mart_Churn",
    "Heart_disease_Prediction": "https://github.com/moulyabpradeep/Heart_disease_Prediction",
    "BrainStrokePrediction": "https://github.com/moulyabpradeep/BrainStrokePrediction",
    "insurance": "https://github.com/moulyabpradeep/insurance",
    "TraceRent_AI": "https://github.com/moulyabpradeep/TraceRent_AI"
}
for name, link in ml_projects.items():
    st.markdown(f"### [{name}]({link})")
    st.markdown("---")

st.header("🌐 Web Development / Platform Projects")
web_projects = {
    "webdev-demos": "https://github.com/moulyabpradeep/webdev-demos",
    "webdev2": "https://github.com/moulyabpradeep/webdev2",
    "SENG8080-3-field_project": "https://github.com/moulyabpradeep/SENG8080-3-field_project",
    "OnlineTestTakingPlatform": "https://github.com/moulyabpradeep/OnlineTestTakingPlatform",
    "folder-management": "https://github.com/moulyabpradeep/folder-management",
    "OnlineCustomerEnrollment": "https://github.com/moulyabpradeep/OnlineCustomerEnrollment"
}
for name, link in web_projects.items():
    st.markdown(f"### [{name}]({link})")
    st.markdown("---")
