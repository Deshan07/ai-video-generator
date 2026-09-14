import streamlit as st
import replicate
import os

st.set_page_config(page_title="Sri Lanka AI Garage", page_icon="🚗")
st.title("🚗 Sri Lanka AI Garage Video Studio")

token = st.secrets.get("REPLICATE_API_TOKEN", "")

prompt = st.text_area("Video Prompt:", "A black modified Toyota Land Cruiser V8 driving in Sri Lanka, cinematic 4k")

if st.button("Generate Video"):
    if not token:
        st.error("REPLICATE_API_TOKEN not found in Streamlit Secrets!")
    else:
        with st.spinner("AI Video Engine processing... Please wait 1-2 minutes."):
            try:
                client = replicate.Client(api_token=token.strip())
                output = client.run(
                    "wan-video/wan-2.1-t2v-14b",
                    input={"prompt": prompt}
                )
                st.success("Video Generated Successfully!")
                st.video(output)
            except Exception as e:
                st.error(f"Error Details: {e}")
