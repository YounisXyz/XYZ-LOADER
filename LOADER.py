import os, sys
os.system("git pull")
try:
    __import__("Canvo").Xyz_Loader()
except Exception as e:
    exit(str(e))
