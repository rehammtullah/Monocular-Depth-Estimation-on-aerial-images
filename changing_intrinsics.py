import numpy as np
import os
with open('train.txt', 'r') as f:
	full_text = f.readlines()
	
	

	
for i in range((len(full_text))):
	path_to_intrinsics = os.path.join("dir_0",full_text[i].split("\n")[0].split(" ")[1]+'_cam.txt')
	print(path_to_intrinsics)
	with open(path_to_intrinsics, 'w') as wrt:
		wrt.write("72.153770,0.,60.955930,0.,74.826132,17.925600,0.,0.,1.")
	
