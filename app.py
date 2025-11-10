import streamlit as st
import librosa, numpy as np, cv2
from moviepy.editor import ImageSequenceClip, AudioFileClip

st.title(" Lip Sync Generator")
audio = st.file_uploader("Upload audio (.wav file)")
if audio:
    with open("audio.wav", "wb") as f:
        f.write(audio.read())
    st.success("Audio uploaded! (This is a demo)")
    st.video("https://static.streamlit.io/examples/video.mp4")
