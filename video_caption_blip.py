import cv2
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import os

# Load BLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

def extract_frames(video_path, output_folder="frames", interval_sec=1):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = 0
    saved_frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % (fps * interval_sec) == 0:
            img_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(img_path, frame)
            saved_frames.append(img_path)
        frame_count += 1

    cap.release()
    return saved_frames

def caption_image(image_path):
    raw_image = Image.open(image_path).convert('RGB')
    inputs = processor(raw_image, return_tensors="pt").to(device)
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def caption_video(video_path):
    print(f"Processing video: {video_path}")
    frames = extract_frames(video_path)
    captions = []
    for frame in frames:
        caption = caption_image(frame)
        captions.append(caption)
    return summarize_captions(captions)

def summarize_captions(captions):
    unique = list(dict.fromkeys(captions))  # Remove duplicates
    return " ".join(unique)

if __name__ == "__main__":
    import glob

    video_files = glob.glob("*.avi")  # or your folder path
    for idx, video in enumerate(video_files, start=1):
        description = caption_video(video)
        print(f"\nVideo #{idx} ({video}):\n{description}\n")
