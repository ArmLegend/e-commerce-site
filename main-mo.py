#!/usr/bin/env python3


import os
from moviepy.editor import VideoFileClip
from tqdm import tqdm

# Prompt the user for the directory path containing video files
video_directory = input("Enter the path to the directory containing your video files: ")

# Check if the entered path exists
if not os.path.exists(video_directory):
    print("The specified directory does not exist.")
    exit(1)

# Initialize a variable to store the total length of videos
total_length = 0

# Count the number of video files for the progress bar
video_count = 0
for root, _, files in os.walk(video_directory):
    for filename in files:
        if filename.lower().endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv')):
            video_count += 1

# Create a progress bar
with tqdm(total=video_count, desc="Processing Videos") as pbar:
    # Iterate over all files in the directory
    for root, _, files in os.walk(video_directory):
        for filename in files:
            if filename.lower().endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv')):
                video_path = os.path.join(root, filename)
                try:
                    video_clip = VideoFileClip(video_path)
                    video_duration = video_clip.duration
                    total_length += video_duration
                    video_clip.close()
                except Exception as e:
                    print(f"Error processing {video_path}: {str(e)}")
                pbar.update(1)  # Update the progress bar

# Convert the total length to hours, minutes, and seconds
total_length_hours = int(total_length // 3600)
total_length_minutes = int((total_length % 3600) // 60)
total_length_seconds = int(total_length % 60)

# Print the total length of videos
print(f"Total length of videos in the directory: {total_length_hours} hours, {total_length_minutes} minutes, {total_length_seconds} seconds")

