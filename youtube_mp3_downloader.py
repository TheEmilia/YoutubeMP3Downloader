# importing packages
from pytube import YouTube, Playlist
import os

# TODO ask if they want to do another before exiting
# TODO prevent duplicate errors
# TODO add way to select which portion of videos to download i.e. starting index and ending index, so that, if interrupted, no need to redownload all

# check for destination to save file
print("Enter the destination (leave blank for default directory)")
destination = str(input(">> ")) or './MP3Downloader/music'

i = 0.0
playlist = Playlist(
    str(input("Enter the URL of the playlist you want to download: \n>> ")))

# for each url in a list:
for video in playlist.videos:
    # say title
    print(f"Downloading: {video.title}")

    # orders video according to playlist position
    video.title = f"{format(i, '.2f')} " + video.title
    i += 0.01

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
