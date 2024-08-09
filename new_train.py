with open('Out_file.txt', 'r') as f:
	full_text = f.readlines()

name_id = [x.split(".")[0] for x in full_text]

	
for i in range(1,(len(full_text)),2):
	with open('new_train_1.txt', 'a') as wrt:
		wrt.write("dir_0 ")
		wrt.write(name_id[i])
		wrt.write("\n")
	
