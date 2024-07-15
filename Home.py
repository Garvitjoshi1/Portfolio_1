import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Define the info dictionary
info = {
    "Full_Name": "Garvit Joshi",
    "Intro": "Data Science Learning Enthusiast",
    "About": "I am pursuing a Bachelor of Technology in Computer Science and Engineering with a specialization in Data Science from Lovely Professional University, Punjab. Currently, I expect to graduate in 2025.",
    "Email": "garvitjoshi46@gmail.com",
    "Tableau": "https://public.tableau.com/app/profile/garvit.joshi6980/vizzes",
    "Github": "https://github.com/Garvitjoshi1",
    "Linkedin": "https://www.linkedin.com/in/garvitjoshi01/"
}

# Set page configuration
st.set_page_config(page_title='Garvit Joshi Portfolio', layout="wide", page_icon='👨‍💻')

# Intro section
with st.container():
    col1, col2 = st.columns([8, 3])
    full_name = info["Full_Name"]
    intro_text = info["Intro"]
    about_text = info["About"]
    with col1:
        st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,#FFD4DD, #000395);font-size:60px;border-radius:2%;">'
                    f'<span style="color:e0fbfc;">Hi, I\'m {full_name}👋</span><br>'
                    f'<span style="color:white;font-size:17px;">{intro_text}</span></h1>', unsafe_allow_html=True)
        st.write("")
        st.write(about_text)
    with col2:
        try:
            image_url = "https://pbs.twimg.com/profile_images/1812890960474386433/KL0jnSIi_400x400.jpg"
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            image = image.resize((200, 200))  # Resize image if necessary
            st.image(image, caption='Profile Photo', use_column_width=True, output_format='PNG')
            st.markdown(
                f'<style> img {{border-radius: 50%;}} </style>',
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Error loading profile photo: {e}")

# Skills section with images in 2 rows and 5 columns
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4, col5 = st.columns(5)
    skills_images = {
        "Python": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/182px-Python-logo-notext.svg.png",
        "SQL": "https://upload.wikimedia.org/wikipedia/en/thumb/d/dd/MySQL_logo.svg/150px-MySQL_logo.svg.png",
        "Git": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/225px-Git-logo.svg.png",
        "GitHub": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/270px-GitHub_Invertocat_Logo.svg.png",
        "TensorFlow": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/TensorFlow_logo.svg/330px-TensorFlow_logo.svg.png",
        "Keras": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/270px-Keras_logo.svg.png",
        "NumPy": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/180px-NumPy_logo_2020.svg.png",
        "Pandas": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/450px-Pandas_logo.svg.png",
        "Tableau": "https://upload.wikimedia.org/wikipedia/en/thumb/0/06/Tableau_logo.svg/375px-Tableau_logo.svg.png",
        "Excel": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg/180px-Microsoft_Office_Excel_%282019%E2%80%93present%29.svg.png",
        "Jupyter": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/180px-Jupyter_logo.svg.png"
    }
    for idx, (skill, image_url) in enumerate(skills_images.items()):
        try:
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            if idx < 5:
                col1.image(image, caption=skill, use_column_width=False, width=100)
            else:
                col2.image(image, caption=skill, use_column_width=False, width=100)
        except Exception as e:
            st.error(f"Error loading image for {skill}: {e}")

# Career Snapshot Timeline with Projects
with st.container():
    st.subheader('📌 Career Snapshot')
    projects = [
        {
            "title": "Stroke Prediction",
            "subtitle": "Webpage to Predict Stroke Occurrences",
            "description": "Tackled the pressing issue of sudden strokes and the absence of immediate medical services, leading to significant annual fatalities.",
            "details": [
                "Engineered a predictive model with a 93% accuracy score and a 94% cross-validation score.",
                "Executed Feature Selection and Exploratory Data Analysis (EDA) on stroke prediction datasets to acquire a thorough understanding of the data.",
                "Deployed a variety of Machine Learning algorithms to devise a predictive model for early stroke detection.",
                "Transformed the predictive model into an intuitive webpage using Streamlit, enhancing user accessibility."
            ]
        },
        {
            "title": "McDonald’s Menu Nutrition",
            "subtitle": "Exploratory Data Analysis",
            "description": "Investigated the dilemma faced by many individuals who commence working out but grapple with eliminating fast food from their diets.",
            "details": [
                "Furnished actionable insights to advocate healthier dietary choices.",
                "Conducted rigorous statistical analysis on nutritional data to identify outliers and discern patterns.",
                "Leveraged various Python libraries (such as pandas, matplotlib, and seaborn) to plot graphs and visualize the interrelationships among nutrition, calories, and menu items."
            ]
        }
    ]
    for project in projects:
        st.write(f"**{project['title']}**")
        st.write(f"*{project['subtitle']}*")
        st.write(project['description'])
        st.write("- " + "\n- ".join(project['details']))

# Tableau visualization
with st.container():
    st.subheader("📊 Tableau Visualization")
    with st.expander('View my Tableau Work'):
        st.markdown('<iframe src="https://public.tableau.com/app/profile/garvit.joshi6980" width="100%" height="500"></iframe>', unsafe_allow_html=True)

# GitHub section
with st.container():
    st.subheader('👨‍💻 GitHub')
    with st.expander('Explore My GitHub Progress'):
        st.markdown('<iframe src="https://github-readme-stats.vercel.app/api?username=Garvitjoshi1&show_icons=true&theme=dark&count_private=true" width="850" height="350"></iframe>', unsafe_allow_html=True)

# Contact form
with st.container():
    st.subheader("📨 Contact Me")
    st.write("Feel free to reach out to me using the form below:")
    contact_form = """
    <form action="https://formsubmit.co/garvitjoshi46@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <label for="name">Your Name:</label><br>
        <input type="text" id="name" name="name" placeholder="Your name" required><br><br>
        <label for="email">Your Email:</label><br>
        <input type="email" id="email" name="email" placeholder="Your email" required><br><br>
        <label for="message">Your Message:</label><br>
        <textarea id="message" name="message" placeholder="Your message here" rows="4" required></textarea><br><br>
        <button type="submit">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
