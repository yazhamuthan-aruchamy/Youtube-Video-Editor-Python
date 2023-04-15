import csv
import os
import moviepy.config as config
from moviepy.editor import *

config.change_settings({"IMAGEMAGICK_BINARY": ""}) #change the dire to your installed path
input_csv_file = r"Your_input_file"  # Input CSV file containing video file names
output_dir = r"Your_outpuf_file" # Output directory
fps = 120 # Set the desired frames per second (FPS)
codec = 'libx264'  # H.264 codec , # Set the output video codec
audio = True # Disable audio encoding
bitrate = '5000k'  # Set the target bitrate for the video (in kilobits per second)
threads = 8 # Set the threads for video export
preset = 'ultrafast' # Set the preset for video export
text = "Your_name" # Set the text clip parameters
fontsize = 70
color = 'white'
with open(input_csv_file, 'r') as csvfile: # Reading the file
    reader = csv.reader(csvfile)
    for row in reader:
        input_filename = row[0]  # Assuming the video file name is in the first column of the CSV
        input_file = os.path.join(os.getcwd(), input_filename)  # Get the input file path using os.path.join
        video_clip = VideoFileClip(input_filename) # Load video clip
        video_width = video_clip.size[0]  # Get the width and height of the video clip
        video_height = video_clip.size[1]
        duration = video_clip.duration  # Set the duration of the video (in seconds)
        video_export_params = {'fps': fps, 'codec': codec, 'audio': audio, 'bitrate': bitrate,
                               'threads': threads, 'preset': preset}    # Set the video export parameters
        logo = (ImageClip(r'Your_logo_path')
                .set_duration(duration)  # Add the watermark to the video clip
                .resize(height=int(video_height/20)) # Resize watermark proportionally to video height
                .margin(right=int(video_width/50), bottom=int(video_height/50), opacity=0) # (optional) logo-border padding
                .set_position(("right", "bottom")))
        text_clip = TextClip(text, fontsize=fontsize, color=color)
        text_clip = text_clip.set_pos("center") # Add the text clip to the video clip
        video_with_watermark = CompositeVideoClip([video_clip, logo, text_clip.set_duration(duration)])
        base_name = input_filename.split("\\")[-1].split(".")[0]   # Get the base file name without extension
        output_file = f"{output_dir}\\{base_name}.mp4"  # Generate the output file name with the base name and incrementing number
        video_with_watermark.write_videofile(output_file, **video_export_params)       # Perform video export
        video_clip.close()   # Close the video clip to free up resources