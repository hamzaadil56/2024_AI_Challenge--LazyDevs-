import streamlit as st
import sounddevice as sd
import soundfile as sf
import os

# Set up Streamlit layout
st.title("Audio Recorder")

# Define function to record audio
def record_audio(filename, duration=5, sample_rate=44100):
    # Record audio
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
    sd.wait()

    # Save audio to file
    sf.write(filename, audio_data, sample_rate)

# Display user input for filename and duration
filename = st.text_input("Enter filename to save audio:", "output.wav")
duration = st.slider("Recording duration (seconds):", 1, 10, 5)

# Display record button
if st.button("Record"):
    # Check if filename is provided
    if not filename:
        st.error("Please enter a filename.")
    else:
        # Record audio and save to file
        record_audio(filename, duration)
        st.success(f"Audio recorded and saved as '{filename}'.")

# Display folder path where the audio will be saved
st.write(f"Audio will be saved in: `{os.getcwd()}`")

# Display recorded audio player if file exists
if os.path.exists(filename):
    st.audio(filename, format="audio/wav")
