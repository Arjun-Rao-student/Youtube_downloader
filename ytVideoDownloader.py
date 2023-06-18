import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    video_url = entry_url.get()
    resolution = entry_resolution.get()

    try:
        # Create a YouTube object with the video URL
        yt = YouTube(video_url)

        # Filter streams by resolution
        streams = yt.streams.filter(res=resolution).all()

        if len(streams) > 0:
            # Get the first stream in the list (highest resolution)
            stream = streams[0]

            # Download the video
            stream.download()

            messagebox.showinfo("Arjun Download Complete", "Arjun Anna Video downloaded successfully!")
        else:
            messagebox.showwarning("Resolution not found", "No video with the specified resolution was found.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.title("Arjun YouTube Video Downloader")

# Create labels
label_url = tk.Label(window, text="Video URL:")
label_url.pack()

# Create an entry field for the video URL
entry_url = tk.Entry(window, width=50)
entry_url.pack()

# Create a label for resolution selection
label_resolution = tk.Label(window, text="Resolution (e.g., 720p, 1080p):")
label_resolution.pack()

# Create an entry field for resolution selection
entry_resolution = tk.Entry(window, width=20)
entry_resolution.pack()

# Create a download button
button_download = tk.Button(window, text="Download", command=download_video)
button_download.pack()

# Start the tkinter event loop
window.mainloop()
