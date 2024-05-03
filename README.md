# VoicedOver

## 2024 AI Challenge – Lazy Devs
"Talk your way through anything."

### Problem
In today's fast-paced world, speed and efficiency in digital interactions are essential, yet many technologies still fall short in delivering instant results. VoicedOver addresses this need by significantly enhancing user interaction speeds with digital platforms, advancing our global pursuit of faster technological responses.

### Solution
VoicedOver enables seamless communication with devices through voice commands, allowing users to operate applications without physical interaction. This enhances efficiency and accessibility, particularly beneficial for e-commerce platforms.

### Target Audience
The initial focus of VoicedOver is on e-commerce stores, with plans to expand to other sectors in the future.

## Engineering

### High-Level Design
VoicedOver is an API tool designed to evolve into a microservice. It accepts audio inputs, processes them using advanced AI technologies, and performs tasks within integrated applications.

### How It Works
1. **Audio Input**: Captures audio commands from the user.
2. **Speech to Text**: Uses OpenAI's Whisper to convert audio into text.
3. **Command Processing**: The text is processed by the OpenAI Assistant to determine and execute the required commands.
4. **Contextual Understanding**: GPT-4 Turbo enhances the response with relevant context.
5. **Text to Speech**: The final response is converted back into audio using TTS-1 for output to the user.

### Role of Generative AI
Generative AI is pivotal in interpreting user intent from audio inputs, executing appropriate actions, and providing audio responses, streamlining user interactions with digital platforms.

### Technologies
- Python 3.12
- Poetry
- FastAPI 0.110.2
- OpenAI Whisper
- OpenAI GPT-4 Turbo
- OpenAI TTS-1
- Streamlit

## Installation and Running the Application

### Prerequisites
Ensure you have Python 3.12 installed on your system. You can download it from [Python's official site](https://www.python.org/downloads/).

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd voicedover
   ```
3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
If poetry is not installed, you can always install it via:
 ```bash
   pip install poetry
   ```

### Running the Application
1. In one terminal, start the Streamlit frontend:
   ```bash
   streamlit run frontend.py
   ```
2. In another terminal, launch the FastAPI backend with Uvicorn:
   ```bash
   poetry run uvicorn voicedover.main:app --reload
   ```

## Results and Analysis
Our testing focused on the core functionalities such as listing, adding, and updating to-do items. The application demonstrated high reliability and user-friendliness, with only minor issues in update functionalities.

---

For more information or if you encounter any issues, please open an issue in this repository.
