import os
import os.path
from pathlib import Path
import eyed3


curdir = os.getcwd()
print(os.listdir())
with os.scandir() as dir_entries:
        for entry in dir_entries:

                mp3File = eyed3.load(entry)
                
                try:                        
                        
                        mp3Title = mp3File.tag.title + ".mp3"
 
                        print(entry,mp3Title)
                        os.rename(entry,mp3Title)
                        #mp3File.tag.artist = "Artist Name"
                        #mp3File.tag.album = "Album Name"
                
                        #mp3File.tag.save()
                        
                except:
                        
                        pass

