import moviepy.config as config
from moviepy.editor import *
config.change_settings({"IMAGEMAGICK_BINARY": ""}) #change the dire to your installed path
input_file = r"Your_input_file" # Input video file name
output_dir = r"Your_outpuf_file" # Output directory
video_clip = VideoFileClip(input_file)
video_width = video_clip.size[0] # Get the width and height of the video clip
video_height = video_clip.size[1]
fps = 120   # Set the desired frames per second (FPS)
duration = video_clip.duration # Set the duration of the video (in seconds)
output_dir = r"Your_outpuf_file"  # Set the output video filename and codec
codec = 'libx264'  # H.264 codec
audio = True  # Disable audio encoding
bitrate = '5000k'  # Set the target bitrate for the video (in kilobits per second)
# For other hardware acceleration options, refer to FFmpeg documentation # For FFmpeg: '-c:v h264_nvenc' for NVIDIA GPU acceleration # For FFmpeg: '-c:v hevc_nvenc' for NVIDIA GPU acceleration with H.265 codec  # Set the hardware acceleration options (if available)
hw_acceleration = '-c:v h264_nvenc'
video_export_params = {'fps': fps, 'codec': codec, 'audio': audio, 'bitrate': bitrate,
                       'threads': 8, 'preset': 'ultrafast'} # Remove 'hw_acceleration' from video_export_params dictionary
logo = (ImageClip(r'Your_logo_path') # Add the watermark to the video clip
        .set_duration(duration)
        .resize(height=int(video_height/20)) # Resize watermark proportionally to video height
        .margin(right=int(video_width/50), bottom=int(video_height/50), opacity=0) # (optional) logo-border padding
        .set_position(("right", "bottom")))
txt_clip = TextClip("Your_name", fontsize=70, color='white')  # Add text clip
video_clip = video_clip.set_duration(duration) # Set the duration of the video clip
video_with_watermark = CompositeVideoClip([video_clip, logo, txt_clip.set_position(("center", "center"))]) # Add the watermark and text clip to the video clip
video_with_watermark = video_with_watermark.set_duration(duration)   # Set the duration of the video clip
base_name = input_file.split("\\")[-1].split(".")[0]  # Get the base file name without extension # Perform video export
output_file = f"{output_dir}\\{base_name}.mp4"  # Generate the output file name with the base name and incrementing number
video_with_watermark.write_videofile(f"{output_dir}\\{base_name}.mp4", **video_export_params)

