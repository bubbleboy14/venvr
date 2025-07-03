import os, sys
from fyg.util import Named
from subprocess import getoutput

def log(*msg):
	print("venvr", *msg)

def err(*msg):
	log("error!", *msg)
	sys.exit()

class Basic(Named):
	def out(self, cmd):
		self.log("out", cmd)
		out = getoutput(cmd)
		self.log(out)
		return out

	def based(self, fname, base=None):
		return os.path.join(base or self.config.path.base, fname)