# Life Coach Assistant

This Python script leverages the power of OpenAI's GPT-4 API to serve as your voice-interactive life coach assistant. It's designed to listen to your experiences of the previous day, whether they're positive or negative, and use this information to help guide and support you through the current day.

## Installation

Firstly, make sure Python 3 is installed on your system. If not, you can download it from the official Python website: https://www.python.org/downloads/

After you've installed Python, you'll need to install the necessary packages. To do this, navigate to the project directory and execute the following command:

```sh
pip install -r requirements.txt
```

This command will install all the necessary packages, including the OpenAI API client and the Python SpeechRecognition library.

Next, you'll need to set up an OpenAI API key and save it in a `.env` file in the root directory of the project. The `.env` file should contain the following line:

```sh
OPENAI_API_KEY=<your-api-key>
```

Make sure to replace `<your-api-key>` with your actual OpenAI API key.

## Usage

To interact with the Life Coach Assistant, run the `main.py` script:

```sh
python main.py
```

The script will prompt you to select a microphone from the list of available devices. Simply enter the index of the microphone you want to use.

```python
Available microphones:
0: sepehr's iPhone Microphone
1: Sepehr’s AirP
3: MacBook Pro Microphone
Select a microphone: 1
```

Once you've selected a microphone, the assistant will listen to you narrate experiences from your previous day, be they positive or negative. Using these details, the assistant provides insights, encouragement, and reminders to help navigate your day. You can interact with the assistant naturally, just like you would in a normal conversation.

## Selecting a Microphone

The assistant requires access to a microphone to listen to your narrations. When you run the script, it will display a list of available microphones on your system. To select a microphone, input the index number of the microphone you'd like to use when prompted.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgments

This project uses the OpenAI GPT-4 API and the Python SpeechRecognition library to function.
