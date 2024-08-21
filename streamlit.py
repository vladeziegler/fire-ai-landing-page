import streamlit as st
from PIL import Image
import base64

# Function to load and encode the image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set background image
def set_bg_hack(main_bg):
    bin_str = get_base64_of_bin_file(main_bg)
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
set_bg_hack('path/to/your/background_image.jpg')  # Replace with your image path

# Custom CSS
st.markdown("""
    <style>
    .big-font {
        font-size:40px !important;
        color: white;
        text-shadow: 2px 2px 4px #000000;
    }
    .medium-font {
        font-size:30px !important;
        color: #3498db;
    }
    .small-font {
        font-size:14px !important;
    }
    .white-font {
        color: white;
    }
    .cta-button {
        font-size: 18px;
        padding: 12px 28px;
        background-color: #e74c3c;
        color: white;
        border-radius: 5px;
        border: none;
        text-decoration: none;
    }
    .cta-button:hover {
        background-color: #c0392b;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<p class="big-font">Be Their Hero: Empower Disaster Victims, Skyrocket Your Business</p>', unsafe_allow_html=True)
st.markdown('<p class="white-font">When disaster strikes, be the first to respond. Our cutting-edge lead generation system ensures you\'re on the scene within minutes, ready to help and grow your business.</p>', unsafe_allow_html=True)

# CTA Button
st.markdown('<a href="https://share.hsforms.com/1BlIBOSplS9KZrEOHWcE0bgs2cn5" target="_blank" class="cta-button">Claim 24 Hours of FREE Leads Now!</a>', unsafe_allow_html=True)

# Benefits Section
st.markdown('<p class="medium-font">Why Top Public Adjusters Choose Us:</p>', unsafe_allow_html=True)
benefits = [
    "🔥 **Laser-Focused Leads:** Only severe incidents you're equipped to handle",
    "🎯 **Hyperlocal Targeting:** Incidents tailored to your specific service areas",
    "⚡ **Lightning-Fast Notifications:** Be first on the scene, every time",
    "💼 **Vetted Contact Gold:** Access premium, verified victim information",
    "🚀 **Instant Team Updates:** Seamlessly sync your sales force via email/SMS"
]
for benefit in benefits:
    st.markdown(benefit)

# Steps Section
st.markdown('<p class="medium-font">Your Success Blueprint in 4 Easy Steps:</p>', unsafe_allow_html=True)
steps = [
    "1. **Customize Your Expertise:** Tell us your specialty (fire, flood, etc.)",
    "2. **Define Your Kingdom:** Specify your service regions",
    "3. **Streamline Communication:** Provide your team's contact details",
    "4. **Watch Your Business Soar:** Close more leads than ever before"
]
for step in steps:
    st.markdown(step)

# FAQ Section
st.markdown('<p class="medium-font">Frequently Asked Questions</p>', unsafe_allow_html=True)
faq = {
    "Who's this secret weapon for?": "Public adjusters, loss assessors, and insurance claims specialists who are ready to dominate their market.",
    "What's the magic behind our system?": "We've engineered a cutting-edge fusion of satellite imagery, AI, and elite data platforms. The result? You're connecting with victims within a mere 5 minutes of disaster striking.",
    "How do we ensure you get the leads that matter?": "Our proprietary algorithm employs 100+ intelligent rules to pinpoint incidents and locations that align perfectly with your expertise and goals.",
    "Do we contact victims directly?": "Never. You're the hero in this story. We provide the intel; you save the day."
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)

# Closing Section
st.markdown('<p class="medium-font">Don\'t Let Another Victim Slip Away</p>', unsafe_allow_html=True)
st.write("In the world of disaster recovery, every second counts. While others are still searching for leads, you could be on-site, building trust, and closing deals.")
st.markdown('<a href="https://share.hsforms.com/1BlIBOSplS9KZrEOHWcE0bgs2cn5" target="_blank" class="cta-button">Start Your 24-Hour FREE Trial Now: Be the Hero They Need</a>', unsafe_allow_html=True)
st.markdown('<p class="small-font"><em>Join the ranks of elite adjusters who\'ve revolutionized their businesses. Your next big success story is just one click away.</em></p>', unsafe_allow_html=True)