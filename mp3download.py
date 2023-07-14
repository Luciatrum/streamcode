import yt_dlp

# Set the default destination directory
default_directory = r"C:\Users\lucia\Music\Playlists\Battle Music"

# Specify the destination directory
destination = input("Enter the destination (leave blank for default directory: {}) ".format(default_directory)) or default_directory

# Get the video URL from the user
video_url = input("Enter the YouTube video URL: ")

# Create options for yt-dlp
options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': destination + '/%(title)s.%(ext)s',
    'verbose': True,  # Enable verbose output
}

# Download the audio using yt-dlp
with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([video_url])

# Print the success message
print("Audio has been successfully downloaded and converted to MP3.")
