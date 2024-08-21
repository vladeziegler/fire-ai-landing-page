import streamlit as st
from pathlib import Path
import base64

# Function to read and return the content of the HTML file
def read_html_file(file_path):
    return Path(file_path).read_text()

# Function to encode the image file
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set background image
def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set page config
st.set_page_config(page_title="FastAdjust: Empower Disaster Victims", layout="wide")

# Set background image
set_background('/Users/vladimirdeziegler/Downloads/backgroundfire.jpg')  # Replace with your image path

# Read the HTML content
html_content = read_html_file("index.html")

# Inject the form link into the HTML content
form_link = "https://share.hsforms.com/1BlIBOSplS9KZrEOHWcE0bgs2cn5"
html_content = html_content.replace("{{FORM_LINK}}", form_link)

# Display the HTML content
st.components.v1.html(html_content, height=5000, scrolling=True)

# You can add any dynamic Streamlit elements here if needed
# For example:
# if st.button("Click me for more info"):
#     st.write("Here's some additional information...")