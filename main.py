from pytube import YouTube
import os

url = input("Enter a link : ")

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()

print("Downloading....")
stream.download(filename="video1.mp4")
print("Download completed")
os.system("vlc video1.mp4")
