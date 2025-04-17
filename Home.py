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
        col.image(image)  # Display image in the column


#=================


import streamlit as st
from PIL import Image
import base64

# Load image and convert to base64
import streamlit as st

# Title
st.markdown("## Projects")

# Create two columns
col1, col2 = st.columns(2)

# Web Projects (inside expander)
with col1:
    with st.expander("🌐 Web Projects", expanded=False):  # This creates a collapsible section
        project_links = {
            "webdev2": {
                "url": "https://webdev2-delta.vercel.app/",
                "description": "A web development project was created for course content, which is developed in node and next.js for SAIT Students. It is deployed project with youtube classroom teaching videos."
            },
            "TraceRent_AI": {
                "url": "https://github.com/moulyabpradeep/TraceRent_AI",
                "description": "AI-powered platform for tenant-property matching. Backend code is developed in python and ML modelling"
            },
            "OnlineTestTakingPlatform": {
                "url": "https://github.com/moulyabpradeep/OnlineTestTakingPlatform",
                "description": "An online test taking platform to administer and take tests. Developed in Java, Hibernate and Spring"
            },
            "OnlineCustomerEnrollment": {
                "url": "https://github.com/moulyabpradeep/OnlineCustomerEnrollment/tree/main/.github/workflows",
                "description": "A system for online customer enrollment with financial institutions. Developed in Java, JPA, Hibernate, Springboot."
            },
            "ContractBase":{
                "url":"https://contractbase.ca/",
                "description":"A Volunteering Project developed for a Recruiter. This website developed using Java and MEAN stack."
            }
        }
        for name, details in project_links.items():
            st.markdown(f"### {name}")
            st.markdown(f"**Description:** {details['description']}")
            st.markdown(f"- [Visit Project]({details['url']})")

# AI Projects (inside expander)
with col2:
    with st.expander("🤖 AI Projects", expanded=False):  # This creates a collapsible section
        project_categories = {
            "📊 Classification / Clustering Projects": {
                "TraceRent_AI": {
                    "url": "https://github.com/moulyabpradeep/TraceRent_AI",
                    "description": "AI-based platform for tenant-property matching and rent prediction."
                },
                "BrainStrokePrediction": {
                    "url": "https://github.com/moulyabpradeep/BrainStrokePrediction",
                    "description": "Predicting brain stroke risk using machine learning models. Developed in Python and ML modelling. The project is deployed on cloud."
                },
                "DBSCAN-Clustering": {
                    "url": "https://github.com/moulyabpradeep/DBSCAN-Clustering",
                    "description": "Using DBSCAN for clustering analysis on datasets."
                },
                "Big_mart_Churn": {
                    "url": "https://github.com/moulyabpradeep/Big_mart_Churn",
                    "description": "Churn prediction model for BigMart's customers."
                },
                "Heart_disease_Prediction": {
                    "url": "https://github.com/moulyabpradeep/Heart_disease_Prediction",
                    "description": "Predicting the risk of heart disease based on medical data."
                },
                
                "insurance": {
                    "url": "https://github.com/moulyabpradeep/insurance",
                    "description": "Predicting insurance claims and customer behavior."
                }
            },
            "🧠 NLP Projects": {
                "ConestogaChatbot": {
                    "url": "https://github.com/moulyabpradeep/ConestogaChatbot",
                    "description": "A chatbot designed for interacting with students at Conestoga College. Developed with Python, RAGs and Vector Database"
                },
                "NLP_Data_Cleaning": {
                    "url": "https://github.com/moulyabpradeep/NLP_Data_Cleaning",
                    "description": "A project for cleaning and preprocessing text data."
                },
                "Movie_reviews_Sentiment_Analysis": {
                    "url": "https://github.com/moulyabpradeep/Movie_reviews_Sentiment_Analysis",
                    "description": "Analyzing sentiment in movie reviews using NLP techniques."
                },
                "NLP_Project_LargeText_to_Voice_to_Speech_to_lipSync": {
                    "url": "https://github.com/moulyabpradeep/NLP_Project_LargeText_to_Voice_to_Speech_to_lipSync",
                    "description": "A large-scale project involving text-to-speech and lip sync for video generation."
                },
                "NLP_Movie_Reviews": {
                    "url": "https://github.com/moulyabpradeep/NLP_Movie_Reviews",
                    "description": "Processing and analyzing movie reviews with NLP."
                }
            },
            "👁 Computer Vision Projects": {
                "ComputerVision_Video_Object_Detect_Segment": {
                    "url": "https://github.com/moulyabpradeep/ComputerVision_Video_Object_Detect_Segment",
                    "description": "Detecting and segmenting objects in video data using computer vision techniques."
                },
                "ComputerVision_Image_Object_Detect_Segment": {
                    "url": "https://github.com/moulyabpradeep/ComputerVision_Image_Object_Detect_Segment",
                    "description": "Detecting and segmenting objects in images using computer vision."
                }
            },
            "📈 Time Series / Forecasting Projects": {
                "Stock_Price_Predictions_Nvidia_ARIMA": {
                    "url": "https://github.com/moulyabpradeep/Stock_Price_Predictions_Nvidia_ARIMA",
                    "description": "Using ARIMA to predict Nvidia stock prices over time."
                },
                "Nvidia_Stock_Predictions_Kfold_cross_val": {
                    "url": "https://github.com/moulyabpradeep/Nvidia_Stock_Predictions_Kfold_cross_val",
                    "description": "Stock prediction with K-fold cross-validation for Nvidia."
                },
                "PricePredictions_DeepLearning_RNN_LSTM": {
                    "url": "https://github.com/moulyabpradeep/PricePredictions_DeepLearning_RNN_LSTM",
                    "description": "Deep learning model using RNN and LSTM for price predictions."
                },
                "TimeSeries_Dataset_Forecasting": {
                    "url": "https://github.com/moulyabpradeep/TimeSeries_Dataset_Forecasting",
                    "description": "Time series dataset forecasting using advanced techniques."
                }
            }
        }

        for category, projects in project_categories.items():
            st.markdown(f"#### {category}")
            for name, details in projects.items():
                st.markdown(f"- [{name}]({details['url']})  \n{details['description']}")




  

