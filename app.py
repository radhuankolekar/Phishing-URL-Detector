import streamlit as st
import random

# ================================
# Page Config
# ================================
st.set_page_config(
    page_title="Phishing Detector 🔐",
    page_icon="🛡️",
    layout="wide"
)

# ================================
# Dark Mode CSS Styling
# ================================
st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background-color: #121212;
        color: #E0E0E0;
    }

    /* Title */
    .main-title {
        font-size: 48px;
        text-align: center;
        font-weight: 800;
        color: #BB86FC;
        margin-bottom: -10px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #B0B0B0;
        margin-bottom: 30px;
    }

    /* Input box */
    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 10px;
        border: 2px solid #BB86FC;
        background-color: #1F1F1F;
        color: #E0E0E0;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 12px;
        background: linear-gradient(90deg, #BB86FC, #6200EE);
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #6200EE, #3700B3);
        transform: scale(1.05);
    }

    /* Results card */
    .result-card {
        background-color: #1F1F1F;
        color: #E0E0E0;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.5);
        text-align: center;
    }

    /* Footer */
    footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 8px;
        background-color: #1F1F1F;
        color: #B0B0B0;
        font-size: 14px;
        border-top: 1px solid #3700B3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================================
# Header
# ================================
st.markdown('<div class="main-title">🔐 Phishing URL Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered tool to keep you safe from malicious websites</div>', unsafe_allow_html=True)

# ================================
# Sidebar
# ================================
st.sidebar.title("⚙️ Navigation")
st.sidebar.markdown("🔍 **Check URL** – Test if a link is safe\n\n📊 **Model Info** – Learn about the ML model\n\n🛡️ **Tips** – Stay safe online")
st.sidebar.markdown("---")
st.sidebar.info("💡 *Always double-check links before clicking!*")

# ================================
# Input Section
# ================================
st.markdown("### 🌐 Enter a website link to analyze")
url = st.text_input("", placeholder="e.g. https://example.com")

if st.button("🔍 Analyze URL"):
    if url:
        # Replace with actual ML model prediction
        prediction = random.choice(["Phishing", "Safe"])
        confidence = round(random.uniform(75, 99), 2)

        # Display Results
        st.markdown("### 📊 Analysis Result")
        col1, col2 = st.columns(2)

        with col1:
            if prediction == "Phishing":
                st.markdown('<div class="result-card">🚨 <h3 style="color:#CF6679;">Phishing Website Detected</h3></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="result-card">✅ <h3 style="color:#03DAC6;">This URL Looks Safe</h3></div>', unsafe_allow_html=True)

        with col2:
            st.markdown(f'<div class="result-card">🎯 <h3>Confidence: {confidence}%</h3></div>', unsafe_allow_html=True)

        st.progress(confidence / 100)

    else:
        st.warning("⚠️ Please enter a URL before analyzing.")

# ================================
# Footer
# ================================
st.markdown(
    """
    <footer>
        <p> <b> © Radhika Kishor Ankolekar</b></p>
    </footer>
    """,
    unsafe_allow_html=True
)
