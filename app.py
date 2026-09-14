import streamlit as st
import replicate
import os
from gtts import gTTS

st.set_page_config(page_title="Sri Lanka AI Garage", page_icon="🚗")

# --- Logo එක සහ ශීර්ෂය (Header) එකතු කිරීම ---
col1, col2 = st.columns([1, 4])

with col1:
    if os.path.exists("logo.jpg"):
        st.image("logo.jpg", width=80)
    elif os.path.exists("logo.png"):
        st.image("logo.png", width=80)
    else:
        st.write("🚗")

with col2:
    st.title("Sri Lanka AI Garage Video Studio")

token = st.secrets.get("REPLICATE_API_TOKEN", "")

prompt = st.text_area("Video Prompt:", "A young Sri Lankan boy standing near the Lotus Tower in Colombo, surrounded by many parked cars, smiling and looking at the camera, cinematic lighting, 4k")

voice_text = st.text_input("Voice Text (සිංහලෙන් හෝ ඉංග්‍රීසියෙන් මෙහි ලියන්න):", "Sri Lanka AI Garage facebook page එක follow කරලා, like කරන්න")

# --- 1. Audio Generate කිරීමේ කොටස ---
st.markdown("### 1. Generate Voice Audio")
if st.button("Generate Audio"):
    if voice_text:
        with st.spinner("Generating Voice Audio..."):
            try:
                tts = gTTS(text=voice_text, lang='si', slow=False)
                audio_file = "output_audio.mp3"
                tts.save(audio_file)
                st.success("Audio Generated Successfully!")
                st.audio(audio_file, format="audio/mp3")
            except Exception as ex:
                st.error(f"Audio error: {ex}")

# --- 2. Video Generate කිරීමේ කොටස ---
st.markdown("### 2. Generate Video")
if st.button("Generate Video"):
    if not token:
        st.error("REPLICATE_API_TOKEN not found in Streamlit Secrets!")
    else:
        with st.spinner("AI Video Engine processing... Please wait a moment."):
            try:
                client = replicate.Client(api_token=token.strip())
                output = client.run(
                    "minimax/video-01:a0f5824987595a892b19bb8f16757df24fc79c3d22b2b11fcda9a90403756e48",
                    input={"prompt": prompt}
                )
                st.success("Video Generated Successfully!")
                
                if hasattr(output, "url"):
                    video_url = output.url
                else:
                    video_url = str(output)
                    
                st.video(video_url)
                
            except Exception as e:
                st.error(f"Error Details: {e}")

# --- Facebook Page Link එක එකතු කිරීම ---
st.markdown("---")
st.markdown("### 🌐 Connect With Us")
facebook_link = "https://www.facebook.com/share/1CmkuWayeL/"
st.markdown(f"👉 **[Click here to visit our Sri Lanka AI Garage Facebook Page]({facebook_link})**", unsafe_allow_html=True)
