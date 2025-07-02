import os, inspect
from .util import Basic, RTMP

class Builder(Basic):
	def __init__(self, name, config):
		self.name = name
		self.config = config

	def build(self):
		self.log("build")
		self.dir()
		self.env()
		self.deps()

	def dir(self):
		bp = self.config.path.base
		self.log("dir", bp)
		os.makedirs(bp)

	def env(self):
		vp = self.config.path.venv
		self.log("env", vp)
		self.out("python3 -m venv %s"%(vp,))

	def deps(self):
		deps = self.config.deps
		self.log("deps", *deps)
		for dep in deps:
			self.out("%s install %s"%(self.config.path.pip, dep))

	def register(self, func):
		fsrc = inspect.getsource(func)
		name = fsrc.split(" ", 1).pop(1).split("(", 1).pop(0)
		rp = self.based("%s.py"%(name,))
		self.config.path.run.update(name, rp)
		caller = fsrc.startswith("class") and "%s()"%(name,) or name
		self.log("register", caller, rp)
		with open(rp, "w") as f:
			f.write(RTMP%(fsrc, caller))
		return name