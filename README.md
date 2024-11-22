
# Audio Transcription Tool

> While there are more advanced tools for speech-to-text conversion, such as the [Google Speech-to-Text API](https://cloud.google.com/speech-to-text), having a local script provides certain advantages.

This Python project allows you to extract audio from a video file or directly process an audio file to transcribe the content into text. The project utilizes the `moviepy` library for video and audio processing, and the `SpeechRecognition` library for audio transcription.

## Features

- Extract audio from video files.
- Process audio files directly.
- Transcribe audio using the Google Web Speech API.
- Output the transcription to the console and save it to a `transcription.txt` file.

## Requirements

- Python 3.10 or higher
- [`moviepy`](https://pypi.org/project/moviepy/)
- [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/)
- [`pydub`](https://pypi.org/project/pydub/)

## Setup

To set up the project on your local machine, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

3. **Install the Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

This script can transcribe both video and audio files. It automatically detects the file type based on the extension and processes it accordingly.

### Running the Script

1. **From the Bash Shell:**

   Ensure the script is executable:

   ```bash
   chmod +x transcribe_file.py
   ```

   Then, run the script directly:

   ```bash
   ./transcribe_file.py <file_path>
   ```

   Replace `<file_path>` with the path to your video or audio file.

2. **Using the Python Command:**

   Alternatively, you can run the script with Python:

   ```bash
   python transcribe_file.py <file_path>
   ```

### Supported File Formats

- **Video:** `.mp4`, `.avi`, `.mov`, `.mkv`
- **Audio:** `.wav`, `.mp3`, `.flac`, `.aac`, `.ogg`

### Example Usage

To transcribe a video file:

```bash
./transcribe_file.py example_video.mp4
```

To transcribe an audio file:

```bash
python transcribe_file.py example_audio.wav
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Acknowledgments

- [MoviePy](https://github.com/Zulko/moviepy)
- [SpeechRecognition](https://github.com/Uberi/speech_recognition)
