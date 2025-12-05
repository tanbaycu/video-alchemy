"""
------------------------------------------------------------------------------
 Application: Video to Text Transcriber
 Author: tanbaycu
 Copyright (c) 2025 tanbaycu. All rights reserved.
 
 Description: Extracts audio from video and transcribes it using OpenAI Whisper.
------------------------------------------------------------------------------
"""
import sys
import os
import subprocess
import imageio_ffmpeg
import whisper
import warnings
import argparse

# Suppress warnings
warnings.filterwarnings("ignore")

def extract_and_transcribe(video_path, output_dir=None):
    if not os.path.exists(video_path):
        print(f"Error: File not found: {video_path}")
        return

    base_name = os.path.splitext(os.path.basename(video_path))[0]
    
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        audio_path = os.path.join(output_dir, f"{base_name}.mp3")
        text_path = os.path.join(output_dir, f"{base_name}.txt")
    else:
        audio_path = f"{base_name}.mp3"
        text_path = f"{base_name}.txt"

    print(f"Processing: {video_path}")

    # 1. Extract Audio using FFmpeg directly
    try:
        print("Extracting audio...")
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        
        cmd = [
            ffmpeg_exe,
            "-i", video_path,
            "-vn",
            "-acodec", "libmp3lame",
            "-y",
            audio_path
        ]
        
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Audio saved to: {audio_path}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error extracting audio: {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    # 2. Transcribe Audio
    try:
        print("Transcribing audio (loading model)...")
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(result["text"])
        
        print(f"Transcription saved to: {text_path}")
        
    except Exception as e:
        print(f"Error during transcription: {e}")
    finally:
        # Optional: cleanup mp3
        pass

def main():
    parser = argparse.ArgumentParser(description="Extract audio and transcribe video to text.")
    parser.add_argument("input", help="Path to input video file")
    parser.add_argument("--output", help="Directory to save output files", default=None)
    
    args = parser.parse_args()
    extract_and_transcribe(args.input, args.output)

if __name__ == "__main__":
    main()
