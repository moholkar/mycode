#!/usr/bin/python3


import shutil
import os

os.chdir('/home/student/mycode/')

shutil.move('aynor.obj' , 'moholkar_storage/')

xname= input("what is the new name for kerrigan.obj?") 

shutil.move('moholkar_storage/kerrigan.obj', 'moholkar_storage/' +xname)


