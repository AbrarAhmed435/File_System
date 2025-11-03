import os
from datetime import datetime

os.chdir('/home/abrar/Desktop/')

for dirpath,dirnames,filenames in os.walk('/home/abrar/Desktop/'):
    if 'first.py' in filenames:
        print("found ",dirpath)
        break
    print("current path",dirpath)
    print("directories:", dirnames)
    
    print("Files", filenames)
    print()
    

print(os.environ.get('HOME'))

PATH=os.path.join(os.environ.get('HOME'),'text.txt')

print(PATH)