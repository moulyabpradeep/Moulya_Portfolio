import streamlit as st
from PIL import Image

st.set_page_config(page_title="Moulya Bangalore Pradeep's Portfolio", layout="wide")

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

# Load and display profile image
col1, col2 = st.columns([1, 3])
with col1:
    image = Image.open("assets/profile.jpg")  # Ensure this image exists in the assets folder
    st.image(image, width=200)

with col2:
    st.title("Moulya Bangalore Pradeep")
    st.markdown("""
    #### Professor | AI & ML Enthusiast | Senior Java Python Developer
    Passionate about building AI-driven applications and sharing knowledge with the next generation of tech leaders.
    Over 10+ years of experience in Java, Python, Machine Learning, and Cloud-native solutions.
    """)
    st.download_button(
        label="📄 Download CV",
        data=open("assets/Moulya_CV.pdf", "rb").read(),
        file_name="assets/Moulya_CV.pdf",
        mime="application/pdf"
    )

st.markdown("---")

st.header("🔗 Explore")

col_a, col_b = st.columns(2)

with col_a:
    st.page_link("pages/Resume.py", label="📋 View Resume", icon="📄")

with col_b:
    st.page_link("pages/Projects.py", label="💻 View Projects", icon="💼")
