from __future__ import unicode_literals
import youtube_dl

#File to read video URL's from
FILENAME = 'videos.txt'

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    #Set output directory
    'outtmpl': 'Songs/%(title)s.%(ext)s',
}

with open(FILENAME, 'r') as f:
    lines = f.readlines()

for url in lines:
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])



