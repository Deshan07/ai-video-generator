import streamlit as st
import replicate
import os

st.set_page_config(page_title="Sri Lanka AI Garage", page_icon="🚗")

st.title("🚗 Sri Lanka AI Garage Video Studio")

# Replicate API Key
api_key = st.text_input("Enter Replicate API Key:", type="password")

prompt = st.text_area("Video Prompt:", "A black modified Toyota Land Cruiser V8 driving in Sri Lanka, cinematic 4k")

if st.button("Generate Video"):
    if not api_key:
        st.error("Please enter your Replicate API key first!")
    else:
        os.environ["REPLICATE_API_TOKEN"] = api_key
        with st.spinner("Generating Video..."):
            try:
                output = replicate.run(
                    "wan-video/wan-2.1-t2v-14b",
                    input={"prompt": prompt}
                )
                st.success("Done!")
                st.video(output)
            except Exception as e:
                st.error(f"Error: {e}")
