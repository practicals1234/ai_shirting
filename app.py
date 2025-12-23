import streamlit as st
from google import genai
from PIL import Image
import io

# 1. App Configuration
st.set_page_config(page_title="Shirting AI", page_icon="👔", layout="centered")

# 2. Initialize Client
# Note: Use your actual key from AI Studio
API_KEY = st.secrets.get("GEMINI_API_KEY", "AIzaSyDAJ3tfjY4fD_jPBnMGeZd7bmuIoQHiCRA")
client = genai.Client(api_key=API_KEY)

st.title("👔 Shirting AI Stylist")
st.write("Snap a photo of your cloth pattern to see a curated outfit.")

# 3. The Styling Logic
STYLING_PROMPT = """
Analyze the colors and the linen/cotton texture of the provided fabric. 
Suggest a high-end menswear outfit. Describe a folded dress shirt made of 
this fabric, paired with specific trousers, shoes, and a watch. 
Focus on 'Business Casual' elegance.
"""

# 4. iPhone-Ready Camera Input
captured_image = st.camera_input("Capture Pattern")

if captured_image:
    img = Image.open(captured_image)
    st.image(img, caption="Pattern Captured", width=300)
    
    with st.spinner("AI Stylist is thinking..."):
        try:
            # Unified SDK call for Gemini 2.0 Flash (Fastest for Mobile)
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[STYLING_PROMPT, img]
            )
            
            st.success("Your Curated Look:")
            st.markdown(response.text)
            
            # Note: For V1, we show the description. 
            # In V2, we can pipe this description into Imagen 3 for the visual.
            
        except Exception as e:
            st.error(f"Connection Error: {e}")

st.divider()
st.caption("Testing on iPhone? Tap 'Share' > 'Add to Home Screen' for the full app experience.")