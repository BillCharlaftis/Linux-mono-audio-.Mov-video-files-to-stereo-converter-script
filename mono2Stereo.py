#replace /name/your/path with the path you need to convert. Tested on Linux

import glob, os

os.chdir("/name/your/path/")

forig = []

for file in glob.glob("*.MOV"):
	forig.append(file)

print("\nFound .mov files :"+str(forig)+"\n\n")

for i in range(0, len(forig)):
	os.system('ffmpeg -i /name/your/path/'+ str(forig[i]) +' -ac 2 -strict -2 -filter_complex "[0:a][0:a]amerge=inputs=2[aout]" -map "[aout]" /name/your/path/audio/'+str(forig[i]))
	os.system('ffmpeg -i /name/your/path/'+str(forig[i]) +' -i /name/your/path/audio/'+str(forig[i])+' -map 0:0 -map 1:0 -vcodec copy -acodec copy /name/your/path/stereoVideo/'+str(forig[i]))
	print("\n\n\n\n\nFile "+str(forig)+ "is now stereo\n\n\n\n\n")

