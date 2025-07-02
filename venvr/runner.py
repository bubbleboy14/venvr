from .util import Basic

class Runner(Basic):
	def __init__(self, name, config):
		self.name = name
		self.config = config

	def run(self, func, *args, **kwargs):
		path = self.config.path
		rp = path.run[func]
		self.log("run", rp, *args, **kwargs)
		return self.out("%s %s %s"%(path.py, rp,
			" ".join(['"%s"'%(a,) for a in args])))