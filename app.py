import json
from pathlib import Path
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
import base64

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "me.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Samrat Ganguly ★ CV"
PAGE_ICON = "🔥"
NAME = "Samrat Ganguly"
DESCRIPTION = """
Software Engineer specializing in Artificial Intelligence and Machine Learning. Passionate about coding, innovation, and continuous learning. Aiming to gain deep expertise in AI, ML, and software development.
"""
EMAIL = "sganguly@techdevai.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/samrat-ganguly-658a96252/",
    "Instagram": "https://www.instagram.com/samthepixelhunter/",
    "GitHub": "https://github.com/samganguly"
}

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# Rain animation on the page
rain(emoji="💻", font_size=54, falling_speed=5, animation_length="1")

# --- FUNCTION DEFINITIONS ---
def encode_cursor_to_base64(file_path):
    with open(file_path, "rb") as cursor_file:
        cursor_content = cursor_file.read()
        encoded_cursor = base64.b64encode(cursor_content).decode("utf-8")
    return encoded_cursor

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def display_lottie_animation(lottie_file, height=200, width=200):
    st_lottie(lottie_file, speed=1, loop=True, quality="high", height=height, width=width)

# Set custom cursor
local_cursor_path = "squirtle.cur"
encoded_cursor_data = encode_cursor_to_base64(local_cursor_path)
st.markdown(f"""
    <style>
        body {{ cursor: url(data:image/x-icon;base64,{encoded_cursor_data}), auto !important; }}
        a:hover {{ color: #ff6347 !important; text-decoration: underline !important; transition: color 0.3s ease-in-out; }}
        .card:hover {{ transform: scale(1.05); transition: transform 0.3s ease-in-out; }}
        .dosis {{ font-family: 'Dosis', sans-serif; color: #333; }}
        h2 {{ font-family: 'Montserrat', sans-serif; color: #4CAF50; }}
        h3 {{ font-family: 'Roboto', sans-serif; color: #007acc; }}
        .fun-text {{ font-family: 'Comic Sans MS', cursive; color: #ff4500; }}
    </style>
    """, unsafe_allow_html=True)

# Load Lottie animations
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
]

columns = st.columns(len(lottie_files))
for column, lottie_data in zip(columns, lottie_files):
    with column:
        display_lottie_animation(load_lottiefile(lottie_data["path"]), height=lottie_data["height"], width=lottie_data["width"])

# --- PDF DOWNLOAD & PROFILE IMAGE ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDF = pdf_file.read()
profile_pic = Image.open(profile_pic_path)

a, b, c = st.columns([.3, 1, 2], gap="small")
with b:
    st.image(profile_pic, width=250)
with c:
    st.title(NAME)
    st.markdown(f'<div class="dosis">{DESCRIPTION}</div>', unsafe_allow_html=True)
    st.download_button(
        label="📄 Download Resume",
        data=PDF,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write(f"📧 {EMAIL}")

# --- SOCIAL MEDIA LINKS ---
st.markdown("<br>", unsafe_allow_html=True)
social_media_cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    social_media_cols[index].markdown(f"[{platform}]({link})", unsafe_allow_html=True)

# --- EXPERIENCE & QUALIFICATIONS ---
st.subheader("Experience & Qualifications")
st.markdown("**AI Intern @ 🌙 Crescent Petroleum, Sharjah, UAE**")
st.write("Aug'23 - Dec'23")
st.write("Developed a sophisticated custom chatbot using Azure OpenAI GPT models integrated with PVA and Copilot for enterprise data generation.")
st.write("Implemented advanced CNN models within Azure Function App for image analysis, utilizing the imagededup library to detect and eliminate duplicate images.")
st.write("Created a user-friendly app in Power Apps for photo capture and real-time comparisons against images stored in SharePoint/Dataverse.")
st.write("Automated email notifications using Power Automate flows based on specific events (e.g., new file creation in SharePoint).")

# --- ADD INTERACTIVE ELEMENTS ---
st.subheader("Fun Fact")
st.write("🎉 Did you know? I'm also a passionate photographer specializing in architectural and wildlife photography!")

st.markdown('<h2>Academic Profile</h2>', unsafe_allow_html=True)
st.write("**Bachelor's degree in CSE with specialization in Artificial Intelligence and Machine Learning**")
st.write("VELLORE INSTITUTE OF TECHNOLOGY, CHENNAI (2021 - Present)")
st.write("CGPA: 7.71")
st.write("**Higher Secondary**")
st.write("LAL BAHADUR SHASTRI SENIOR SEC SCHOOL (2019 - 2021) - XII: 92.6% (CBSE), XI: 97.6%")
st.write("**High School**")
st.write("OUR OWN ENGLISH HIGH SCHOOL, Sharjah, UAE (2017 - 2019) - Grade 10: 96.8% (CBSE)")

st.markdown('<h2>Skills</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="fun-text">
    <p>👩‍💻 Programming: Python, Java, C, C++</p>
    <p>📊 Data Analysis & Reporting: Power BI, Excel</p>
    <p>🛠️ Tools and Frameworks: ScikitLearn, OpenCV, TensorFlow, NLTK, Face Recognition, Firebase, Computer Vision, Git, KNIME, Linux, Raspberry OS</p>
    <p>🗄️ Database Management: SQL, MongoDB</p>
    <p>☁️ Cloud & Automation: Azure Open AI, Power Apps, Power Automate, Power Virtual Agent, Azure Function App</p>
</div>
""", unsafe_allow_html=True)

# --- CERTIFICATIONS ---
st.markdown('<h2>Certifications</h2>', unsafe_allow_html=True)
st.write("- Machine Learning Specialization, Stanford University (Coursera)")
st.write("- Finlatics Business Analyst")
st.write("- C, C++, Java, PHP, MySQL (IIT Bombay Spoken Tutorial)")
st.write("- Python for Data Science (IIT Madras)")
st.write("- Data Analytics Consulting Virtual Internship Program (KPMG AU)")
st.write("- Introduction to Machine Learning (IIT Kharagpur NPTEL)")

# --- PROJECTS ---
st.markdown('<h2>Projects</h2>', unsafe_allow_html=True)
st.markdown("**Smart Vision Aid for the Visually Impaired**")
st.write("Developed an assistive technology device using Raspberry Pi, OpenCV, and Azure Computer Vision API to capture and process visual information for visually impaired individuals. Integrated real-time object recognition, scene understanding, and text extraction, delivering audio descriptions via Text-to-Speech (pyttsx3).")

st.markdown("**Unity Aid**")
st.write("Designed a charity web platform using HTML, CSS, JavaScript, PHP, and MySQL. Optimized back-end with PHP/MySQL, significantly reducing page load times. Created an intuitive admin panel, enhancing administrative efficiency.")

# --- HOBBIES & PERSONAL INTERESTS ---
st.markdown('<h2>Hobbies & Personal Interests</h2>', unsafe_allow_html=True)
st.write("📷 Architectural and Wildlife Photography")
st.write("🌍 Traveling")
st.write("⚽ Playing Football")
st.write("🤝 Volunteering for Social Work")
st.write("🎵 Listening to Music")

# --- LANGUAGE PROFICIENCY ---
st.markdown('<h2>Language Proficiency</h2>', unsafe_allow_html=True)
st.write("**English:** Full professional proficiency")
st.write("**Hindi:** Professional working proficiency")
st.write("**Bengali:** Native or Bilingual proficiency")
st.write("**German:** Elementary proficiency")
