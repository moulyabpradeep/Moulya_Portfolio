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
    
    "🌐 Web Development / Platform Projects": {
        "TraceRent_AI": "https://github.com/moulyabpradeep/TraceRent_AI",
        "webdev-demos": "https://github.com/moulyabpradeep/webdev-demos",
        "webdev2": "https://github.com/moulyabpradeep/webdev2",
        "SENG8080-3-field_project": "https://github.com/moulyabpradeep/SENG8080-3-field_project",
        "OnlineTestTakingPlatform": "https://github.com/moulyabpradeep/OnlineTestTakingPlatform",
        "folder-management": "https://github.com/moulyabpradeep/folder-management",
        "OnlineCustomerEnrollment": "https://github.com/moulyabpradeep/OnlineCustomerEnrollment/tree/main/.github/workflows"
    }
}

# Display as sectioned tables
for category, projects in project_categories.items():
    st.subheader(category)
    df = pd.DataFrame({"Project Name": list(projects.keys()), "GitHub Link": list(projects.values())})
    df["Project Name"] = df.apply(lambda row: f'<a href="{row["GitHub Link"]}" target="_blank">{row["Project Name"]}</a>', axis=1)
    st.markdown(df[["Project Name"]].to_html(escape=False, index=False), unsafe_allow_html=True)
    st.markdown("---")
