import os
import pathlib
import vlc
import time

class video:
    def __init__(self, source_file, subtitle_file=None):
        
        # Perform checks on source_file
        self.source_file = pathlib.Path(source_file)
        self.check_fileExists(self.source_file)
        self.check_fileType(self.source_file)
        
        # If given, perform checks on subtitle_file. If not given, subtitle_file = None
        if subtitle_file: 
            self.subtitle_file = pathlib.Path(subtitle_file)
            self.check_fileExists(self.subtitle_file)
            self.check_fileType(self.subtitle_file)
        else:
            self.subtitle_file = None
        
    
    def check_fileExists(self, file_handle):
        if not file_handle.exists():
            raise OSError(f"File does not exist ({file_handle})")
        if not file_handle.is_file():
            raise OSError(f"Provided path is not a file ({file_handle})")
    
    def check_fileType(self, file_handle):
        extension = file_handle.suffix # get file extension
        types = {"video":[".3gp", ".asf", ".wmv", ".flv", ".mov", ".wav", ".mp4", ".mkv", ".avi"], \
                 "subtitles":[".aqt", ".cvd", ".dks", ".jss", ".sub", ".ttxt", ".mpl", ".txt", ".pjs", ".psb", ".rt", ".smi", ".ssf", ".srt", ".ssa", ".ass", ".svcd", ".usf", ".idx"]}
        
        if not (extension in types["video"] or extension in types["subtitles"]):
            raise OSError(f"File type not recognized ({extension})")
    
    
    def getDuration(self,):
        '''Credits to https://www.geeksforgeeks.org/vlc-module-in-python-an-introduction/'''
        vlc_instance = vlc.Instance()
        
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new(self.source_file)
        
        player.set_media(media)
        player.play()

        time.sleep(0.1)

        # getting the duration of the video
        duration = player.get_length()
        
        player.stop()
        
        return duration
        
# END OF media

class movie:
    def __init__(self, source_dir):
        self.source_dir = pathlib.Path(source_dir)
        self.check_dirExists(self.source_dir)
        
        
        
    def check_dirExists(self, dir_handle):
        if not dir_handle.exists():
            raise OSError(f"Directory does not exist ({dir_handle})")
        if not dir_handle.is_dir():
            raise OSError(f"Provided path is not a directory ({dir_handle})")
    
    
# END OF movie

class series:
    def __init__(self, source_dir):
        source_dir = os.path.normpath(source_dir)
        if os.path.isfile(source_file):
            self.file_path = source_dir
        else: 
            raise Exception(f"Error: non-existing file path provided ({source_dir})")
        
        