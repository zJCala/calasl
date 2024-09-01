import streamlit as st
from PIL import Image

# Set the title of the application
st.set_page_config(page_title="Jobeth Albert T. Cala - Portfolio", layout="centered")

# Load your profile image
profile_image = Image.open("profile.jpg") 

# Sidebar - Navigation
st.sidebar.title("Navigation")
options = ["Home", "Autobiography", "Portfolio", "Contact"]
choice = st.sidebar.radio("Go to", options)

# Home Page
if choice == "Home":
    st.title("Welcome to My Portfolio!")
    st.image(profile_image, width=150)
    st.write("""
    Hi! I'm Jobeth Albert T. Cala, an aspiring programmer from Labangon, Cebu City. 
    Explore my autobiography, check out my portfolio, and feel free to get in touch with me.
    """)

# Autobiography Page
elif choice == "Autobiography":
    st.title("Autobiography")
    st.write("""
    ## About Me
    My name is Jobeth Albert T. Cala, and I live in Labangon, Cebu City. My zodiac sign is Leo, which reflects my passion and drive in everything I do. I'm a dog lover, and I find joy in playing computer games and biking.

    ## Academic Journey
    I'm currently in my fourth year of studying Bachelor of Science in Information Technology (BSIT). The primary reason I chose this course is my deep interest in learning how to program. I aspire to become a skilled programmer and am committed to enhancing my coding skills.

    ## Goals and Beliefs
    I am keen on discovering new ways to learn and improve my abilities. I believe that life offers only one chance, so it's essential to seize every moment and make it count.
    """)

# Portfolio Page
elif choice == "Portfolio":
    st.title("Portfolio")
    st.write("### Capstone Project: CIT-U Inventory Management Portal")
    st.write("""
    This project is a comprehensive inventory management system designed and developed by me and my groupmates for our university. It focuses on streamlining the in/out process and provides digital record-keeping along with printing capabilities.
    """)

    st.write("### Skills")
    st.progress(80)  
    st.write("HTML - 80%")

    st.progress(70)  
    st.write("PHP - 70%")

    st.progress(70)  
    st.write("Python - 70%")

    st.progress(60)  
    st.write("JavaScript - 60%")


# Contact Page
elif choice == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out to me via the following contact details:")

    # Display contact information
    st.write("**Phone:** 09760009417")
    st.write("**Email:** jobeth.cala18@gmail.com")
    
    # Contact Form
    contact_form = st.form(key='contact_form')
    name = contact_form.text_input("Name")
    email = contact_form.text_input("Email")
    message = contact_form.text_area("Message")
    
    submit_button = contact_form.form_submit_button("Send")
    
    if submit_button:
        st.success(f"Thank you for your message, {name}! I'll get back to you soon.")

# Footer
st.sidebar.title("About")
st.sidebar.info("This is a simple portfolio web application built with Streamlit. It showcases my autobiography, portfolio, and provides a way to contact me.")
