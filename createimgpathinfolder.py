import os
import glob
import sys
dirpath = input("Enter the full path:")
if os.path.isdir(dirpath):
	list = os.listdir(dirpath)
	for file in list:
		ext = os.path.splitext(os.getcwd()+"/"+dirpath+"/"+file)[1]
		if ext in ['.jpg', '.png']:
			print(file)
		else:
			list.remove(file)
	print("\n" , len(list) , " files")
	outputtextpath = input("Enter the path.txt filename:")
	while os.path.isfile(os.getcwd()+"outputtextpath"):
		print("file already exist")
		outputtextpath = input("Enter the path.txt filename:")
	with open(outputtextpath + ".txt", "w") as outputtextfile:
		for fp in list:
			outputtextfile.write("data/" + os.path.basename(dirpath) + "/" + fp + "\n")
else:
	print("dir does not exist")