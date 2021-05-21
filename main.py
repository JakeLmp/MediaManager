import os

root = "D:/"

try:
    os.isdir(root)
except:
    raise Exception("Root directory not found!")


from mediaMethods import getDuration

duration = getDuration(test)
print(f"Duration of file: {duration}")

import subprocess

vlc_loc = "C:/Program Files/VideoLAN/VLC/vlc.exe"
vlc_file_addon = "file:///"

subprocess.run([vlc_loc, vlc_file_addon + test])
# p = subprocess.Popen([vlc_loc, "file:///" + test])