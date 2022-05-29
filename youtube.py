import youtube_dl

URL_movie = 'https://www.youtube.com/watch?v=rzJ4IEJZ6XM'

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL_movie])

    