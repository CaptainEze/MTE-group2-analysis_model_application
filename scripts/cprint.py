import os
import sys,time



def cprint(str):
	for i in str + "\n":
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(3/90)