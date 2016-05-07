# PyRun
Python package executor. [Linux only]

#First time Usage
- sudo chmod +x setup.sh
- sudo ./setup.sh

#Usage
- Navigate to dir which has PyRun package ("x.pyrun.zip")
- run "pyrun" for a "cli-based" package executor which allows you to 
choose the package
- run "pyrun x.pyrun.zip" to execute the "x" package

#Creating a PyRun Package
- Create Python code, with multiple modules as files
- Create "pyrun-main.py" (this is the first script which is executed, 
sample should be available in this directory as "sample-pyrun-main.py")
- zip all files as "x.pyrun.zip" (where "x" is the name of the PyRun 
package)

#Arguments
- You can now add arguments to the command (which you want to be passed to the program) by the usual method.
- Your program (pyrun-main.py) will recieve the arguments as if it were executed by itself (just use your sys.argv values how you normally would)
- check the sample to understand
