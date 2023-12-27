import json
from pathlib import Path

import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain 
import base64

#path 
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file=current_dir / "styles" / "main.css" 
resume_file= current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "me.png"

# --- GENERAL ---
PAGE_TITLE = "Samrat Ganguly ★ CV"
PAGE_ICON = "random"
NAME = "Samrat Ganguly"
DESCRIPTION = """
Software Engineer<br><br>
In my third year currently pursuing CSE with specialization in Artificial Intelligence and Machine 
Learning. Talking about my interests, I like to code with Python and Java. Apart from that I am fascinated by 
concepts of Machine Learning and Deep Learning and want to gain in-depth knowledge in that subject. With 
a passion for innovation, I am eager to contribute my expertise and learn from experienced professionals in 
the field. I aspire to become an AI and software developer. I am always open and enthusiastic in learning and 
adapting to new tech!  
"""
EMAIL = "sganguly@techdevai.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/samrat-ganguly-658a96252/",
    "Instagram": "https://www.instagram.com/samthepixelhunter/"
}
PROJECTS = {
    "Enterprise Chatbot with Azure OpenAI GPT-4 Integration",
    "Image Deduplication App Deployment",
    "Power Automate Flows for Workflow Automation"
}

#page elements
st.set_page_config(
    page_title=PAGE_TITLE, 
    page_icon=PAGE_ICON , 
    layout="wide",
)
rain(
    emoji="🌐",
    font_size=54,
    falling_speed=5,
    animation_length="1",
)

# Function to encode the local cursor file to base64
def encode_cursor_to_base64(file_path):
    with open(file_path, "rb") as cursor_file:
        cursor_content = cursor_file.read()
        encoded_cursor = base64.b64encode(cursor_content).decode("utf-8")
    return encoded_cursor

# Set the path to your local cursor file
local_cursor_path = "squirtle.cur"

# Encode the cursor file to base64
encoded_cursor_data = encode_cursor_to_base64(local_cursor_path)

# Use HTML and CSS to set the cursor with a data URI
st.markdown(
    f"""
    <style>
        body {{
            cursor: url(data:image/x-icon;base64,{encoded_cursor_data}), auto !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Function to load Lottie file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Function to display Lottie animation
def display_lottie_animation(lottie_file, height=200, width=200):
    st_lottie(
        lottie_file,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",  # Adjust quality as needed
        height=height,
        width=width,
        key=None,
    )


# Load multiple Lottie files
lottie_files = [
    {"path": "dragon.json", "height": 150, "width": 150},
    {"path": "T_cap.json", "height": 150, "width": 150},
    {"path": "e.json", "height": 120, "width": 120},
    {"path": "c.json", "height": 120, "width": 120},
    {"path": "h.json", "height": 120, "width": 120},
    {"path": "D_cap.json", "height": 150, "width": 150},
    {"path": "e.json", "height": 120, "width": 120},
    {"path": "v.json", "height": 120, "width": 120},
    {"path": "A_cap.json", "height": 150, "width": 150},
    {"path": "I_cap.json", "height": 150, "width": 150}
    # Add file paths and dimensions as needed
]

columns = st.columns(len(lottie_files))
for column, lottie_data in zip(columns, lottie_files):
    with column:
        display_lottie_animation(
            load_lottiefile(lottie_data["path"]),
            height=lottie_data["height"],
            width=lottie_data["width"],
        )

#pdf and photo
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDF = pdf_file.read()
profile_pic = Image.open(profile_pic)

a,b,c=st.columns([.3,1,2] , gap="small")
with b:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.image(profile_pic,width=490)
with c:
    st.title(NAME)
    st.markdown(f'<div class="dosis">{DESCRIPTION}</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.download_button(
        label="📄 Download Resume",
        data=PDF,
        file_name=resume_file.name,
        mime="application/octet-stream" #as pdf is converted to binary beforee

    )
    st.write("📧", EMAIL)

selected_social_media = {
    "LinkedIn": "https://www.linkedin.com/in/samrat-ganguly-658a96252/",
    "Instagram": "https://www.instagram.com/samthepixelhunter/"
}
st.markdown("<br><br>", unsafe_allow_html=True)

cols = st.columns(len(selected_social_media))

for index, (platform, link) in enumerate(selected_social_media.items()):
    cols[index].write(f"[{platform}]({link})")
#exp
st.write('\n')
st.subheader("Experience & Qualifications")

# Experience details with emojis on separate lines
st.markdown("**AI Intern @ 🌙Crescent Petroleum Sharjah ,United Arab Emirates**")
st.write("Aug'23-Dec'23")
st.write("👉🏼 Developed a highly sophisticated custom chatbot leveraging Azure OpenAI GPT models integrating them with PVA and copilot to generate text based on enterprise data.")
st.write("👉🏼 Integration of advanced Convolutional Neural Network (CNN) models within the Azure Function App environment to perform in-depth image analysis. This included the successful implementation of the imagededup library, significantly enhancing the identification and elimination of duplicate images within the Power Apps framework.")
st.write("👉🏼 Innovatively crafted a user-friendly application within Power Apps, allowing users to capture photos using the camera or gallery and perform real-time comparisons against a comprehensive database of images stored in SharePoint/Dataverse.")
st.write("👉🏼 Implemented Power Automate flows to send emails based on specific instances i.e. new file/record creation in SharePoint")


st.write('\n')
st.subheader("Hard Skills")
st.write("👩‍💻 Programming: Python (Scikitlearn,Pandas), SQL, Java , C/C++")
st.write("📊 Data Visulization: PowerBi, MS Excel, Plotly")
st.write("📚 Modeling: Machine Learning ,  Logistic regression , Decision Trees , Linear Regression")
st.write("🗄️ Databases: MongoDB, MySQL , Azure Database , PVA and Power Automate")


