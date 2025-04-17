import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(
    page_title="Moulya Bangalore Pradeep's Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling and scroll behavior
st.markdown("""
    <style>
        /* Remove Streamlit padding */
        .main .block-container {
            padding: 0 4rem;
        }

        /* White background */
        body, .stApp {
            background-color: white;
        }

        /* Sticky header */
        .sticky-header {
            position: sticky;
            top: 0;
            background-color: white;
            z-index: 999;
            padding: 1rem 0;
            border-bottom: 1px solid #ccc;
        }

        /* Section heading highlight on scroll */
        .highlight {
            background-color: #f0f8ff;
            border-left: 4px solid #1e90ff;
            padding: 0.5rem 1rem;
            margin: 2rem 0 1rem 0;
            font-weight: bold;
            font-size: 1.3rem;
        }

        /* Scroll animations */
        .reveal {
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.6s ease;
        }

        .reveal.visible {
            opacity: 1;
            transform: none;
        }

        /* Hide sidebar completely */
        [data-testid="stSidebar"] {
            display: none;
        }
        button[title="View fullscreen"] {
        display: none;
    }
    /* Hide anchor link symbols from all headers */
    h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
        display: none !important;
    }
    
    </style>

    <script>
        window.addEventListener('scroll', function() {
            let reveals = document.querySelectorAll('.reveal');
            for (let i = 0; i < reveals.length; i++) {
                let windowHeight = window.innerHeight;
                let elementTop = reveals[i].getBoundingClientRect().top;
                let elementVisible = 150;

                if (elementTop < windowHeight - elementVisible) {
                    reveals[i].classList.add("visible");
                }
            }
        });
    </script>
""", unsafe_allow_html=True)
import base64
from io import BytesIO
# Sticky title header
st.markdown('<div class="sticky-header"><h1>Moulya Bangalore Pradeep</h1></div>', unsafe_allow_html=True)
# Profile Section

def get_base64_image(img_path):
    img = Image.open(img_path).resize((300, 300))
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode()
    return img_b64

# Profile Section
st.markdown('<div class="reveal">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    img_b64 = get_base64_image("assets/profile.jpg")
    st.markdown(f"""
        <style>
            .circular-image {{
                width: 300px;
                height: 300px;
                border-radius: 50%;
                object-fit: cover;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }}
        </style>
        <img src="data:image/png;base64,{img_b64}" class="circular-image">
    """, unsafe_allow_html=True)
with col2:
    st.markdown(
    '<h3 style="text-decoration: none; font-weight: 600;">Professor | AI & ML Enthusiast | Senior Java & Python Developer</h3>',
    unsafe_allow_html=True)
    st.write("""
    Passionate about building AI-driven applications and sharing knowledge with the next generation of tech leaders.
    Over 10+ years of experience in Java, Python, Machine Learning, and Cloud-native solutions.
    """)
    st.download_button("📄 Download CV", open("assets/Moulya_CV.pdf", "rb").read(), "Moulya_CV.pdf", mime="application/pdf")
st.markdown('</div>', unsafe_allow_html=True)





#=========


import streamlit as st
from PIL import Image
import os

# Title
st.markdown("## Skills")

# Create a container for the images
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10,col11,col12,col13 = st.columns(13)  # Creates 3 columns (you can adjust the number of columns)
col_list = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10,col11,col12,col13]

# Loop through all images 0.jpg to 14.jpg
for i in range(15):  # Image range from 0.jpg to 14.jpg
    img_path = f"assets/{i}.jpg"  # Image path (ensure your images are in 'assets' folder)
    if os.path.exists(img_path):
        image = Image.open(img_path)
        image = image.resize((60, 80))  # Resize the image to 60x80 pixels (as per your request)
        
        # Find an available column and place the image there
        col = col_list[i % len(col_list)]  # This ensures the images are placed in a cycle of 3 columns
        col.image(image, use_column_width=False)  # Display image in the column



#=====================================================================================================================
# Small heading

import streamlit as st
from PIL import Image

st.markdown("## 🤖 AI Projects")

# Display the AI image
ai_image = Image.open("assets/ai.jpg")
clicked = st.toggle("🔍 Click to explore all AI Projects", help="Click the AI toggle")

# Center image with style
st.image(ai_image, width=400, caption="AI Projects", use_column_width=False)

# Show projects if toggle is active
if clicked:
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
        }
    }

    for category, projects in project_categories.items():
        st.markdown(f"### {category}")
        for name, url in projects.items():
            st.markdown(f'<a href="{url}" target="_blank" style="text-decoration: none;"> ▸ {name}</a>', unsafe_allow_html=True)


#============


import streamlit as st
from PIL import Image
import base64

# Set default session state
if "show_web_projects" not in st.session_state:
    st.session_state["show_web_projects"] = False

# Function to toggle project visibility
def toggle_projects():
    st.session_state["show_web_projects"] = not st.session_state["show_web_projects"]

# Load image and convert to base64
with open("assets/web.jpg", "rb") as image_file:
    img_base64 = base64.b64encode(image_file.read()).decode()

# Inject styled clickable image
st.markdown("""
    <style>
    .clickable-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 400px;
        border-radius: 12px;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 0 0px rgba(0,0,0,0);
    }
    .clickable-image:hover {
        box-shadow: 0px 0px 16px 2px rgba(0, 123, 255, 0.6);
        cursor: pointer;
        transform: scale(1.02);
    }
    button[title="Hidden form button"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# Image wrapped in a button using a form (safe toggle)
with st.form("image_form", clear_on_submit=True):
    st.markdown(
        f'<input type="image" src="data:image/jpeg;base64,{img_base64}" class="clickable-image" alt="Click to show projects"/>',
        unsafe_allow_html=True
    )
    submitted = st.form_submit_button("Hidden form button")
    if submitted:
        toggle_projects()

# Display project list
if st.session_state["show_web_projects"]:
    st.markdown("### 🌐 Web Development / Platform Projects")
    project_links = {
        "webdev2": "https://github.com/moulyabpradeep/webdev2",
        "TraceRent_AI": "https://github.com/moulyabpradeep/TraceRent_AI",
        "OnlineTestTakingPlatform": "https://github.com/moulyabpradeep/OnlineTestTakingPlatform",
        "OnlineCustomerEnrollment": "https://github.com/moulyabpradeep/OnlineCustomerEnrollment/tree/main/.github/workflows",
        "folder-management": "https://github.com/moulyabpradeep/folder-management"
    }

    for name, url in project_links.items():
        st.markdown(f"- [{name}]({url})")


#===================================================================================================================
# Resume Section
st.markdown('<div class="highlight">📄 Resume</div>', unsafe_allow_html=True)
st.markdown('<div class="reveal">', unsafe_allow_html=True)
st.write("### Professional Summary")
st.write("""
Results-driven AI Software Engineer... [same as your content]
""")

st.write("### Experience")
st.write("""
**Professor, Data Analytics Dept — SAIT** (Jan 2025 – Present)  
... [same content]
""")

st.write("### Education")
st.write("...")

st.write("### Technical Skills")
st.write("...")
st.markdown('</div>', unsafe_allow_html=True)


# Final CV Download Section
st.markdown('<div class="highlight">⬇️ Get Full CV</div>', unsafe_allow_html=True)
st.markdown('<div class="reveal">', unsafe_allow_html=True)
st.download_button("📄 Download Full CV", open("assets/Moulya_CV.pdf", "rb").read(), "Moulya_CV.pdf", mime="application/pdf")
st.markdown('</div>', unsafe_allow_html=True)
