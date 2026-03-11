# app.py
import streamlit as st
from audio_to_text import audio_to_text
from summarize import summarize_text
from action_extract import extract_action_items

st.set_page_config(page_title="AI Meeting Summarizer", layout="wide")
st.title("📝 AI Meeting Summarizer + Action Item Extractor")

uploaded_file = st.file_uploader("Upload Audio (.mp3/.wav) or Text (.txt)", type=["mp3", "wav", "txt"])

if uploaded_file:
    if uploaded_file.type in ["audio/mpeg", "audio/wav"]:
        # Save temporary audio file
        with open("temp_audio.mp3", "wb") as f:
            f.write(uploaded_file.getbuffer())
        transcript = audio_to_text("temp_audio.mp3")
    else:
        transcript = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Transcript")
    st.write(transcript)

    st.subheader("📝 Summary")
    summary = summarize_text(transcript)
    st.write(summary)

    st.subheader("✅ Action Items")
    tasks = extract_action_items(transcript)
    if tasks:
        st.table(tasks)
    else:
        st.write("No action items found!")
