# importing packages
from email.mime import audio
from pytube import YouTube
from pytube import Playlist
import os
  
# url input from user
playlist = Playlist(str(input("Enter the URL of the playlist you want to download: \n>> ")))
    # https://www.youtube.com/playlist?list=PLDIoUOhQQPlWvtxdeVTG3i7-SlSN0jfWj Vevo 2022 Playlist - VEVO Hot This Week - New Music Videos 2022 (100 videos)


# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
# C:\Users\emili\Documents\Repos\Python\MP3Downloader\music

# for each url in a list:
for video in playlist.videos:
    # say title
    print(f"Downloading: {video.title}")

    # find video 


    # extract only audio
    audio_of_video = video.streams.filter(only_audio=True).first()
    
    # download the file
    out_file = audio_of_video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    # result of success
    print(video.title + " has been successfully downloaded.")