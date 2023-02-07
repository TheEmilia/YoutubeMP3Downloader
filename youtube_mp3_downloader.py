# IMPORTS
from pytube import Playlist, YouTube
import os

# GLOBAL VARIABLES
destination = "./"

# have user specify destination directory
# TODO ask if they want to do another before exiting
# TODO prevent duplicate errors
# TODO add way to select which portion of videos to download i.e. starting index and ending index, so that, if interrupted, no need to redownload all


def download_single_audio(video, destination, prefix=None):
    # say title
    print(f"Downloading: {video.title}")

    # extract only audio and download the file
    out_file = (
        video.streams.filter(only_audio=True).first().download(output_path=destination)
    )

    # orders video according to playlist position
    if prefix is not None:
        video.title = f"{format(prefix, '.2f')} " + video.title

    # save the file
    base = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)

    # result of success
    print(video.title + " has been successfully downloaded.")


def download_playlist_audio(playlist, destination):
    i = 0.01
    for video in playlist.videos:
        download_single_audio(video, destination, prefix=i)
        i += 0.01


# MENU
menu = """
1. Set Destination Directory
2. Download Single Video's Audio
3. Download Playlist Audio
0. Exit
"""


def main():
    # Display menu, respond to inputs
    # Handle exceptions gracefully

    running = True
    while running:
        try:
            user_input = int(input(menu)[0])
            match user_input:
                case 0:
                    # Allows loop to end, which then calls shutdown()
                    running = False
                case 1:
                    # check for destination to save file
                    destination = (
                        str(
                            input(
                                "Enter path to target directory (leave blank to cancel):"
                            )
                        )
                        or destination
                    )
                case 2:
                    download_single_audio(
                        YouTube(
                            str(
                                input(
                                    "Enter the URL of the video you want to download: \n>> "
                                )
                            )
                        ),
                        destination,
                    )
                case 3:
                    download_playlist_audio(
                        Playlist(
                            str(
                                input(
                                    "Enter the URL of the playlist you want to download: \n>> "
                                )
                            )
                        ),
                        destination,
                    )
        except Exception as e:
            print(
                f"Error occurred: {e}.\nPlease Ensure you are entering a valid menu option."
            )


if __name__ == "__main__":
    main()
