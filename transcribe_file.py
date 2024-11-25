#!/usr/bin/env python3

import os
import sys

import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
from moviepy.video.io.VideoFileClip import VideoFileClip


def extract_audio_from_video(video_path, audio_output_path):
    """Extract audio from a video file."""
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_output_path)
    return audio_output_path


def transcribe_audio_with_timestamps(audio_path, chunk_length_ms=30000):
    """Transcribe audio and add timestamps."""
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_wav(audio_path)
    chunks = make_chunks(audio, chunk_length_ms)

    transcription = ""

    for i, chunk in enumerate(chunks):
        chunk_filename = f"chunk{i}.wav"
        chunk.export(chunk_filename, format="wav")

        with sr.AudioFile(chunk_filename) as source:
            audio_data = recognizer.record(source)

            try:
                chunk_transcription = recognizer.recognize_google(audio_data)
                timestamp = i * chunk_length_ms / 1000
                transcription += f"[{timestamp:.2f}s]: {chunk_transcription}\n"
                print(f"[{timestamp:.2f}s]: {chunk_transcription}")

            except sr.UnknownValueError:
                print(f"Chunk {i} could not be understood.")
            except sr.RequestError as e:
                print(
                    f"Could not request results from Google Speech Recognition service; {e}"
                )

        os.remove(chunk_filename)

    with open("transcription_with_timestamps.txt", "w", encoding="utf-8") as file:
        file.write(transcription)


def main(input_path):
    """Main function to determine file type and transcribe."""
    file_extension = os.path.splitext(input_path)[1].lower()

    if file_extension in [".mp4", ".avi", ".mov", ".mkv"]:
        print("Video file detected. Extracting audio...")
        audio_output_path = "output_audio.wav"
        audio_path = extract_audio_from_video(input_path, audio_output_path)
    elif file_extension in [".wav", ".mp3", ".flac", ".aac", ".ogg"]:
        print("Audio file detected. Transcribing...")
        audio_path = input_path
    else:
        print("Unsupported file format. Please provide a video or audio file.")
        return

    transcribe_audio_with_timestamps(audio_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe_file.py <file_path>")
    else:
        file_path = sys.argv[1]
        main(file_path)
