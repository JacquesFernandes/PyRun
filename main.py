'''
Main executor file
'''
import sys;
import os;
import time;
try:
	import PyLin;
except ImportError:
	print("PyRun:ERROR: PyLin module is missing!");

'''
Functions
'''
def dispWelcomeBanner():
	try:
		import PyLin;
		res = PyLin.retSysCom("which cowsay");
		if res is not "cowsay not found":
			os.system('cowsay -f tux "PyRun! Dealing with your Python code packages"');
	except ImportError:
		print("PyRun:ERROR: Could not display banner because PyLin not installed...");
		return();
	
def checkArgs():
	if len(sys.argv) >= 2:
		return(sys.argv[1:]);
	else:
		return(None);

def cli():
	#cli interface
	print("CLI (Command Line Interface) not yet implemented, please check the readme file again :P");
	
def fileCheck(zfname):
	res = PyLin.retSysCom("unzip -l "+zfname+" | grep .py");
	for line in res:
		if "pyrun-main.py" in line:
			print("PyRun: Found pyrun-main.py! Extracting files to ./"+zfname.strip(".pyrun.zip")+"-temp");
			return(True);
		#print(line);
	return(False);

def error(msg, ex=0):
	print("PyRun:ERROR: "+msg);
	if ex == 1:
		exit();

''' 
MAIN 
'''
if __name__ == "__main__":
	dispWelcomeBanner();
	args = checkArgs();
	if args is None:
		cli();
	else:
		zf = args[0]; #the zip file name
		if ".pyrun.zip" not in zf:
			error("Invalid package! It isn't a .pyrun.zip file",ex=1);
		if fileCheck(zf) is False:
			error("Not a vaild PyRun package, no pyrun-main.py found...",ex=1);
		try:
			folder = zf.strip(".pyrun.zip")+"-temp";
			os.mkdir(folder);
			os.system("unzip "+zf+" -d ./"+folder);
			print("\nStarting excution!");
			time.sleep(0.5);
			os.system("clear");
			args = sys.argv[2:];
			args_string = str();
			for val in args:
				args_string = args_string+val+" ";
			os.system("python ./"+folder+"/pyrun-main.py "+args_string);
			os.system("rm -r "+folder);
			#print("PyRun: Folder removed...");
		except FileExistsError:
			error("Odd, folder already exits....");
			os.system("rm -r "+folder);
			print("Folder removed...");
			exit();
		
		
