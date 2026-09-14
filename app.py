import streamlit as st
import replicate
import os

st.set_page_config(page_title="Sri Lanka AI Garage", page_icon="🚗")

st.title("🚗 Sri Lanka AI Garage Video Studio")

# Secret එක හරියටම Environment variable එකට set කිරීම
if "REPLICATE_API_TOKEN" in st.secrets:
    os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]
    api_key = st.secrets["REPLICATE_API_TOKEN"]
else:
    api_key = st.text_input("Enter Replicate API Key:", type="password")
    if api_key:
        os.environ["REPLICATE_API_TOKEN"] = api_key

prompt = st.text_area("Video Prompt:", "A black modified Toyota Land Cruiser V8 driving in Sri Lanka, cinematic 4k")

if st.button("Generate Video"):
    if not os.environ.get("REPLICATE_API_TOKEN"):
        st.error("Replicate API Key එක සෙට් වී නැත! කරුණාකර Secrets පරීක්ෂා කරන්න.")
    else:
        with st.spinner("AI Video Engine processing... Please wait 1-2 minutes."):
            try:
                # Replicate Client එක කෙළින්ම API Token එක සමඟ Initialize කිරීම
                client = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])
                
                output = client.run(
                    "wan-video/wan-2.1-t2v-14b",
                    input={"prompt": prompt}
                )
                st.success("Video Generated Successfully!")
                st.video(output)
            except Exception as e:
                st.error(f"Error: {e}")
