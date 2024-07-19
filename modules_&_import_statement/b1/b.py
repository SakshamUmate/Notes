
# Import Statements:

# os and sys are Python modules for interacting with the operating system and system-specific parameters.
# dirname, join, and abspath are functions from the os.path module for manipulating file paths.
# Setting the Path:

# sys.path.insert(0, abspath(join(dirname(__file__), '..'))): This line inserts the absolute path of the parent directory of the current file into the Python path (sys.path). This allows importing modules from the parent directory.
# Importing Module b from Package b1:

# from b1 import b: This line imports the module b from the package (directory) named b1.
# Function Definition:

# def pr(): return print("hello_world"): This defines a function pr that prints "hello_world."
# Function Invocation:

# pr(): Calls the pr function, resulting in the output "hello_world."
# Calling Function from Imported Module:

# b.j_k(): Calls the function j_k from module b (imported from the b1 package).





import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from a1 import a

def j_k():
    return print("hello_dear")
j_k()
a.pr()
