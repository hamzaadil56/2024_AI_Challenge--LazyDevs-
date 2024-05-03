import streamlit as st
import sounddevice as sd
import soundfile as sf
import os
from datetime import datetime
import requests
from requests.models import Response
import json
from openai.types.chat.chat_completion import ChatCompletion
from testingTTS2 import TTS

# Set up Streamlit layout
st.title("VoicedOver")

# Define function to record audio


def record_audio(filename, duration=10, sample_rate=44100):
    # Display recording status
    recording_status = st.empty()
    recording_status.write("Recording...")

    # Record audio
    audio_data = sd.rec(int(duration * sample_rate),
                        samplerate=sample_rate, channels=2)
    sd.wait()

    # Notify user that recording has stopped
    recording_status.write("Compiling...")

    # Save audio to file
    sf.write(filename, audio_data, sample_rate)

    # Notify user that compilation is complete
    recording_status.write("Compiled")


# I want to create a function for calling the api for response-audio and getting response
# def call_api(prompt):
#     # Make a GET request to a server
#     response: Response = requests.get(


# Display user input for filename and duration
default_filename = f"voicedover/speech{
    datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
duration = st.slider("Recording duration (seconds):", 1, 10, 5)

# Display record button
if st.button("Record"):
    # Check if filename is provided
    if not default_filename:
        st.error("Please enter a filename.")
    else:
        # Record audio and save to file
        record_audio(default_filename, duration)
        st.success(f"Audio recorded and saved as '{default_filename}'.")

        # # Make a GET request to a server
        response: Response = requests.get(
            f"http://127.0.0.1:8000/audio?audio_file_path={default_filename}")
        st.write(response.text)
        if response.text:

            post_data = {
                "prompt": response.text}

            response = requests.post(
                # Use the 'data' parameter to send the request body
                "http://127.0.0.1:8000/call-api", json=post_data)
            response_json = response.json()
            completion = response_json.get("completion")
            messages = response_json.get("messages")
            tool_calls = completion['choices'][0]['message']['tool_calls']

            # Step 2: check if the model wanted to call a function
            if tool_calls:
                for tool_call in tool_calls:
                    function_name = tool_call['function']['name']
                    function_args = json.loads(
                        tool_call['function']['arguments'])
                    # call the api from the function args having method and url
                    if (function_args.get("method") == "get"):
                        response = requests.get(
                            f"{function_args.get('url')}")

                        response = requests.post(
                            "http://127.0.0.1:8000/response-audio", json={"response_json": json.dumps(response.text)})
                        response_json = response.json()

                        outputAudio = TTS(
                            response_json['choices'][0]['message']['content'])
                        st.audio("voicedover/speech.mp3", format="audio/mp3")
                    elif (function_args.get("method") == "post"):
                        query = function_args.get("query")
                        response = requests.post(
                            f"{function_args.get('url')}", params=query)
                        response = requests.post(
                            "http://127.0.0.1:8000/response-audio", json={"response_json": json.dumps(response.text)})
                        response_json = response.json()

                        outputAudio = TTS(
                            response_json['choices'][0]['message']['content'])
                        st.audio("voicedover/speech.mp3", format="audio/mp3")
                    elif (function_args.get("method") == "patch"):
                        response = requests.patch(
                            f"{function_args.get('url')}", json=function_args.get("body"))
                        messages.append(
                            {"role": "system", "content": response.text})
                        outputAudio = TTS(response.text)
                        st.audio("/speech.mp3")
                    else:
                        messages.append(
                            {"role": "system", "content": response.text})
                        outputAudio = TTS(response.text)
                        st.audio(outputAudio)
                    # response = requests.get(f"http://127.0.0.1:8000/api-details?url={function_args.get("url")}&method={function_args.get("method")}"
                    #                         )
