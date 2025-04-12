import streamlit as st

st.set_page_config(page_title="Resume", layout="wide")


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


st.title("📄 Resume - Moulya Bangalore Pradeep")
st.markdown("---")

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
