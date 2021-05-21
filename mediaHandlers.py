import os
import vlc
import time

class media:
    def __init__(self, video_file, subtitle_file=None):
        source_file = os.path.normpath(source_file)
        if os.path.isfile(source_file):
            self.file_path = source_file
        else: 
            raise Exception(f"Error: non-existing file path provided ({source_file})")
        
        
        
        
#         self.duration = self.getDuration(self.file_path)
#         self.imdb_link
    
    def check_fileType(self, file_str):
        extension = file_str.split('.')[-1] # get file extension
        types = {video:["mp4", "mkv", "avi"], subtitles:["srt"]}
        
        if not (extension in types[video] or extension in types[subtitles]):
            raise OSError(f"File type not recognized ({extension})")
    
    
    def getDuration(self, source):
        '''Credits to https://www.geeksforgeeks.org/vlc-module-in-python-an-introduction/'''
        # creating a vlc instance
        vlc_instance = vlc.Instance()

        # creating a media player
        player = vlc_instance.media_player_new()

        # creating a media
        media = vlc_instance.media_new(source)

        # setting media to the player
        player.set_media(media)

        # play the video
        player.play()

        # wait time
        time.sleep(0.5)

        # getting the duration of the video
        duration = player.get_length()

        # printing the duration of the video
        return duration
        
# END OF media

class movie(media):
    def __init__(self, source_dir):
        source_dir = os.path.normpath(source_dir)
        if os.path.isfile(source_file):
            self.file_path = source_dir
        else: 
            raise Exception(f"Error: non-existing file path provided ({source_dir})")
        
# END OF movie

class series(media):
    def __init__(self, source_dir):
        source_dir = os.path.normpath(source_dir)
        if os.path.isfile(source_file):
            self.file_path = source_dir
        else: 
            raise Exception(f"Error: non-existing file path provided ({source_dir})")
        
        