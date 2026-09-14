import streamlit as st
import replicate
import os
from gtts import gTTS
import base64

st.set_page_config(page_title="Sri Lanka AI Garage", page_icon="🚗")
st.title("🚗 Sri Lanka AI Garage Video Studio")

token = st.secrets.get("REPLICATE_API_TOKEN", "")

prompt = st.text_area("Video Prompt:", "A young Sri Lankan boy standing near the Lotus Tower in Colombo, surrounded by many parked cars, smiling and looking at the camera, cinematic lighting, 4k")

# කටහඬින් කියවිය යුතු දෙය (Voice text) ඇතුළත් කිරීමට කොටුවක්
voice_text = st.text_input("Voice Text (සිංහලෙන් හෝ ඉංග්‍රීසියෙන් මෙහි ලියන්න):", "Sri Lanka AI Garage facebook page එක follow කරලා, like කරන්න")

if st.button("Generate Video & Audio"):
    if not token:
        st.error("REPLICATE_API_TOKEN not found in Streamlit Secrets!")
    else:
        # 1. වීඩියෝව හැදීම
        with st.spinner("AI Video Engine processing... Please wait 1-2 minutes."):
            try:
                client = replicate.Client(api_token=token.strip())
                output = client.run(
                    "minimax/video-01",
                    input={"prompt": prompt}
                )
                st.success("Video Generated Successfully!")
                
                video_url = str(output)
                st.video(video_url)
                
            except Exception as e:
                st.error(f"Error Details: {e}")
        
        # 2. කටහඬ (Audio) එක සකස් කිරීම
        if voice_text:
            with st.spinner("Generating Voice Audio..."):
                try:
                    # gTTS මඟින් සිංහල/ඉංග්‍රීසි කටහඬ නිර්මාණය කිරීම ('si' සඳහා සිංහල හෝ 'en' සඳහා ඉංග්‍රීසි පාවිච්චි කළ හැක)
                    tts = gTTS(text=voice_text, lang='si', slow=False)
                    audio_file = "output_audio.mp3"
                    tts.save(audio_file)
                    
                    st.success("Audio Generated Successfully!")
                    st.audio(audio_file, format="audio/mp3")
                    
                except Exception as ex:
                    st.warning(f"Audio generation note: {ex}")

# --- Facebook Page Link එක එකතු කිරීම ---
st.markdown("---")
st.markdown("### 🌐 Connect With Us")
facebook_link = "https://www.facebook.com/share/1D4PohRKFK/"
st.markdown(f"👉 **[Click here to visit our Sri Lanka AI Garage Facebook Page]({facebook_link})**", unsafe_allow_html=True)
