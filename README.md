# Video Alchemy

> _Turn raw video footage into golden content: Auto-generate PowerPoint slides, transcribe speech to text with Whisper, and upscale video to 4K._

A set of Python tools by **tanbaycu** to process and transform video content.

## Features

- **Video to PPTX**: Extracts key slides from a video based on visual changes and saves them to a PowerPoint presentation.
- **Video to Text**: Extracts audio and uses OpenAI's Whisper model to transcribe speech to text.
- **Video Upscaler**: Upscales video to 4K resolution using OpenCV detail enhancement.

## Installation

1. Clone the repository.
   ```bash
   git clone https://github.com/tanbaycu/video-alchemy.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   _Note: You need `ffmpeg` installed on your system or accessible via `imageio-ffmpeg` (included)._

## Usage

### 1. Video to PowerPoint

Detects slides in a video and converts them to a PPTX presentation.

```bash
python src/video_to_pptx.py input_video.mp4 output.pptx --threshold 2000 --rate 1.0
```

### 2. Video transcription

Extracts audio and transcribes it to a text file.

```bash
python src/video_to_text.py input_video.mp4 --output results/
```

### 3. Video Upscaling (4K)

Upscales a video to 4K resolution.

```bash
python src/video_upscaler.py input_video.mp4 output_4k.mp4
```

## Structure

- `src/`: Source code for the tools.
- `examples/`: Sample inputs and outputs.

## License

Copyright (c) 2025 tanbaycu. All rights reserved.
