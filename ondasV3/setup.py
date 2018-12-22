import os
import os.path
import sys
import time
import sqlite3
import datetime
import serial


from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY'] = r'C:\Users\Ramalho\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Ramalho\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


options1 = {
    'build_exe':
	{
        'include_files':
			[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),

			],
			
		'packages':
			[
			
			 'time', 'sys', 'datetime', 'serial', 'PIL',
			],
            "excludes": ["PyQt4.QtSql", "sqlite3", 
                                  "scipy.lib.lapack.flapack",
                                  "PyQt4.QtNetwork",
                                  "PyQt4.QtScript",
                                  "numpy.core._dotblas", 
                                  "PyQt5", "asyncio", 'email', 'html', 'http', 'xml', 'xmlrpc', 'win32com', 'pyDoc', 'pyWin', 'distutils' ],
                                  
    
    
    "optimize": 2
    },
}





setup(
    options = options1,
    name="pyArdu",
    version="0.1",
    description="pyArdu",
    shortcutName="pyArdu ",
    shortcutDir="Desktop",
    executables=[Executable(script = "main.py", base="Win32GUI")],
    

    
    
    )
    





