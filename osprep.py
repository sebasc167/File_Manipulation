import os
import sys
import os.path
import re
import shutil


#So we will work with file manipulation and rename

copy = 1
# 1. Copy a file from one place to another
def filecopy(filename = "",opath = os.getcwd(),npath = os.getcwd()):
	os.chdir(opath)
	if os.path.isfile(filename):
		try:
			f = open(filename)
		except IOError:
			print("There has been an error opening file, exiting now")
			sys.exit(-1)
		else:
			lines = f.readlines()
			for line in lines:
				line = line.strip("\n")
			document = "\n".join(lines)
			f.close()
			print("file contents copied and ready for transport")
	else:
		raise FileNotFoundError("The file is not found")
		sys.exit(-2)

	os.chdir(npath)
	nfile = filename.split(".")
	global copy
	nfile[0] += "_{}".format(copy)
	copy+=1
	nfilename = ".".join(nfile)
	print("file has been renamed: {} in destination".format(nfilename))
	final = os.path.join(os.getcwd(),nfilename)
	try:
		f1 = open(final,'w')
	except (IOError,FileNotFoundError):
		print("File IO error, exiting now")
		sys.exit(-3)
	else:
		f1.write(document)
		f1.close()
		print("{} has been renamed to {} and copied to\n {}".format(filename,nfilename,npath))

#2. Deleting a file in a specific filepath given by user as parameters 
def filedeletion(filename,pathy = os.getcwd()):
	'''Simple functin will delete a filename 
	within a folder'''
	os.chdir(pathy)
	path = os.getcwd()
	path = os.path.join(path,filename)
	if os.path.isfile(path):
		os.remove(filename)
		print(filename + " has been removed!")
		return True
	else:
		raise FileNotFoundError("File does not exist")
		return False

#3. Deleting all files and its copies in a directory
def filecpydel(filename,pathy = os.getcwd()):
	'''
	Will delete all instances of files with the
	filename given, including copies with regex
	'''
	f = re.compile(filename + r'(_\d+)?')
	for file in os.listdir(pathy):
		if f.search(file) != None:
			filepath = os.path.join(pathy,file) #file is not the absolute path! must attach all 
			print(filepath + " is being deleted!") 
			os.remove(filepath)

#4. Create a file in a directory
def filecreation(filename,path = os.getcwd()):
	os.chdir(path)
	pathname = os.path.join(os.getcwd(),filename)
	with open(pathname,'w') as f:
		pass
	print("I have created the file: " + filename)

#5. Find all instances of a string in a directory with direct files
def findinstances(find,path = os.getcwd()):
	freg = re.compile(find)
	os.chdir(path)
	for file in os.listdir(path):
		with open(file,'r') as f:
			lines = f.readlines()
			for line in lines:
				if freg.search(line) != None:
					print(file) #or... for absolute path
					#print(os.path.join(path,file))
					break

#6. Find all instances of a file in a directory
def catchall(findy="",path = os.getcwd()):
	found = 0
	os.chdir(path)
	for(root,dirs,files) in os.walk(path):
		if findy in files:
			print(os.path.join(root,findy))
			found+=1
	print(str(found) + " instances of " + findy + " in directory: " + path)

#7. Delete all occurences of the file in the given directory/folder
def deleteall(findy="",path = os.getcwd()):
	os.chdir(path)
	for(root,dirs,files) in os.walk(path):
		if findy in files:
			print("Removing {}".format(os.path.join(root,findy)))
			os.remove(os.path.join(root,findy))


#8. Find all instances of the string in the directory files, all of them even within subdirectories
def catchthemall(findy="",path = os.getcwd()):
	found = 0
	cond = re.compile(findy)
	os.chdir(path)
	for(root,dirs,files) in os.walk(path):
		for file in files:
			try:
				f = open(os.path.join(root,file),encoding="latin-1")
			except UnicodeDecodeError:
				print("Decoding error and will skip " + os.path.join(root,file))
				continue
			except Exception:
				print("Unknown error and will skip " + os.path.join(root,file))
				continue
			else:
				lines = f.readlines()
				for line in lines:
					if cond.search(line) != None:
						found+=1
						print(os.path.join(root,file))
						break
				f.close()
			
	print(str(found) + " instances of " + findy + " in directory: " + path)

def insertxt(file):
	with open(file,'w') as f:
		f.write("This is a new file\nand here is a new place\nso what now!")

def copypaste(opath = os.getcwd(),npath= os.getcwd(),newfilename="hey"):
	os.chdir(npath)
	os.mkdir(os.path.join(os.getcwd(),newfilename))
	os.chdir(os.path.join(os.getcwd(),newfilename))
	pathy = os.getcwd()
	os.chdir(opath)
	copied = 0

	for file in os.listdir(opath):
		#newfile = os.path.join(pathy,file)
		try:
			shutil.copy(file,pathy)
		except PermissionError:
			print("error with permission for file: + file")
			continue
		except Exception:
			print("unknown error for file: + file")
			continue
		else:
			copied += 1
			print("File: {} was copied from {} to {}, count = {}".format(file,opath,pathy,copied))
			continue

def deletedir(filepath = os.getcwd()):
	for file in filepath:
		pathy = os.path.join(filepath,file)
		os.remove(pathy)

copypaste(opath="F:",npath="C:/Users/Sara/Pictures",newfilename="Fotos201720")

#Unit tests

#filecreation("hey.txt")
#filecopy("hey.txt")
#filecopy("hey.txt")
#filecopy("hey.txt")
#findinstances("way")
#filecpydel("hey")
#filecopy("C:/Users/Sara/OneDrive/Python Upgrade","whoops.txt","C:/Users/Sara/OneDrive/Java")
#filedeletion("whoops.txt")
#filecpydel("hey")
#catchthemall("whoops","C:/Users/Sara/OneDrive/Java")
