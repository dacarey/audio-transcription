
# Audio Transcription Project

This Python project extracts audio from a video file or directly processes an audio file to transcribe the audio into text. It uses the `moviepy` library to handle video and audio processing and the `SpeechRecognition` library to transcribe the audio.

## Features

- Extracts audio from video files.
- Directly processes audio files.
- Transcribes audio using Google Web Speech API.
- Outputs transcription to the console and saves it to a `transcription.txt` file.

## Requirements

- Python 3.10 or greater
- `moviepy`
- `SpeechRecognition`
- `pydub`

## Setup

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can use this script to transcribe both video and audio files. The script will automatically detect the file type based on the extension and process it accordingly.

### Running the Script

1. **From the Bash Shell:**

   Make sure the script is executable:

   ```bash
   chmod +x transcribe_file.py
   ```

   Then, you can run the script directly:

   ```bash
   ./transcribe_file.py <file_path>
   ```

   Replace `<file_path>` with the path to your video or audio file.

2. **Using the Python Command:**

   You can also run the script using Python:

   ```bash
   python transcribe_file.py <file_path>
   ```

### Supported File Formats

- **Video:** `.mp4`, `.avi`, `.mov`, `.mkv`
- **Audio:** `.wav`, `.mp3`, `.flac`, `.aac`, `.ogg`

### Example

To transcribe a video file:

```bash
./transcribe_file.py example_video.mp4
```

To transcribe an audio file:

```bash
python transcribe_file.py example_audio.wav
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Acknowledgments

- [MoviePy](https://github.com/Zulko/moviepy)
- [SpeechRecognition](https://github.com/Uberi/speech_recognition)