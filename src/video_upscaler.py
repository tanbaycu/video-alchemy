"""
------------------------------------------------------------------------------
 Application: 4K Video Upscaler
 Author: tanbaycu
 Copyright (c) 2025 tanbaycu. All rights reserved.
 
 Description: Upscales video to 4K resolution using OpenCV detail enhancement.
------------------------------------------------------------------------------
"""
import cv2
import numpy as np
from moviepy import VideoFileClip
import argparse
import os

def upscale_video(input_path, output_path):
    print(f"Opening video: {input_path}")
    cap = cv2.VideoCapture(input_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Target 4K
    target_width = 3840
    target_height = 2160
    
    temp_video_path = "temp_4k_no_audio.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(temp_video_path, fourcc, fps, (target_width, target_height))
    
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        upscaled = cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_CUBIC)
        enhanced = cv2.detailEnhance(upscaled, sigma_s=10, sigma_r=0.15)
        
        out.write(enhanced)
        frame_count += 1
        if frame_count % 10 == 0:
            print(f"Processed {frame_count}/{total_frames} frames", end='\r')

    cap.release()
    out.release()
    print("\nMerging audio...")
    
    try:
        original_clip = VideoFileClip(input_path)
        new_clip = VideoFileClip(temp_video_path)
        final_clip = new_clip.set_audio(original_clip.audio)
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', logger=None)
        
        original_clip.close()
        new_clip.close()
        final_clip.close()
        
        if os.path.exists(temp_video_path):
            os.remove(temp_video_path)
        print(f"Done! Saved to: {output_path}")
    except Exception as e:
        print(f"Error merging audio: {e}")

def main():
    parser = argparse.ArgumentParser(description="Upscale video to 4K.")
    parser.add_argument("input", help="Path to input video file")
    parser.add_argument("output", help="Path to output video file")
    
    args = parser.parse_args()
    upscale_video(args.input, args.output)

if __name__ == "__main__":
    main()
