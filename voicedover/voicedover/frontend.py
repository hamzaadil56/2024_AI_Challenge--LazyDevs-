import streamlit as st
import sounddevice as sd
import soundfile as sf
import os
from datetime import datetime
import requests
from requests.models import Response
import json
from openai.types.chat.chat_completion import ChatCompletion
# from testingTTS import textToSpeech
from testingTTS2 import TTS
# Set up Streamlit layout
st.title("Audio Recorder")

# Define function to record audio


def record_audio(filename, duration=10, sample_rate=44100):
    # Display recording status
    with st.empty():
        st.write("Recording...")
        # Record audio
        audio_data = sd.rec(int(duration * sample_rate),
                            samplerate=sample_rate, channels=2)
        sd.wait()
        # Notify user that recording has stopped
        st.write("Compiling...")

    # Save audio to file
    sf.write(filename, audio_data, sample_rate)
    # Clear the compiling message
    st.empty()


# Display user input for filename and duration
default_filename = f"voicedover/output_{
    datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
filename = st.text_input("Enter filename to save audio:", default_filename)
duration = st.slider("Recording duration (seconds):", 1, 10, 5)

# Display record button
if st.button("Record"):
    # Check if filename is provided
    if not filename:
        st.error("Please enter a filename.")
    else:
        # Record audio and save to file
        # record_audio(filename, duration)
        # st.success(f"Audio recorded and saved as '{filename}'.")

        # # # # Make a GET request to a server
        # response: Response = requests.get(
        #     f"http://127.0.0.1:8000/audio?audio_file_path={filename}")
        # st.write(response.text)

        # if response.text:

        post_data = {
            "prompt": "I want to add breakfast in my todo list"}

        response = requests.post(
            # Use the 'data' parameter to send the request body
            "http://127.0.0.1:8000/call-api", json=post_data)
        st.write(response.text)
        response_json = response.json()
        st.write(type(response_json))
        st.write(response_json)
        # tool_calls = response_json['choices'][0]['message']['tool_calls']

        # # Step 2: check if the model wanted to call a function
        # if tool_calls:
        #     for tool_call in tool_calls:
        #         function_name = tool_call['function']['name']
        #         function_args = json.loads(
        #             tool_call['function']['arguments'])
        #         st.write(function_args)
        #         # call the api from the function args having method and url
        #         if (function_args.get("method") == "get"):
        #             response = requests.get(
        #                 f"{function_args.get('url')}")
        #             st.write(response.text)
        #             outputAudio = TTS(response.text)
        #             st.audio(outputAudio)
        #         elif (function_args.get("method") == "post"):
        #             response = requests.post(
        #                 f"{function_args.get('url')}", json=function_args.get("body"))
        #             st.write(response.text)
        #             outputAudio = TTS(response.text)
        #             st.audio(outputAudio)
        #         elif (function_args.get("method") == "patch"):
        #             response = requests.patch(
        #                 f"{function_args.get('url')}", json=function_args.get("body"))
        #             st.write(response.text)
        #             outputAudio = TTS(response.text)
        #             st.audio(outputAudio)
        #         else:
        #             st.write("Invalid method")
        #             outputAudio = TTS(response.text)
        #             st.audio(outputAudio)
        # response = requests.get(f"http://127.0.0.1:8000/api-details?url={function_args.get("url")}&method={function_args.get("method")}"
        #                         )


# Display folder path where the audio will be saved
st.write(f"Audio will be saved in: `{os.getcwd()}`")

# Display recorded audio player if file exists
if os.path.exists(filename):
    st.audio(filename, format="audio/wav")
