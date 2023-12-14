import os
import time
import shutil



def file_orgnaizer():
    """This function automatically sorts files in a 
    directory into categorized folders"""
    
    file_ext = {".jpg":"Images", ".jpeg":"Images", ".jpe":"Images", ".jif":"Images", ".jfif":"Images", ".jfi":"Images", 
                 ".png":"Images", ".gif":"Images", ".webp":"Images", ".tiff":"Images", ".tif":"Images", ".psd":"Images", 
                 ".raw":"Images", ".arw":"Images", ".cr2":"Images", ".nrw":"Images", ".k25":"Images", ".bmp":"Images", 
                 ".dib":"Images", ".heif":"Images", ".heic":"Images", ".pdf":"Documents", ".json":"Documents", ".csv":"Documents", ".py":"Documents", ".txt":"Documents", 
                ".docx":"Documents", ".zip":"Documents", ".webm":"Videos", ".mpg":"Videos", ".mp2":"Videos", ".mpeg":"Videos", ".mpe":"Videos", 
                 ".mpv":"Videos", ".ogg":"Videos", ".mp4":"Videos", ".mp4v":"Videos", ".m4v":"Videos", 
                 ".avi":"Videos", ".wmv":"Videos", ".mov":"Videos", ".qt":"Videos", ".flv":"Videos", ".swf":"Videos", 
                 ".avchd":"Videos"}
    
    def get_file_extension(file):
        _, file_extension = os.path.splitext(file)
        return file_extension
    
    user_directory = input('Enter the path to the desired directory: ')
    os.chdir(user_directory)
    
    os.mkdir('Images')
    os.mkdir('Videos')
    os.mkdir('Documents')
    
    for file in os.listdir():
        _, file_extension = os.path.splitext(file)
        if file_extension in file_ext:
            shutil.move(file, )
        