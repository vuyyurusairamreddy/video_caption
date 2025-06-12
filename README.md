# Video Captioning with BLIP

This project is a Python-based tool that automatically generates natural language descriptions (captions) for videos using the BLIP model from Hugging Face. It is designed for tasks like video annotation, dataset labeling, and semantic video indexing using computer vision and NLP.

## Features

- Extracts key frames from input videos.
- Uses BLIP (Bootstrapped Language-Image Pretraining) model for captioning each frame.
- Summarizes multiple captions into a concise description.
- Supports .avi and .mp4 files.
- Runs on CPU or GPU.

## Project Structure

video-caption-blip/
 video_caption_blip.py         # Main script
 requirements.txt              # Dependencies
 README.md                     # This documentation file
 frames/                       # Folder for extracted frames (created automatically)
 videos/                       # Place your input videos here

## Setup Instructions

1. Install dependencies:

Make sure you are using Python 3.7 or above.

pip install -r requirements.txt

## Input Format

- Videos should be in .avi or .mp4 format.
- Place all videos inside the `videos/` folder.
- Example:
  videos/ApplyEyeMakeup.avi
  videos/Typing.avi

## How to Run

Run the script using Python:
''''
python video_caption_blip.py
'''

The script will:
- Read all `.avi` files from the current folder (you can modify this to include `.mp4`).
- Extract 1 frame per second from each video.
- Generate captions using the BLIP model.
- Summarize the captions into a natural description for each video.

## Output

- Captions will be printed in the terminal for each video.
- Example output:A person is typing on a keyboard quickly with both hands. The typing happens in a continuous and focused manner, possibly indicating professional work.



