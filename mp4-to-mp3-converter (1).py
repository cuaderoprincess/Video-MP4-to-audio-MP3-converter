import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file, output_file):
    # Load MP4 File
    video = VideoFileClip(input_file)
    
    # Extract Audio
    audio = video.audio
    
    # Convert to MP3
    audio.write_audiofile(output_file)
    
    # Close the video file
    video.close()

def main():
    print("MP4 to MP3 Converter")
    
    # Get input file
    input_file = input("Enter the path to the MP4 file: ")
    
    # Ensure input file exists
    if not os.path.exists(input_file):
        print("Error: Input file does not exist.")
        return
    
    # Get output file
    output_file = input("Enter the path for the output MP3 file: ")
    
    # Convert file
    print("Converting...")
    try:
        convert_mp4_to_mp3(input_file, output_file)
        print(f"Conversion complete. MP3 file saved as: {output_file}")
    except Exception as e:
        print(f"An error occurred during conversion: {str(e)}")

if __name__ == "__main__":
    main()
