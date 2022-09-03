# importing packages
from email.mime import audio
from pytube import YouTube
from pytube import Playlist
import os

# ask if want to download playlist or video
wants_playlist = input("Would you like to download a playlist? Answer N for an individual video. (Y/N) \n")

# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
# C:\Users\emili\Documents\Repos\Python\MP3Downloader\music

if wants_playlist == 'Y':
    # downloads each video in playlist as mp3
    # url input from user
    playlist = Playlist(str(input("Enter the URL of the playlist you want to download: \n>> ")))
        # https://www.youtube.com/playlist?list=PLDIoUOhQQPlWvtxdeVTG3i7-SlSN0jfWj Vevo 2022 Playlist - VEVO Hot This Week - New Music Videos 2022 (100 videos)
    # for each url in a list:
    for video in playlist.videos:
        # say title
        print(f"Downloading: {video.title}")

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
else:
    # downloads only a single video
    yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))
    
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    
    # download the file
    out_file = video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    # result of success
    print(yt.title + " has been successfully downloaded.")