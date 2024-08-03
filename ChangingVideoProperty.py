from moviepy.editor import VideoFileClip

# Load the video
video = VideoFileClip("Untitled video - Made with Clipchamp (6).mp4")

# Resize the video (change resolution)
resized_video = video.resize(newsize=(640, 480))  # New size in (width, height)

# Change frame rate
video_with_new_fps = resized_video.set_fps(24)  # New frame rate

# Write the output video
video_with_new_fps.write_videofile("Untitled video - Made with Clipchamp (6).mp4", codec='libx264')