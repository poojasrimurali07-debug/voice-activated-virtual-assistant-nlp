# Voice Activated Virtual Assistant Using NLP

A Python-based voice activated virtual assistant that captures spoken commands, converts speech into text, processes the command, and responds using text-to-speech.

## Project Overview

This project demonstrates the use of speech recognition, natural language processing concepts, and text-to-speech technologies to create an interactive voice assistant.

The assistant listens to the user's voice, converts the speech into text, identifies the requested command, performs the corresponding action, and provides a spoken response.

## Features

- Voice input using a microphone
- Speech-to-text conversion
- Command processing
- Text-to-speech responses
- Greeting and conversational commands
- Date and time responses
- Exit command handling
- Error handling for unclear or unavailable speech recognition

## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- NLP concepts
- Google Speech Recognition service

## Project Workflow

1. User provides a voice command.
2. The microphone captures the audio.
3. Speech recognition converts the audio into text.
4. The command is processed and interpreted.
5. The appropriate response is generated.
6. The response is converted into speech.
7. The assistant speaks the response to the user.

## Installation

Install the required Python packages using:

```bash
pip install -r requirements.txt