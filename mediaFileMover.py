## Media file organizer

"""
1. Move all files with the relevant exstension to the proper folder

2. Delete any empty folders in the source

"""

import os, shutil
import mediaFileMoverConfig

## Source directory to start searching for files
src_dir = mediaFileMoverConfig.src_dir

## Scan and move the video files
## Delete the junk
def move_video_files(src_dir):
	for root, dirs, files in os.walk(src_dir):
		path = root.split('/')
		
		## Destination directory to move files
		dest = mediaFileMoverConfig.video_dest

		## Destination for 3D video files
		threed_dest = mediaFileMoverConfig.threed_video_dest
		
		## File exstensions to move
		file_ext = mediaFileMoverConfig.video_ext
		
		for file in files:
			if 'sample' in str(file):
				os.remove(os.path.join(root,file))
				print('Deleted sample file: ' + file)
					
			elif str(file).endswith('.nfo') | str(file).endswith('.srt') | str(file).endswith('.sfv'):
				os.remove(os.path.join(root,file))
				print('Deleted nfo / srt file: ' + file)
			
			elif '3d' in str(file):
				if any(map(str(file).__contains__, file_ext)):
					shutil.move(os.path.join(root,file), os.path.join(threed_dest,file))
					print('Moved: ' + file + ' to ' + threed_dest)
			
			elif any(map(str(file).__contains__, file_ext)):
				shutil.move(os.path.join(root,file), os.path.join(dest,file))
				print('Moved: ' + file + ' to ' + dest)
				

## Scan and move the audio files
def move_audio_files(src_dir):
	for root, dirs, files in os.walk(src_dir):
		path = root.split('/')
		
		## Destination directory to move files
		dest = mediaFileMoverConfig.audio_dest
		
		## File exstensions to move
		file_ext = mediaFileMoverConfig.audio_ext
		
		for file in files:
			if any(map(str(file).__contains__, file_ext)):
				shutil.move(os.path.join(root,file), os.path.join(dest,file))
				print('Moved: ' + file + ' to ' + dest)
				
## Scan and move the image files
def move_image_files(src_dir):
	for root, dirs, files in os.walk(src_dir):
		path = root.split('/')
		
		## Destination directory to move files
		dest = mediaFileMoverConfig.image_dest
		
		## File exstensions to move
		file_ext = mediaFileMoverConfig.image_ext
		
		for file in files:
			if any(map(str(file).__contains__, file_ext)):
				shutil.move(os.path.join(root,file), os.path.join(dest,file))
				print('Moved: ' + file + ' to ' + dest)

## Delete the empty directories
def delete_empty_dirs(src_dir):

	for dirpath, _, _ in os.walk(src_dir, topdown=False):

		if dirpath == src_dir:
			break
		try:
			os.rmdir(dirpath)
			print('Deleted empty dir: ' + dirpath)
		except OSError as e:
			print(e)

## Organize the destination			
def organize_video_dest(dest):

        ## Destination for 3D video files
	threed_dest = mediaFileMoverConfig.threed_video_dest
	
	for root, dirs, files in os.walk(dest):
		path = root.split('/')
		
		for file in files:
			
			if '3d' in str(file):
				shutil.move(os.path.join(root,file), os.path.join(threed_dest,file))
				print('Moved: ' + file + ' to ' + threed_dest)
			
			elif 'sample' in str(file):
				os.remove(os.path.join(root,file))
				print('Deleted sample file: ' + file)
	
def main():

	if mediaFileMoverConfig.move_videos:
		move_video_files(src_dir)
		
	if mediaFileMoverConfig.move_audio:
		move_audio_files(src_dir)
		
	if mediaFileMoverConfig.move_images:
		move_image_files(src_dir)
	
	if mediaFileMoverConfig.delete_empty_dirs:
		delete_empty_dirs(src_dir)
	
	if mediaFileMoverConfig.organize_video_dest:
		organize_video_dest(mediaFileMoverConfig.video_dest)

	print("MediaFileMover operation complete.")

if __name__ == "__main__":
	main()

  
