import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        youtubeLink = link.get()
        youtubeObject = YouTube(youtubeLink, on_progress_callback=onProgress)
        video = youtubeObject.streams.get_lowest_resolution()
        title.configure(text=youtubeObject.title, text_color="white")
        finsishedlabel.configure(text="")
        video.download()
        finsishedlabel.configure(text="Downloaded 🙂")
    except Exception as e:
        finsishedlabel.configure(text="Download Error: " + str(e), text_color="red")

def onProgress(stream, chunk, bytes_remaining):
    totalSize = stream.filesize
    bytesDownloaded = totalSize - bytes_remaining
    percentageOfCompletion = bytesDownloaded / totalSize * 100
    percent = str(int(percentageOfCompletion))
    progressPercentage.configure(text=percent + '%')
    progressPercentage.update()

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Frame
app = customtkinter.CTk()
app.geometry("720x480")  # Remove space between dimensions
app.title("Youtube Downloader")

# Interface
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# User input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=360, height=40, textvariable=url_var)
link.pack()

# Download progress
finsishedlabel = customtkinter.CTkLabel(app, text="")
finsishedlabel.pack()

progressPercentage = customtkinter.CTkLabel(app, text="0%")
progressPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Button component
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run program
app.mainloop()
