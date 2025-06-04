import os

def download_file(link):
    # Fake download (for now). You can update this to real logic later.
    filename = "video.mp4"
    with open(filename, "wb") as f:
        f.write(b"x" * 1024 * 1024 * 10)  # 10MB dummy file
    return filename

def get_file_size(path):
    return round(os.path.getsize(path) / (1024 * 1024), 2)
