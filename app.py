import streamlit as st
import replicate
import os

st.set_page_config(page_title="Sri Lanka AI Garage", page_icon="🚗")

st.title("🚗 Sri Lanka AI Garage Video Studio")

# Check API Token from Streamlit Secrets or User Input
api_key = st.secrets.get("REPLICATE_API_TOKEN") if "REPLICATE_API_TOKEN" in st.secrets else st.text_input("Enter Replicate API Key:", type="password")

prompt = st.text_area("Video Prompt:", "A black modified Toyota Land Cruiser V8 driving in Sri Lanka, cinematic 4k")

if st.button("Generate Video"):
    if not api_key:
        st.error("Please enter or configure your Replicate API key first!")
    else:
        os.environ["REPLICATE_API_TOKEN"] = api_key
        with st.spinner("AI Video Engine processing... Please wait 1-2 minutes."):
            try:
                output = replicate.run(
                    "wan-video/wan-2.1-t2v-14b",
                    input={"prompt": prompt}
                )
                st.success("Video Generated Successfully!")
                st.video(output)
            except Exception as e:
                st.error(f"Error: {e}")
