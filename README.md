# MediaFileMover
Configurable script to move media files based on exstension.


The Media File Mover is a simple script that will scan a directory for media files, based on the exstension, and then move them to a directory of your specification.

You can also enable flags to delete any empty directories in the primary source directory.

To setup, edit mediaFileMoverConfig.py (example below):

-------------------------------------------------------------------

	src_dir = 'Your source directory'

	## Destination Directories
	video_dest = 'Your video destination directory'
	threed_video_dest = 'Your 3D video destination directory'
	audio_dest = 'Your music directory'
	image_dest = 'Your image directory'

	## File exstensions
	video_ext = [".avi",".mpeg",".mp4",".divx",".mkv"]
	audio_ext = [".mp3",".ogg",".flac"]
	image_ext = [".mpeg",".bmp",".tiff",".png"]

	## Flags for moving the files
	move_videos=True
	move_audio=True
	move_images=True

	## Flag for deleting destination folder
	delete_empty_dirs=True

	## Flag for organizimg destination folder
	organize_video_dest=False
	
--------------------------------------------------------------------

Place both mediaFileMover.py and mediaFileMoverConfig.py in the same folder. 

To execute, simply use python to run mediaFileMover.py	
