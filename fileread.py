import os
import os.path
from pathlib import Path

curdir = os.getcwd()
print(os.listdir())
with os.scandir() as dir_entries:
	for entry in dir_entries:
		info = entry.stat()
		print(info.st_mtime)
		
		

