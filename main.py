import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedStyle
from pytube import YouTube, Playlist
# Function to choose file path
def choose_file_path():
    path = filedialog.askdirectory()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, path)
# Function to get video information
def get_video_info():
    url = url_entry.get()
    if url:
        try:
            yt = YouTube(url)
            video_info_label.config(text=f"Title: {yt.title}\nAuthor: {yt.author}\nLength: {yt.length} seconds")
        except:
            video_info_label.config(text="Unable to get video information.")
    else:
        video_info_label.config(text="Please enter a valid YouTube URL.")
# Function to download single video
def download_single_video():
    url = url_entry.get()
    if url:
        try:
            yt = YouTube(url)
            resolution = resolution_var.get()
            file_path = file_path_entry.get()
            if file_path:
                video = yt.streams.filter(res=resolution).first()
                video.download(file_path)
                video_info_label.config(text="Video downloaded successfully!", foreground="green")
            else:
                video_info_label.config(text="Please choose a file path.", foreground="red")
        except:
            video_info_label.config(text="Unable to download video.", foreground="red")
    else:
        video_info_label.config(text="Please enter a valid YouTube URL.", foreground="red")
# Function to download playlist videos
def download_playlist_videos():
    url = url_entry.get()
    if url:
        try:
            playlist = Playlist(url)
            resolution = resolution_var.get()
            file_path = file_path_entry.get()
            if file_path:
                for video in playlist.videos:
                    video.streams.filter(res=resolution).first().download(file_path)
                video_info_label.config(text="Playlist videos downloaded successfully!", foreground="green")
            else:
                video_info_label.config(text="Please choose a file path.", foreground="red")
        except:
            video_info_label.config(text="Unable to download playlist videos.", foreground="red")
    else:
        video_info_label.config(text="Please enter a valid YouTube URL.", foreground="red")

# Create the main window
window = tk.Tk()
window.title("YouTube Downloader")
window.state("zoomed")
style = ThemedStyle(window)
style.set_theme("equilux")

# Configure the window background
window.configure(background=style.lookup("TFrame", "background"))

# Set colors and fonts
style.configure(".", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12, "bold"))
style.configure("TButton", font=("Arial", 12, "bold"))

# Create the URL entry field
url_label = ttk.Label(window, text="Enter YouTube URL:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
url_entry = ttk.Entry(window)
url_entry.grid(row=0, column=1, padx=10, pady=10, sticky="WE")

# Create the video resolution selection field
resolution_label = ttk.Label(window, text="Select video resolution:")
resolution_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
resolution_var = tk.StringVar(window, "720p")
resolution_choices = ["144p", "240p", "360p", "480p", "720p", "1080p"]
resolution_dropdown = ttk.Combobox(window, textvariable=resolution_var, values=resolution_choices, state="readonly")
resolution_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="WE")

# Create the file path selection field
file_path_label = ttk.Label(window, text="Choose file path:")
file_path_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")
file_path_entry = ttk.Entry(window)
file_path_entry.grid(row=2, column=1, padx=10, pady=5, sticky="WE")
file_path_button = ttk.Button(window, text="Browse", command=choose_file_path)
file_path_button.grid(row=2, column=2, padx=5, pady=5, sticky="W")

# Create the "Get Video Info" button and label
get_info_button = ttk.Button(window, text="Get Video Info", command=get_video_info)
get_info_button.grid(row=3, column=0, padx=10, pady=10, sticky="WE")
video_info_label = ttk.Label(window, text="", font=("Arial", 12))
video_info_label.grid(row=3, column=1, padx=10, pady=10, sticky="WE")

# Create the "Download Single Video" portion of code
download_single_video_button = ttk.Button(window, text="Download Single Video", command=download_single_video, style="Accent.TButton")
download_single_video_button.grid(row=4, column=0, padx=10, pady=10, sticky="WE")

# Create the "Download Playlist Videos" portion of code
download_playlist_videos_button = ttk.Button(window, text="Download Playlist Videos", command=download_playlist_videos, style="Accent.TButton")
download_playlist_videos_button.grid(row=4, column=1, padx=10, pady=10, sticky="W")
# Start the GUI
window.mainloop()