#========================


#===================================================================================================================
# Resume Section

# Title
st.markdown("## Resume")


st.subheader("Professional Summary")
st.write("""
Results-driven AI Software Engineer with over 10 years of experience in enterprise software development, system architecture, and distributed systems. Specializes in Python and Java with deep expertise in machine learning, data modeling, AI automation, and business intelligence.

Skilled in building scalable data pipelines, deploying machine learning models, and enabling intelligent data-driven decisions. Passionate about AI-powered automation and cloud-native solutions.
""")

st.subheader("Experience")
st.write("""
**Professor, Data Analytics Dept — SAIT** (Jan 2025 – Present)  
• Teaching Python, Machine Learning, Data Modeling, and BI Reporting.  
• Empowering students with hands-on AI/ML projects and real-world analytics.

**Java Team Lead — Q2, Bangalore** (Jul 2020 – Aug 2023)  
• Developed AWS-based onboarding apps, integrated KYC systems, led backend team.

**Senior Java Developer — ITC Infotech** (Mar 2019 – Jul 2020)  
• Built Erste Bank's paperless onboarding system using microservices.

**Java Developer — Capgemini** (Jun 2018 – Mar 2019)  
• Designed GE Water Purifiers platform with real-time monitoring and filtration insights.

**Associate Java Developer — MeritTrac** (Apr 2014 – Jun 2018)  
• Built online assessment system including RESTful APIs, scoring engine, and exam delivery.
""")

st.subheader("Education")
st.write("""
**SAIT – Post Graduation in AI** (May 2024 – Dec 2024)  
• Advanced ML, Deep Learning, NLP, and model deployment.

**Conestoga College – Big Data & ML** (Sep 2023 – Apr 2024)  
• ETL, OLAP, BI Reporting, Data Warehousing, and full-stack analytics.

**VTU University – B.E. Computer Science** (2007 – 2011)  
• Data Structures, DBMS, OOP, Java, C++, MySQL.
""")

st.subheader("Technical Skills")
st.write("""
**Languages**: Python, Java, SQL, MySQL, HTML/CSS, R  
**Frameworks**: Flask, Streamlit, Spring Boot, Hibernate, JSP, JUnit, PyTest, Maven  
**Developer Tools**: Jupyter Notebook, Anaconda, Git, Docker, VS Code, PyCharm  
**Libraries**: TensorFlow, PyTorch, Scikit-learn, XGBoost, Hugging Face, NLTK, NumPy, Matplotlib
""")

st.subheader("Personal Projects on AI")

st.markdown("**AI Stroke Predictor** | PyCaret, scikit-learn, Streamlit (Jun 2024 – Aug 2024)")
st.markdown("""
• Built supervised Random Forest classifier with 100% Kaggle accuracy.  
• Performed preprocessing, feature selection, and real-time stroke risk prediction.
""")

st.markdown("**Conestoga AI Chatbot** | Flask, PyTorch, RAG, Vector DB (Jan 2024 – Apr 2024)")
st.markdown("""
• Developed chatbot with PDF-based NLP pipeline and vector DB querying.  
• Integrated RAG for contextual, accurate responses from documents.
""")

st.markdown("---")
st.download_button(
    label="📄 Download Full CV",
    data=open("assets/Moulya_CV.pdf", "rb").read(),
    file_name="Moulya_CV.pdf",
    mime="application/pdf"
)

